


from stations import master_data
from copy import deepcopy

class train_ccs(object):

    def find_all_paths(self,graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def recursive_dfs(graph, start, path=[]):
      path=path+[start]
      for node in graph[start]:
        if not node in path:
          path=recursive_dfs(graph, node, path)
      return path

    def get_trans(self,path,class_mdata,dict_connec):
        list_tu_trans,qty_trans=[],0
        for i,j in zip(path,path[1::]):
            if dict_connec.get(i,) and j in dict_connec[i].keys(): 
                if (i,j) == ('Capuchinos','Teatros') and ('Mamera','Antimano') in list_tu_trans:
                    pass
                elif (i,j) == ('Mamera','Antimano') and ('Capuchinos', 'Teatros') in list_tu_trans:
                    pass
                elif (i,j) == ('Mamera','Ruiz Pineda') and ('Teatros','Capuchinos') in list_tu_trans:
                    pass
                elif (i,j) == ('Teatros','Capuchinos') and ('Mamera','Ruiz Pineda') in list_tu_trans:
                    pass
                elif (i,j) == ('Plaza Venezuela','Ciudad Universitaria') and \
                (path[path.index(i)-1],'Plaza Venezuela') in list_tu_trans:
                    pass
                elif (i,j) == ('Plaza Venezuela','Zona Rental') and \
                (path[path.index(i)-1],'Plaza Venezuela') in list_tu_trans:
                    pass
                else:
                    list_tu_trans.append((i,j))
                    qty_trans = qty_trans + 1
        list_tu_trans = list(set(list_tu_trans))
        return list_tu_trans, qty_trans

    def line_2(self,sta_i,class_mdata,path,dict_connec):
        
        #Zona Rental - Las Adjuntas / Zona Rental - Zoologico
        #~ if list_sta_partial[0] in class_mdata.direction['4'].keys() and \
        #~ path[len(path)-1] in class_mdata.direction['99'].keys():
            #~ if dict_connec.get('Teatros',) and \
            #~ dict_connec['Teatros'].get('Capuchinos',):
                #~ dict_connec['Teatros'].pop('Capuchinos')
            #~ if dict_connec.get('Mamera',) and \
            #~ dict_connec['Mamera'].get('Ruiz Pineda',):
                #~ dict_connec['Mamera'].pop('Ruiz Pineda')
        
        #Silencio - Las Adjuntas / Silencio - Zoologico
        #~ if list_sta_partial[0] in class_mdata.direction['2'].keys() and \
        #~ path[len(path)-1] in class_mdata.direction['99'].keys():
            #~ if dict_connec.get('Mamera',) and \
            #~ dict_connec['Mamera'].get('Caricuao',):
                #~ dict_connec['Mamera'].pop('Caricuao')
        
        #Zoologico - Zona Rental
        #~ if list_sta_partial[0] in class_mdata.direction['20'].keys() and \
        #~ path[len(path)-1] in class_mdata.direction['4'].keys():
            #~ if dict_connec.get('Capuchinos',) and \
            #~ dict_connec['Capuchinos'].get('Teatros',):
                #~ dict_connec['Capuchinos'].pop('Teatros')
            #~ if dict_connec.get('Ruiz Pineda',) and \
            #~ dict_connec['Ruiz Pineda'].get('Mamera',):
                #~ dict_connec['Ruiz Pineda'].pop('Mamera')
        
        #Las Adjuntas - Zona Rental
        #~ if list_sta_partial[0] in class_mdata.direction['21'].keys():
            #~ 
            #~ if 'Silencio' not in path or path[len(path)-1] in class_mdata.direction['2'].keys():
            #~ 
                #~ for i in path:
                    #~ if dict_connec.get('Capuchinos',) and \
                    #~ dict_connec['Capuchinos'].get('Teatros',):
                        #~ dict_connec['Capuchinos'].pop('Teatros')
                    #~ if dict_connec.get('Mamera',) and \
                    #~ dict_connec['Mamera'].get('Antimano',):
                        #~ dict_connec['Mamera'].pop('Antimano')
            
        
        #Zoologico - Silencio
        #~ if list_sta_partial[0] in class_mdata.direction['20'].keys() and \
        #~ path[len(path)-1] in class_mdata.direction['2'].keys():
            #~ if dict_connec.get('Caricuao',) and \
            #~ dict_connec['Caricuao'].get('Mamera',):
                #~ dict_connec['Caricuao'].pop('Mamera')


        #~ print 'list_staaaa', list_sta_partial
        #Linea 4(Zona Rental) - Linea 2 / Silencio
        if sta_i in class_mdata.direction['4'].keys():
            #~ print 'list_sta_partiaaaal', list_sta_partial
            #Linea 4(Zona Rental) - Linea 2
            if path[-1] in class_mdata.direction['2'].keys() and path[-1] != 'Silencio':
                print 'entre'
                if dict_connec.get('Teatros',) and \
                dict_connec['Teatros'].get('Capuchinos',):
                    dict_connec['Teatros'].pop('Capuchinos')
            #Linea 4(Zona Rental) - Linea 21 sin Silencio en el camino
            if path[-1] in class_mdata.direction['21'].keys() and not any('Silencio' in s for s in path):
                if dict_connec.get('Mamera',) and dict_connec['Mamera'].get('Ruiz Pineda',):
                    dict_connec['Mamera'].pop('Ruiz Pineda')
                if dict_connec.get('Teatros',) and dict_connec['Teatros'].get('Capuchinos',):
                    dict_connec['Teatros'].pop('Capuchinos')
            #Linea 4(Zona Rental) - Linea 20 con Silencio en el camino
            if path[-1] in class_mdata.direction['20'].keys() and ('Silencio' in s for s in path):
                if dict_connec.get('Mamera',) and dict_connec['Mamera'].get('Caricuao',):
                    dict_connec['Mamera'].pop('Caricuao')
            #Linea 4(Zona Rental) - Linea 20 con Silencio en el camino
            if path[-1] in class_mdata.direction['20'].keys() and not ('Silencio' in s for s in path):
                if dict_connec.get('Mamera',) and dict_connec['Mamera'].get('Caricuao',):
                    dict_connec['Mamera'].pop('Caricuao')
                if dict_connec.get('Teatros',) and dict_connec['Teatros'].get('Capuchinos',):
                    dict_connec['Teatros'].pop('Capuchinos')
            
        #Zoologico - Linea 2 / Silencio
        if sta_i in class_mdata.direction['20'].keys():
            #Zoologico - Linea 2
            if path[-1] in class_mdata.direction['2'].keys() and path[-1] != 'Silencio':
                if dict_connec.get('Mamera',) and \
                dict_connec['Mamera'].get('Antimano',):
                    dict_connec['Mamera'].pop('Antimano')
            #Zoologico - Silencio / Pasa por Silencio
            if any('Silencio' in s for s in path):
                if dict_connec.get('Capuchinos') and \
                dict_connec['Capuchinos'].get('Teatros',):
                    dict_connec['Capuchinos'].pop('Teatros')
                if dict_connec.get('Mamera',) and \
                dict_connec['Mamera'].get('Antimano',):
                    dict_connec['Mamera'].pop('Antimano')

        #Zoologico - Linea 4
        if sta_i in class_mdata.direction['20'].keys() and path[len(path)-1] in class_mdata.direction['4'].keys():
            if dict_connec.get('Capuchinos',) and \
            dict_connec['Capuchinos'].get('Teatros',):
                dict_connec['Capuchinos'].pop('Teatros')
                
        #Las Adjuntas - Linea 4
        if sta_i in class_mdata.direction['21'].keys() and path[len(path)-1] in class_mdata.direction['4'].keys():
            if dict_connec.get('Capuchinos',) and \
            dict_connec['Capuchinos'].get('Teatros',):
                dict_connec['Capuchinos'].pop('Teatros')
            if dict_connec.get('Mamera',) and \
            dict_connec['Mamera'].get('Antimano',):
                dict_connec['Mamera'].pop('Antimano')

        #Las Adjuntas - Linea 2 / Silencio
        if sta_i in class_mdata.direction['21'].keys():
            #Las Adjuntas - Linea 2
            if path[len(path)-1] in class_mdata.direction['2'].keys() and path[len(path)-1] != 'Silencio':
                if dict_connec.get('Mamera',) and \
                dict_connec['Mamera'].get('Antimano',):
                    dict_connec['Mamera'].pop('Antimano')
            #Las Adjuntas - Silencio
            if path[len(path)-1] == 'Silencio':
                if dict_connec.get('Capuchinos') and \
                dict_connec['Capuchinos'].get('Teatros',):
                    dict_connec['Capuchinos'].pop('Teatros')
            #Las Adjuntas - Linea1 con paseo por linea 4
            union = list (set(path) & set(class_mdata.direction['4'].keys()))
            inter = list(set(class_mdata.direction['4'].keys()).difference(set(union)))
            if len(inter)==1 and inter[0] == 'direction':
                if dict_connec.get('Mamera',) and \
                dict_connec['Mamera'].get('Antimano',):
                    dict_connec['Mamera'].pop('Antimano')
                if dict_connec.get('Capuchinos') and \
                dict_connec['Capuchinos'].get('Teatros',):
                    dict_connec['Capuchinos'].pop('Teatros')
        return dict_connec
        
    def get_direction(self,list_sta_partial,class_mdata):
        valor_dir,direction,ll,l=0,'',[],[]
        
        if list_sta_partial:
            #~ print 'LIST', list_sta_partial
            #Se divide list_sta_partial por listas y se toma la ultima lista para 
            #buscar la direccion, esto por que a veces list_sta_partial puede venir
            #de la siguiente forma: ['Antimano', 'Carapita', 'La Yaguara', 'La Paz', 'Artigas', 
            #~ 'Maternidad', 'Capuchinos', 'Teatros', 'Nuevo Circo'] y coloca direccion silencio 
            #~ en lugar de zona rental
            for i,j in zip(list_sta_partial,list_sta_partial[1::]):
                line = class_mdata.line[i]
                if line == class_mdata.line[j]:
                    l.append(i)
                else:
                    l.append(i)
                    ll.append(l)
                    l=[]
                if j == list_sta_partial[-1]:
                    l.append(j)
                    ll.append(l)
            #~ print 'LL', ll
            
            #Origen: Linea 4- Destino Linea 2.
            if len(ll)>1 and (list(set(ll[-1])&set(class_mdata.direction['2'].keys())) and \
                 list(set(ll[-2])&set(class_mdata.direction['4'].keys()))):
                    direction = 'Las Adjuntas'
                    return direction
            elif ll and len(ll[-1]) > 1:
                list_sta_partial = ll[-1]
            #~ if la lista tiene una sola estacion, entonces no se puede determinar la direccion
            #~ porque no hay como restar, entonces accedo al diccionario
            elif ll and len(ll[-1])==1:
                direction = class_mdata.direction2[list_sta_partial[-1]][list_sta_partial[-2]]
                return direction

            valor_dir = class_mdata.direction[class_mdata.line \
            [list_sta_partial[0]]] \
            [list_sta_partial[0]]-class_mdata.direction \
            [class_mdata.line[list_sta_partial[-1]]] \
            [list_sta_partial[-1]]

            #Si es mayor o igual que 1, la transferencia esta en la segunda posicion de la tupla
            if valor_dir >=1:
                direction = class_mdata.direction[class_mdata.line[list_sta_partial[0]]]['direction'][1]
            #Si es menor que 0, la transferencia esta en la primera posicion de la tupla
            elif valor_dir <= 0:
                direction = class_mdata.direction[class_mdata.line[list_sta_partial[0]]]['direction'][0]

            if ll and ll[0][-1] in class_mdata.direction['21'] and direction == 'Silencio':
                direction = 'Zona Rental'
        return direction

    def get_options(self,start,end):
        
        class_mdata = master_data()
        list_path = self.find_all_paths(class_mdata.graph,start,end)
        list_sta_trans,list_sta_partial= [],[]
        dict_transitory,list_direction={},[]
        print start, end
        print 'PATHS', list_path
        print ''
        print ''

        if start in class_mdata.direction['21'].keys():
            dict_del = {}
            if end =='Silencio' or end in class_mdata.direction['4'].keys():
                [dict_del.update({len(path):list_path.index(path)}) for path in list_path]
                list_path.pop(dict_del[max(dict_del.keys())])
        
        #~ list_path.pop(0)
        
        for path in list_path:
            qty_trans,dict_sta_trans,list_trans=0,{},[]
            list_path_end,list_sta_partial,l_transac = [],[],[]
            dict_connec=deepcopy(class_mdata.connec)

            if class_mdata.line[path[0]] in ['21','20']:
                line='2'
            else:
                line=class_mdata.line[path[0]]
            list_path_end.append({'text':'Aborde la estacion ' + path[0] + ' de la Linea ' + line,
                                  'stations':[]})

            for i,j in zip(path,path[1::]):
                list_sta_partial.append(i)
                not list(set([i])&set(list_sta_partial)) and list_sta_partial.append(i)
                dict_connec = self.line_2(i,class_mdata,path,dict_connec)
                list_trans, qty_trans = self.get_trans(path,class_mdata,dict_connec)
                
                if (i,j) in list_trans:
                    l_transac.append((i,j))
                    #~ print 'I %s J %s' % (i,j)
                    #~ print 'list_sta_partiallll', list_sta_partial
                    if len(list_sta_partial) > 0:
                        direction= self.get_direction(list_sta_partial,class_mdata)
                        print 'DIRECTION', direction

                        if class_mdata.line[j] in ['21','20']:
                            line='2'
                        else:
                            line=class_mdata.line[j]
                        if start==i:
                            if  class_mdata.connec3[1] in ','.join(path):
                                list_path_end.append({'text':'Realice Transferencia de la estacion '+ i + ' a la Linea ' + 
                                class_mdata.line[path[path.index(j)+1]],'stations':[]})
                            else:
                                list_path_end.append({'text':'Realicee Transferencia de la estacion '+ i + ' a la Linea ' + line + ' hasta la estacion ' + j,'stations':[]})
                        elif dict_connec[i][j]==1:
                            direction and list_path_end.append({'text':'IIngrese al tren con direccion ' + direction,'stations':[]})
                            list_path_end.append({'text':'Contiiinue ' + str(len(list_sta_partial)) + ' estaciones en esta linea hasta la estacion ' + list_sta_partial[-1] + ' ->','stations':list_sta_partial})
                            list_path_end.append({'text':'Realiice Transferencia de tren en la estacion ' + list_sta_partial[len(list_sta_partial)-1],'stations':[]})
                        elif dict_connec[i][j]==2 and class_mdata.connec3[1] in ','.join(path):
                            direction and list_path_end.append({'text':'Ingre al tren con direccion ' + direction,'stations':[]})
                            list_path_end.append({'text':'Continueee ' + str(len(list_sta_partial)) + ' estaciones en esta linea hasta la estacion ' + i + ' ->','stations':list_sta_partial})
                            list_path_end.append({'text':'RRealicee Transferencia en la estacion '+ i + ' a la Linea ' + class_mdata.line[path[path.index(j)+1]],'stations':[]})
                        elif dict_connec[i][j] in [2,3]:
                            direction and list_path_end.append({'text':'Ingressse al tren con direccion ' + direction,'stations':[]})
                            list_path_end.append({'text':'Continueee ' + str(len(list_sta_partial)) + ' estaciones en esta linea hasta la estacion ' + i + ' ->','stations':list_sta_partial})
                            list_path_end.append({'text':'Realicee Transferencia en la estacion '+ i + ' a la Linea ' + line + ' hasta la estacion ' + j,'stations':[]})
                        elif dict_connec[i][j]==4:
                            direction and list_path_end.append({'text':'Inggggrese al tren con direccion ' + direction,'stations':[]})
                            list_path_end.append({'text':'Continueee ' + str(len(list_sta_partial)) + ' estaciones en esta linea hasta la estacion ' + i + ' ->','stations':list_sta_partial})
                            list_path_end.append({'text':'RRealicee Transferencia en la estacion '+ i + ' a la Linea ' + line,'stations':[]})
                        elif dict_connec[i][j]==5:
                            direction and list_path_end.append({'text':'Inggggrese al tren con direccion ' + direction,'stations':[]})
                            list_path_end.append({'text':'Continueee ' + str(len(list_sta_partial)+1) + ' estaciones en esta linea hasta la estacion ' + j + ' ->','stations':list_sta_partial})
                            if class_mdata.connec3[2] in ','.join(path):
                                list_path_end.append({'text':'RRealicee Transferencia en la estacion '+ j + ' a la Linea ' + class_mdata.line[path[path.index(j)+1]],'stations':[]})
                            else:
                                list_path_end.append({'text':'RRealicee Transferencia en la estacion '+ j + ' a la Linea ' + line,'stations':[]})
                        elif dict_connec[i][j]==6:
                            direction and list_path_end.append({'text':'Ingrese al tren con direccion ' + direction,'stations':[]})
                            list_path_end.append({'text':'Continueee ' + str(len(list_sta_partial)+1) + ' estaciones en esta linea hasta la estacion ' + j + ' ->','stations':list_sta_partial})
                            list_path_end.append({'text':'Realice Transferencia de tren en la estacion '+ j,'stations':[]})
                    if not j==end or not list_sta_partial[-1] ==end:
                        list_sta_partial=[]
            
            if not any(j in s for s in list_sta_partial):
                list_sta_partial.append(j)
            direction = self.get_direction(list_sta_partial,class_mdata)

            #~ Para el caso en que luego de la transferencia no hay que rodar una estacion mas para 
            #~ poder llegar. Con el solo hecho de hacer la transferencia ya se llego al destino.
            #~ Ejemplo: La Hoyada - Zona Rental.
            print 'direction', direction
            #~ print ''
            #~ print 'DICT_CONNECT', dict_connec
            #~ print 'I %s J %s' % (i,j)
            
            if  ((dict_connec.get(i,) and dict_connec[i].get(j,)) == 3) or \
            ((l_transac and l_transac[-1][1]==end) and not \
            ((dict_connec.get(i,) and dict_connec[i].get(j,)) == 4)):
                pass
            else:
                direction and list_path_end.append({'text':'Innnngrese al tren con direccion ' +
                direction,'stations':[]})
                sta1=list_sta_partial[0]
                sta2=list_sta_partial[1]
                if (dict_connec.get(sta1,) and dict_connec[sta1].get(sta2,))==4 and \
                (class_mdata.connec3[1] in ','.join(path)):
                    list_sta_partial.pop(0) #Para el caso en que la transferencia es la 4 me sobra
                    #la estacion Plaza Venezuela, me da una estacion de mas.
                if len(list_sta_partial)>=1:
                    list_path_end.append({'text':'CContinue ' + str(len(list_sta_partial)) + 
                    ' estaciones en esta linea hasta la estacion ' + j + ' ->', \
                    'stations':list_sta_partial})

            list_path_end.append({'text':'Usted ha llegado a su destino','stations':[]})
            dict_sta_trans.update({'stations':len(path)})
            dict_sta_trans.update({'transfers':qty_trans})
            dict_sta_trans.update({'path':list_path_end})
            dict_transitory.update({len(path):dict_sta_trans})

        for key, value in sorted(dict_transitory.iteritems(), key=lambda (k,v): (v,k)):
            list_sta_trans.append(value)

        return list_sta_trans

    def min_path(self, graph, start, end):
        paths=self.find_all_paths(graph,start,end)
        mt=10**99
        mpath=[]
        print '\tAll paths:',paths
        for path in paths:
            t=sum(graph[i][j] for i,j in zip(path,path[1::]))
            print '\t\tevaluating:',path, t
            if t<mt: 
                mt=t
                mpath=path

        e1=' '.join('{}->{}:{}'.format(i,j,graph[i][j]) for i,j in zip(mpath,mpath[1::]))
        e2=str(sum(graph[i][j] for i,j in zip(mpath,mpath[1::])))
        print 'Best path: '+e1+'   Total: '+e2+'\n'  

train_ccs()

def main():

    class_master_data = master_data()
    class_train_ccs = train_ccs()
    
    a= class_train_ccs.get_options('Silencio','Bellas Artes')
    
    for i in a:
        print ''
        for j in i['path']:
            print j['text']
            
    #~ print class_train_ccs.get_options('Altamira','Las Adjuntas')
    #~ print class_train_ccs.transfer_qty()
    
    #~ class_train_ccs.get_list_path_decription()

    #~ class_train_ccs.recursive_dfs(class_master_data.graph,'')

if __name__ == '__main__':
    main()
