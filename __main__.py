import kivy
kivy.require('1.1.3')

from kivy.properties import NumericProperty
from kivy.app import App
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

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import random
from train_ccs import train_ccs
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.accordion import Accordion, AccordionItem
import re

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

class Showcase(Screen):
    pass

class StandardWidgets2(Screen):
    value = NumericProperty(0)
    ce = ComboEdit()
    
    def get_route(self):
        print 'ENTREEEEEEEEEEEEE'
        print 'LIST', self.ce.list_station
        

        #~ s2 = StandardWidgets()
        #~ station_a=s2.station_a
        #~ aa=s2.station_a
        #~ station_b=s2.station_b
#~ 
        #~ d=train_caracas()
        #~ station_a = d.find_station(station_a)
        #~ station_b = d.find_station(station_b)
        #~ 
        #~ print 'station_aaa', station_a
        #~ print 'station_bbbb',station_b
#~ 
        #~ if station_a[1]==station_b[1]:
            #~ a= d.get_route(station_a,station_b)
            #~ print a 
        #~ else:
            #~ dict_lines, dict_sort = d.get_dict_option(station_a,station_b)
            #~ dict_station_line = d.get_station_line(dict_lines,dict_sort)
            #~ a= d.get_route_options(dict_station_line)
            #~ print a
        a= 'Hola Gaviotinaaaa'
        print 'a',a
        return 'NON ENTIENDO'
    

class StandardWidgets(Screen):
    
    rtsstr = StringProperty("".join(("Maternidad,,,Sabana Grande,,,Maternidad,,,",
                        "Substrate1,,,La Hoyada,,,La Bandera",
                        ",,,Agua Salud,,,Altamira,,,substrate_",
                        "silicon,,,")))

    def get_string_route(self, dict_route):
        
        for option in dict_route:
            print 'OPTION', option +1
            
            #~ print 'ANTESSS', dict_route[option]
            
            print ''
            for direction_route in dict_route[option]:
                #~ print 'DESPUES',direction_route
                #~ print 'DIRECTION',direction_route['Direction']
                direction = 'Tomar tren con direccion ' + direction_route['Direction'] + '\n' + 'Recorrer las Estaciones:'
                #~ print direction
                #~ print 'ROUTE', direction_route['Route']
                
                stations = ','.join(direction_route['Route'])
                
                #~ for i in direction_route['Route']:
                    #~ direction = + '',i
                
                direction = direction + '\n' + stations
                
                
                
                print direction
            return direction
                
                #~ print 'DIRECTION', direction
                #~ print 'STATIONS',stations
                
                
            #~ for list_dict in dict_route[option]:
                #~ print 'LISTA DE DICCIONARIOS',list_dict


    def get_route(self,instance):
        print 'ENTREEEEEEEEEEEEE'
        
        d=train_caracas()
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
        
        self.route.text = self.get_string_route(a)
            
        #~ self.route.text =''.join('{}{}'.format(key, val) for key, val in a.items())

    def on_text(self, instance, value):
        if value == '':
            instance.options=[]
        else:
            match = re.findall("(?<=,{3})(?:(?!,{3}).)*?%s.*?(?=,{3})" % value,\
                                self.rtsstr, re.IGNORECASE)
            #using a set to remove duplicates, if any.
            instance.options = list(set(match))
        instance.drop_down.open(instance)

sm = ScreenManager()
sm.add_widget(StandardWidgets(name='menu'))
sm.add_widget(StandardWidgets2(name='settings'))

class Trainccs(App):

    def build(self):
        return sm

if __name__ == '__main__':
    Trainccs().run()
