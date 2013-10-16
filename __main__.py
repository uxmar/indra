import kivy
kivy.require('1.1.3')

from kivy.app import App
from kivy.lang import Builder
from stations import master_data
from kivy.uix.scrollview import ScrollView
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.properties import NumericProperty
from kivy.properties import OptionProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.modalview import ModalView
import random
from train_ccs import train_ccs
from kivy.uix.textinput import TextInput
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView
import re
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.graphics import Line
from functools import partial
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown


class ComboEdit(TextInput):
    '''
    This class defines a Editable Combo-Box in the traditional sense
    that shows it's options 
    '''
    
    options = ListProperty(('', ))
    list_station=[]
    '''
    :data:`options` defines the list of options that will be displayed when
    touch is released from this widget.ComboEdit
    '''

    def __init__(self, **kw):
        ddn = self.drop_down = DropDown()
        ddn.bind(on_select=self.on_select)
        super(ComboEdit, self).__init__(**kw)

    def on_options(self, instance, value):
        ddn = self.drop_down
        # clear old options
        ddn.clear_widgets()
        for option in value:
            # create a button for each option
            but = Button(text=option,
                        size_hint_y=None,
                        height='36sp',
                        # and make sure the press of the button calls select
                        # will results in calling `self.on_select`
                        on_release=lambda btn: ddn.select(btn.text))
            ddn.add_widget(but)

    def on_select(self, instance, value):
        # on selection of Drop down Item... do what you want here
        # update text of selection to the edit box
        self.text = value
        self.list_station.append(value)

class ColorLayout(FloatLayout):
    pass

class MultiLineLabel(Button):
    def __init__(self, **kwargs):
        super(MultiLineLabel, self).__init__( **kwargs)
        self.text_size = self.size
        self.bind(size= self.on_size)
        self.bind(text= self.on_text_changed)
        self.size_hint_y = None # Not needed here

    def on_size(self, widget, size):
        self.text_size = size[0], None
        self.texture_update()
        if self.size_hint_y == None and self.size_hint_x != None:
            self.height = max(self.texture_size[1]+32, self.line_height)
        elif self.size_hint_x == None and self.size_hint_y != None:
            self.width  = self.texture_size[0]

    def on_text_changed(self, widget, text):
        self.on_size(self, self.size)

