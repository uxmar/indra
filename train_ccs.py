


class train_ccs(object):


    link_lines={('line_1','line_2'):(6,8),('line_2','line_1'):(8,6),('line_2','line_4'):(7,0),('line_4','line_2'):(0,7),('line_2','line_20'):(0,0),('line_20','line_2'):(0,0),('line_2','line_21'):(0,0),('line_21','line_2'):(0,0),('line_1','line_4'):(11,3),('line_4','line_1'):(3,11),('line_3','line_1'):(0,11),('line_1','line_3'):(11,0)}

    def __init__(self):
        self.line_station={
        'line_1':{0:'Propatria',1:'Perez Bonalde',2:'Plaza Sucre',3:'Gato Negro',4:'Agua Salud',5:'Cano Amarillo',6:'Capitolio',7:'La Hoyada',8:'Parque Carabobo',9:'Bellas Artes',10:'Colegio de Ingenieros',11:'Plaza Venezuela',12:'Sabana Grande',13:'Chacaito',14:'Chacao',15:'Altamira',16:'Miranda',17:'Los Dos Caminos',18:'Los Cortijos',19:'La California',20:'Petare',21:'Palo Verde','direction':('Palo Verde','Propatria')},
        'line_2':{0:'Mamera',1:'Antimano',2:'Carapita',3:'La Yaguara',4:'La Paz',5:'Artigas',6:'Maternidad',7:'Capuchinos',8:'Silencio','direction':('Silencio','Zoologico o Las Adjuntas')},
        'line_20':{0:'Caricuao',1:'Zoologico','direction':('Zoologico','Silencio o Zona Rental')},
        'line_21':{0:'Ruiz Pineda',1:'Las Adjuntas','direction':('Las Adjuntas','Silencio o Zona Rental')},
        'line_4':{0:'Teatros',1:'Nuevo Circo',2:'Parque Central',3:'Zona Rental','direction':('Zona Rental','Zoologico o Las Adjuntas')},
        'line_3':{0:'Ciudad Universitaria',1:'Los Simbolos',2:'La Bandera',3:'El Valle',4:'Los Jardines', 5:'Coche',6:'Mercado',7:'La Rinconada','direction':('La Rinconada','Plaza Venezuela')}}
        
        self.lines={('line_1','line_2'):(6,8),('line_2','line_1'):(8,6),('line_2','line_4'):(7,0),('line_4','line_2'):(0,7),('line_2','line_20'):(0,0),('line_20','line_2'):(0,0),('line_2','line_21'):(0,0),('line_21','line_2'):(0,0),('line_1','line_4'):(11,3),('line_4','line_1'):(3,11),('line_3','line_1'):(0,11),('line_1','line_3'):(11,0)}
        
        self.excepcion={'Caricuao':'Zoologico','Zoologico':'Zoologico','Ruiz Pineda':'Las Adjuntas','Las Adjuntas':'Las Adjuntas','El Silencio':'El Silencio','Teatros':'Zona Rental','Nuevo Circo':'Zona Rental','Parque Central':'Zona Rental','Zona Rental':'Zona Rental'}
        self.direction={'line_1':('Propatria','Palo Verde'),'line_2':('exception','Silencio')}

    def find_station(self,station):
    #~ Obtengo numero del indice de las estaciones ingresadas
    #~ por el usuario.
        for line_name,value in self.line_station.items():
            for k,v in value.items():
                if station == v:
                        return k, line_name

    def get_direction(self,line,type_sort):
        if type_sort=='down':
            return self.line_station[line]['direction'][0]
        else:
            return self.line_station[line]['direction'][1]


    def get_route(self,from_1,up_1):
    #~ Get the route to trace
        list_num=[]
        list_routed_sorted=[]
        i=0
        dict_routed={'Direction':'','Route':None,'Line':''}
        if from_1[0] < up_1[0]:
            [list_num.append(i) for i in range(from_1[0],up_1[0]+1)]
            for index in sorted(list_num):
                if self.line_station[from_1[1]][index]:
                    list_routed_sorted.insert(i,self.line_station[from_1[1]][index])
                    i=i+1
            dict_routed.update({'Route':list_routed_sorted})
            
            dict_routed.update({'Direction':self.line_station[from_1[1]]['direction'][0]})
            
            
            dict_routed.update({'Line':from_1[1]})
            
            #~ print 'DIRECCION', self.get_direction(from_1[1],'down')
            
            
            return dict_routed
        else:
            [list_num.append(i) for i in range(up_1[0],from_1[0]+1)]
            for index in sorted(list_num,reverse=True):
                if self.line_station[from_1[1]][index]:
                    list_routed_sorted.insert(i,self.line_station[from_1[1]][index])
                    i=i+1
            dict_routed.update({'Route':list_routed_sorted})
            dict_routed.update({'Direction':self.line_station[from_1[1]]['direction'][1]})
            dict_routed.update({'Line':from_1[1]})
            
            #~ print 'DIRECCION', self.get_direction(from_1[1],'up')
            return dict_routed

    def get_line_option(self,station_a,station_b,lines,dict_lines,dict_sort,j,lines_accumulated,qty, tuple_done):
        #~ Genero 2 diccionarios:
        #~ 1.- Diccionario de lineas con estaciones a recorrer dentro de la linea.
        #~ 2.- Diccionario de lineas con el orden correcto a recorrer.
        #~ 3.- Diccionario de tuplas a eliminar para realizar la proxima busqueda con el dict de lines
        
        trunk=False
        i=0
        for line,station in lines.items():
            i=i+1
            
            #~ print '' 
            #~ print 'lines_accumulated',lines_accumulated
            #~ print 'LINE', line
            #~ print 'station', station
            #~ print 'station_a', station_a
            #~ print 'dict_lines',dict_lines
            #~ print 'dict_sort',dict_sort
            #~ print 'tuple_done',tuple_done
            
            if not line in lines_accumulated and not dict_lines.get(line[1],): 
                if line[0]==station_a[1]:
                    if (((line[1],station_b[1]) in lines) and dict_lines):
                        #~ print 'A1'
                        dict_lines.update({line[0]:(dict_lines[line[0]][0],station[0])})
                        j=j+1
                        dict_sort.update({line[0]:j})
                        tuple_done.insert(j,line)
                        x,y=lines[line[1],station_b[1]]
                        dict_lines.update({line[1]:(station[1],x)})
                        j=j+1
                        dict_sort.update({line[1]:j})
                        tuple_done.insert(j,(line[1],station_b[1]))
                        dict_lines.update({station_b[1]:(y,station_b[0])})
                        j=j+1
                        dict_sort.update({station_b[1]:j})
                        trunk=True 
                        break

                    if not dict_lines.get(line[0],):
                        #~ print 'A2'
                        dict_lines.update({line[0]:(station_a[0],station[0])})
                        lines_accumulated.append((line[1],line[0]))
                        j=j+1
                        dict_sort.update({line[0]:j})
                        tuple_done.insert(j,line)

                    if  dict_lines.get(line[1],) and len(dict_lines[line[1]])==1:
                        #~ print 'A3'
                        dict_lines.update({station_a[1]:(dict_lines[station_a[1]][0],station[0])})
                        lines_accumulated.append((line[1],line[0]))
                        j=j+1
                        dict_sort.update({line[1]:j})
                        tuple_done.insert(j,line)    

                    if not dict_lines.get(line[1],):
                        #~ print 'A4'
                        dict_lines.update({line[1]:(station[1],)})

                    if dict_lines.get(line[0],) and len(dict_lines[line[0]])==1:
                        #~ print 'A5'
                        dict_lines.update({line[0]:(dict_lines[line[0]][0],station[0])})
                        lines_accumulated.append((line[1],line[0]))
                        j=j+1
                        dict_sort.update({line[0]:j})
                        tuple_done.insert(j,line)

                    if station_b[1]==line[1]:
                        #~ print 'A6'
                        dict_lines.update({line[1]:(dict_lines[line[1]][0],station_b[0])})
                        j=j+1
                        dict_sort.update({line[1]:j})
                        trunk=True
                        break
                    station_a=(station[1],line[1])
        #~ print ''
        if not trunk:
            
            qty=qty+1
            if qty>2 and i==len(lines):
                #~ print 'salgo pero no valgo'
                return {}, tuple_done, {}, []
            else:
                #~ print 'Me vuelvo a llamar'
                return self.get_line_option(station_a,station_b,lines,dict_lines,dict_sort,j,lines_accumulated,qty,tuple_done)
        else:
            #~ print 'Saliendo'
            return dict_lines, tuple_done, dict_sort, tuple_done
        

    def get_dict_option(self,station_a,station_b):
        #~ Retorna 2 diccionarios:
        #~ 1.- Diccionario con opcion 1, opcion 2, etc, cada opcion tiene un diccionario de lineas con
        #~ las estaciones a recorrer dentro de esa misma linea.
        #~ 2.- Diccionario con opcion1, opcion2, cada opcion tiene un diccionario de linea:num, el num
        #~ es el orden con el que deberian recorrerse las estaciones, esto para organizar el diccionario
        #~ devuelto en 1.

        state=False
        dict_options={}
        dict_sort_option={}
        lines_pair=self.lines
        
        route_done=[]
        tuple_done_options=[]
        i=0
        qty=0
        qty_neg=0
        
        while state==False:
            dict_lines={}
            dict_sort={}
            lines_accumulated=[]
            tuple_done=[]
            drop_lines=[]
            j=-1
            
            dict_lines,drop_lines,dict_sort,tuple_done= self.get_line_option(station_a,station_b,lines_pair,dict_lines,dict_sort,j,lines_accumulated,qty,tuple_done)
            
            #~ print 'TUPLE DONE', tuple_done
            #~ print 'dict_linessss', dict_lines
            #~ print 'dict_sortttt', dict_sort
            #~ print 'drop_linessss', drop_lines
             
            if dict_lines:
                dict_options.update({i:dict_lines})
                dict_sort_option.update({i:dict_sort})
                tuple_done_options.append(tuple(tuple_done))
                i=i+1
            
            for drop in drop_lines:
                if lines_pair.get(drop,):
                    del lines_pair[drop]
    
            for each_line in lines_pair:
                if each_line[0] != station_a[1]:
                    qty_neg=qty_neg+1

            if len(lines_pair) == qty_neg:
                state=True
            qty_neg=0
        #~ print ''
        #~ print 'DICT_OPTIONS', dict_options
        #~ print 'dict_sort_option', dict_sort_option
        #~ print 'tuple_done_option', tuple_done_options
        
        
        lines_2=self.link_lines
        for tuples in tuple_done_options:
            for pair_line in tuples:
                tuple1_add=lines_2[pair_line]
                del lines_2[pair_line]

                dict_lines={}
                dict_sort={}
                lines_accumulated=[]
                j=-1
                
                #~ print 'lines EEEEEEEEE1111111111111', lines_2

                dict_lines,drop_lines,dict_sort,tuple_done= self.get_line_option(station_a,station_b,lines_2,dict_lines,dict_sort,j,lines_accumulated,qty,tuple_done)
                
                #~ print 'dict_linessssss', dict_lines
                
                lines_2.update({pair_line:tuple1_add})

                if dict_lines:
                    dict_options.update({i:dict_lines})
                    dict_sort_option.update({i:dict_sort})
                    i=i+1
        #~ print 'tuple_done_option', tuple_done_options
        #~ print 'dict_options SSSS', dict_options

        return dict_options,dict_sort_option



    def get_station_line(self,dict_lines,dict_sort):
        #~ Retorna 1 diccionario de listas:
        #~ Diccionario de opciones, donde cada opcion tiene una lista de tuplas,
        #~ (num,line), num es el numero de la estacion y line la linea donde se encuenta.
            
        dict_station_line={}
        for key,sort_values in sorted(dict_sort.iteritems(),key=lambda(key,sort_values):(sort_values,key)):
            i=0
            for k,v in dict_lines.items():
                if key==k:
                    dict_station_line.update({k:[]})
                    for key,value in sorted(sort_values.iteritems(), key=lambda(key,value):(value,key)):
                        if v[key]:
                            dict_station_line[k].insert(i,((v[key][0],key),(v[key][1],key)))
                            i=i+1
        return dict_station_line

    def get_route_options(self,dict_station_line):
        
        dict_route={}
        for key,value in dict_station_line.items():
            i=0
            list_route=[]
            for from_up in value:
                list_route.insert(i,self.get_route(from_up[0],from_up[1]))
                i=i+1
            dict_route.update({key:list_route})
        return dict_route
