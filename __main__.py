import kivy
kivy.require('1.1.3')

from kivy.uix.listview import ListView
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
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
import re

#~ list_route=[]


#~ class BuddyList(BoxLayout):
    #~ list_view = list_route
    
    #~ def __init__(self, list_route):
        
        #~ super(BuddyList, self).__init__()
        #~ self.app = Orkiv.get_running_app()
        #~ self.list_view.adapter.data = sorted(self.app.xmpp.client_roster.keys())

#~ class TrainRoot(ModalView):
    #~ 
    #~ def __init__(self):
        #~ super (TrainRoot,self).__init__()
        #~ self.buddy_list = BuddyList()
        #~ self.add_widget(self.buddy_list)
        

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


class StandardWidgets(Screen):
    
    #~ def __init__(self):
        #~ list_route = []
    
    
    rtsstr = StringProperty("".join(("Maternidad,,,Sabana Grande,,,Maternidad,,,",
                        "Substrate1,,,La Hoyada,,,La Bandera",
                        ",,,Agua Salud,,,Altamira,,,substrate_",
                        "silicon,,,")))

    def get_string_route(self, dict_route):
        
        list_route =[]
        
        for option in dict_route:
            list_route.append('OPTION  ' + str(option +1))
            
            for direction_route in dict_route[option]:
                direction = 'Tomar tren con direccion ' + direction_route['Direction'] + '\n' + 'Recorrer las Estaciones:'
                list_route.append('Tomar tren con direccion ' + direction_route['Direction'])
                list_route.append('Recorrer las Estaciones:')
                list_route.append(', '.join(direction_route['Route']))
                
                print direction
                print '-------'
        print 'LIST ROUTE', list_route
        return list_route

    def get_route(self,instance):
        
        #~ self.clear_widgets()
        #~ self.final = Label(text="Hello World")
        #~ self.add_widget(self.final)
        d=train_ccs()
        station_a = d.find_station(self.station_a.text)
        station_b = d.find_station(self.station_b.text)
        
        print 'station_aaa', station_a
        print 'station_bbbb',station_b

        if station_a[1]==station_b[1]:
            a= d.get_route(station_a,station_b)
            #~ self.get_string_route(a)
            print a 
        else:
            dict_lines, dict_sort = d.get_dict_option(station_a,station_b)
            dict_station_line = d.get_station_line(dict_lines,dict_sort)
            a= d.get_route_options(dict_station_line)
            #~ self.get_string_route(a)
            print a

        self.get_string_route(a)
            #~ self.clear_widgets()
            #~ self.buddy_list = BuddyList(self.get_string_route(a))
            #~ self.add_widget(self.buddy_list)




        #~ self.clear_widgets()
        #~ list_view = ListView(item_strings=[str(index) for index in self.get_string_route(a)])
        #~ self.add_widget(list_view)


        #~ modal = TrainRoot()
        #~ modal.open()


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
