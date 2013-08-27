import kivy
kivy.require('1.1.3')

from kivy.app import App
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
from kivy.properties import StringProperty, ListProperty
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.modalview import ModalView
import random
from train_ccs import train_ccs
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView
import re
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

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
        print 'list_station', self.list_station
        print 'VALUE', value


class RouteResult(ModalView):

    def __init__(self,list_route):
        super(RouteResult, self).__init__(auto_dismiss=False)
        self.clear_widgets()
        self.list_route = list_route
        self.on_open = self.show_view_result

    def show_view_result(self):

        root = Accordion(orientation='vertical',anchor_x='center')
        i=1
        for x in self.list_route:
            item = AccordionItem(title='OPCION ' + str(i))
            boxl = BoxLayout(orientation= 'vertical',height= "500dp",size_hint_y= None,)
            gl = GridLayout(cols=1,row_default_height= "20dp",row_force_default=True)

            for m in x:
                p= Label(text=m,halign='left',text_size=(500, None))
                #~ p = Label(text='[color=ff3333]Hello[/color][color=3333ff]World[/color]', markup = True)
                gl.add_widget(p)

            boxl.add_widget(gl)
            item.add_widget(boxl)
            root.add_widget(item)
            button = Button(text="Go Back", auto_dismiss=False, size_hint=(0.2, 0.1), pos_hint= {'center_x':.5, 'center_y':.7})
            button.bind(on_press=self.dismiss)
            boxl.add_widget(button)
            i=i+1
        self.add_widget(root)


class StandardWidgets(Screen):

    rtsstr = StringProperty("".join(("Maternidad,,,Sabana Grande,,,Maternidad,,,",
                        "Substrate1,,,La Hoyada,,,La Bandera",
                        ",,,Agua Salud,,,Altamira,,,substrate_",
                        "silicon,,,")))

    def get_string_route(self, dict_route):
        
        list_route =[]
        list_option=[]
        list_list_route = []
        
        for option in dict_route:
            for direction_route in dict_route[option]:
                list_route.append('Linea: ')
                list_route.append('Direccion: ' + direction_route['Direction'])
                list_route.append('Estaciones:')
                
                for station in direction_route['Route']:
                    list_route.append(station)
                
                #~ list_route.append(', '.join(direction_route['Route']))
                
                print 'LIST ROUTE', list_route
                
            if list_route:
                print 'ENTRE'
                list_list_route.append(list_route)
            print 'list_list_route', list_list_route
                
            list_route =[]

        return list_list_route

    def get_route(self, instance):
        
        d=train_ccs()
        station_a = d.find_station(self.station_a.text)
        station_b = d.find_station(self.station_b.text)
        
        print 'station_aaa', station_a
        print 'station_bbbb',station_b

        if station_a[1]==station_b[1]:
            a= d.get_route(station_a,station_b)
            print a 
        else:
            dict_lines, dict_sort = d.get_dict_option(station_a,station_b)
            dict_station_line = d.get_station_line(dict_lines,dict_sort)
            a= d.get_route_options(dict_station_line)
            print a

        

        route = RouteResult(self.get_string_route(a))
        route.open()

    def on_text(self, instance, value):
        if value == '':
            instance.options=[]
        else:
            match = re.findall("(?<=,{3})(?:(?!,{3}).)*?%s.*?(?=,{3})" % value,\
                                self.rtsstr, re.IGNORECASE)
            #using a set to remove duplicates, if any.
            instance.options = list(set(match))
        instance.drop_down.open(instance)


 
class TrainccsApp(App):

    def __init__(self):
        super(TrainccsApp, self).__init__()

TrainccsApp().run()