train_ccs()


def main():

    #1 opcion
    #~ a='Palo Verde' 
    #~ b='La Rinconada'
    #~ a='La Rinconada'
    #~ b='Palo Verde'

    #1 opcion
    #~ a='La Bandera'
    #~ b='Parque Central'
    #~ a='Parque Central'
    #~ b='La Bandera'
    
    #2 opciones
    #~ a='Bellas Artes'
    #~ b='Teatros'
    #~ a='Teatros'
    #~ b='Bellas Artes' # Me falta una opcion **

    #2 opciones
    #~ a='El Valle'
    #~ b='Carapita'
    #~ a='Carapita'
    #~ b='El Valle' # me falta una opcion

    #2 opciones
    #~ a='Sabana Grande'
    #~ b='La Paz'
    #~ a='La Paz'
    #~ b='Sabana Grande'

    # 2 opciones
    #~ a='Zona Rental' # me falta una opcion **
    #~ b='La Yaguara'
    #~ a='La Yaguara'
    #~ b='Zona Rental' # me falta una opcion **

    #2 opciones
    #~ a='Coche'
    #~ b='Zoologico'
    #~ a='Zoologico' # no aparecio nada ???
    #~ b='Coche' 

    #2 opciones
    #~ a='Coche'
    #~ b='Las Adjuntas' 
    #~ a='Las Adjuntas'
    #~ b='Coche' # me falta una opcion **
    
    #2 opciones
    #~ a='Miranda' # me falta una opcion **
    #~ b='Zoologico'
    #~ a='Zoologico'# no aparecio nada
    #~ b='Miranda'
    
    #2 opciones
    #~ a='Nuevo Circo'  # me falta una opcion **
    #~ b='Las Adjuntas'
    #~ a='Las Adjuntas'
    #~ b='Nuevo Circo'  # me falta una opcion **

    #1 opcion
    #~ a='Zoologico'
    #~ b='Las Adjuntas'
    #~ a='Las Adjuntas'# no aparecio nada
    #~ b='Zoologico'
    
    a="Capitolio"
    b="Mercado"

    
    d=train_ccs()
    station_a = d.find_station(a)
    station_b = d.find_station(b)
    
    #~ print 'station_a', station_a
    #~ print 'station_b',station_b
    
    if station_a[1]==station_b[1]:
        print 'aa', d.get_route(station_a,station_b)
    else:
        dict_lines, dict_sort = d.get_dict_option(station_a,station_b)
        dict_station_line = d.get_station_line(dict_lines,dict_sort)
        print 'bb', d.get_route_options(dict_station_line)
    

if __name__ == '__main__':
    main()