class OptionsView(ModalView):

    def __init__(self,list_sta_trans):
        super(OptionsView, self).__init__(auto_dismiss=False)
        self.clear_widgets()
        self.list_sta_trans = list_sta_trans
        self.on_open = self.show_option_view

    def show_list_stations(self, *args, **kwargs):
        self.clear_widgets()
        color = ColorLayout()
        boxl = BoxLayout(orientation= 'vertical',anchor_y= "top")
        grid = GridLayout(cols=1, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height')) 
        scroll = ScrollView(size_hint=(None, None))
        scroll.size = (Window.width, Window.height)
        scroll.center = Window.center
        l_space = MultiLineLabel(text='',font_size="16dp", background_color=(255,255,255,255), markup=True)
        grid.add_widget(l_space)

        for j in args[0]:
            text_st = '[color=333333]' + j + '[/color]'
            l = MultiLineLabel(text=text_st,font_size="16dp", background_color=(255,255,255,255), markup=True)
            grid.add_widget(l)
            
        button_back = Button(text="Go Back", auto_dismiss=False, size_hint=(None, None), pos_hint= {'center_x':.5, 'center_y':.7})
        button_back.height="50dp"
        button_back.width="100dp"
        button_back.bind(on_press = lambda widget: self.show_view_list_path(args[1]))
        
        scroll.add_widget(grid)
        boxl.add_widget(scroll)
        boxl.add_widget(button_back)
        color.add_widget(boxl)
        self.add_widget(color)

    def show_view_list_path(self, *args, **kwargs):
        
        self.clear_widgets()
        color = ColorLayout()
        boxl = BoxLayout(orientation= 'vertical',anchor_y= "top")
        grid = GridLayout(cols=1,size_hint_x=None, width=Window.width,pos_hint= {'center_x':.5, 'center_y':.5})
        
        for i in args[0]:
            text = '[color=333333]' + i['text'] + '[/color]'
            l = MultiLineLabel(text=text,font_size="16dp", background_color=(255,255,255,255), markup=True)
            i['stations'] and l.bind(on_press = partial(self.show_list_stations, i['stations'],args[0]))
            grid.add_widget(l)
            
        button_back = Button(text="Go Back", auto_dismiss=False, size_hint=(None, None), pos_hint= {'center_x':.5, 'center_y':.7})
        button_back.height="50dp"
        button_back.width="100dp"
        button_back.bind(on_press = lambda widget: self.show_option_view())
        
        boxl.add_widget(grid)
        boxl.add_widget(button_back)
        color.add_widget(boxl)
        self.add_widget(color)

    def show_option_view(self):
        color = ColorLayout()
        boxl = BoxLayout(orientation= 'vertical',anchor_y= "top")
        gl1 = GridLayout(cols=3,size_hint_x=None, width="300dp",row_default_height= "60dp",row_force_default=True,pos_hint= {'center_x':.5, 'center_y':.7})
        text=''
        i=0
        for resume in self.list_sta_trans:
            i=i+1
            
            text = 'OPCION ' + str(i)
            color_text = '[color=000000]' + text + '[/color]'
            label_option = Label(text=color_text,size_hint=(None, None),markup=True)
            label_option.width="90dp"
            gl1.add_widget(label_option)
            
            text = 'Estaciones: '+str(resume['stations'] \
            )+'\nTransferencias: '+str (resume['transfers'])
            color_text = '[color=000000]' + text + '[/color]'
            label_info = Label(text=color_text,halign='left',markup=True)
            label_info.width="130dp"
            gl1.add_widget(label_info)
            
            button = Button(text='Button \n HOLA', size_hint=(None, None))
            button.height="60dp"
            button.width="80dp"
            button.bind(on_press = partial(self.show_view_list_path, resume['path']))
            gl1.add_widget(button)
        
        button_back_1 = Button(text="Go Back", auto_dismiss=False, size_hint=(None, None), pos_hint= {'center_x':.5, 'center_y':.7})
        button_back_1.height="50dp"
        button_back_1.width="100dp"
        button_back_1.bind(on_press=self.dismiss)
        
        boxl.add_widget(gl1)
        boxl.add_widget(button_back_1)
        color.add_widget(boxl)
        self.add_widget(color)

class StandardWidgets(Screen):

    rtsstr = StringProperty("".join(("Caricuao,,,Zoologico,,,Caricuao",
    
                        ",,,Propatria,,,Perez Bonalde,,,Plaza Sucre",
                        ",,,Gato Negro,,,Agua Salud,,,Cano Amarillo",
                        ",,,Capitolio,,,La Hoyada,,,Parque Carabobo",
                        ",,,Bellas Artes,,,Colegio de Ingenieros,,,Plaza Venezuela",
                        ",,,Sabana Grande,,,Chacaito,,,Chacao",
                        ",,,Altamira,,,Miranda,,,Los Dos Caminos",
                        ",,,Los Cortijos,,,La California,,,Palo Verde,,,Petare",
                        
                        ",,,Mamera,,,Antimano,,,Carapita,,,La Yaguara",
                        ",,,La Paz,,,Artigas,,,Maternidad,,,Capuchinos,,,Silencio",
                        
                        ",,,Ruiz Pineda,,,Las Adjuntas",
                        
                        ",,,Teatros,,,Nuevo Circo,,,Parque Central,,,Zona Rental",
                        
                        ",,,Ciudad Universitaria,,,Los Simbolos,,,La Bandera",
                        ",,,El Valle,,,Los Jardines,,,Coche,,,Mercado",
                        ",,,La Rinconada,,,")))

    def get_route(self, instance):
        
        class_train_ccs = train_ccs()
        
        list_sta_trans = class_train_ccs.get_options(self.station_a.text,self.station_b.text)
        
        route = OptionsView(list_sta_trans)
        route.open()

    def on_text(self, instance, value):
        if value == '':
            instance.options=[]
        else:
            match = re.findall("(?<=,{3})(?:(?!,{3}).)*?%s.*?(?=,{3})" % value,\
                                self.rtsstr, re.IGNORECASE)
            #using a set to remove duplicates, if any.
            instance.options = list(set(match))
        if instance.get_parent_window(): 
            instance.drop_down.open(instance)

class MainWindow(Screen):
    pass

class TrainccsApp(App):

    def __init__(self):
        super(TrainccsApp, self).__init__()

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow(name='mainwindow'))
        sm.add_widget(StandardWidgets(name='inputstation'))
        
        Window.bind(on_keyboard=self.hook_keyboard)

        return sm

    def hook_keyboard(self, window, key, *largs):
        if key == 27: # BACK
        # Irrelevant code
            pass
        elif key in (282, 319): # SETTINGS
        # Irrelevant code
            pass

TrainccsApp().run()

