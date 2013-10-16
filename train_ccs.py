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

    def get_trans(self,path,cl_mdata,d_connec):

        list_tu_trans,qty_trans=[],0
        for i,j in zip(path,path[1::]):
            if d_connec.get(i,) and j in d_connec[i].keys(): 
                if (i,j)==('Capuchinos','Teatros') and ('Mamera','Antimano') in list_tu_trans:
                    pass
                elif (i,j)==('Mamera','Antimano') and ('Capuchinos', 'Teatros') in list_tu_trans:
                    pass
                elif (i,j)==('Mamera','Ruiz Pineda') and ('Teatros','Capuchinos') in list_tu_trans:
                    pass
                elif (i,j)==('Teatros','Capuchinos') and ('Mamera','Ruiz Pineda') in list_tu_trans:
                    pass
                elif (i,j)==('Plaza Venezuela','Ciudad Universitaria') and \
                (path[path.index(i)-1],'Plaza Venezuela') in list_tu_trans:
                    pass
                elif (i,j)==('Plaza Venezuela','Zona Rental') and \
                (path[path.index(i)-1],'Plaza Venezuela') in list_tu_trans:
                    pass
                elif (i,j)==('Capuchinos','Teatros') and \
                path[0] in cl_mdata.direction['2'].keys():
                    pass
                else:
                    list_tu_trans.append((i,j))
                    qty_trans = qty_trans + 1
        list_tu_trans = list(set(list_tu_trans))
        return list_tu_trans, qty_trans

    def line_2(self,sta_i,cl_mdata,path,d_connec):
        
        #~ Linea 2 -> Linea 20 / Linea 21
        if sta_i in cl_mdata.direction['2'].keys():
            #~ Linea 2 / Linea 20
            if path[-1] in cl_mdata.direction['20'].keys():
                if d_connec.get('Mamera') and d_connec['Mamera'].get('Caricuao',):
                    d_connec['Mamera'].pop('Caricuao')
            #~ Linea 2 / Linea 21
            if path[-1] in cl_mdata.direction['21'].keys():
                if d_connec.get('Mamera') and d_connec['Mamera'].get('Ruiz Pineda',):
                    d_connec['Mamera'].pop('Ruiz Pineda')
                
        #~ Silencio / Zoologico
        if sta_i == 'Silencio' and path[-1] in cl_mdata.direction['20'].keys():
            if d_connec.get('Mamera',) and d_connec['Mamera'].get('Caricuao',):
                d_connec['Mamera'].pop('Caricuao')

        #Linea 4(Zona Rental) - Linea 2 / Silencio
        if sta_i in cl_mdata.direction['4'].keys():
            #Linea 4(Zona Rental) - Linea 2
            if path[-1] in cl_mdata.direction['2'].keys() and path[-1] != 'Silencio':
                if d_connec.get('Teatros',) and d_connec['Teatros'].get('Capuchinos',):
                    d_connec['Teatros'].pop('Capuchinos')
            #Linea 4(Zona Rental) - Linea 21 sin Silencio en el camino
            if path[-1] in cl_mdata.direction['21'].keys() and \
            not any('Silencio' in s for s in path):
                if d_connec.get('Mamera',) and d_connec['Mamera'].get('Ruiz Pineda',):
                    d_connec['Mamera'].pop('Ruiz Pineda')
                if d_connec.get('Teatros',) and d_connec['Teatros'].get('Capuchinos',):
                    d_connec['Teatros'].pop('Capuchinos')
            #Linea 4(Zona Rental) - Linea 20 con Silencio en el camino
            if path[-1] in cl_mdata.direction['20'].keys() and ('Silencio' in s for s in path):
                if d_connec.get('Mamera',) and d_connec['Mamera'].get('Caricuao',):
                    d_connec['Mamera'].pop('Caricuao')
            #Linea 4(Zona Rental) - Linea 20 con Silencio en el camino
            if path[-1] in cl_mdata.direction['20'].keys() and \
            not ('Silencio' in s for s in path):
                if d_connec.get('Mamera',) and d_connec['Mamera'].get('Caricuao',):
                    d_connec['Mamera'].pop('Caricuao')
                if d_connec.get('Teatros',) and d_connec['Teatros'].get('Capuchinos',):
                    d_connec['Teatros'].pop('Capuchinos')
            
        #Zoologico - Linea 2 / Silencio
        if sta_i in cl_mdata.direction['20'].keys():
            #Zoologico - Linea 2
            if path[-1] in cl_mdata.direction['2'].keys() and path[-1] != 'Silencio':
                if d_connec.get('Mamera',) and d_connec['Mamera'].get('Antimano',):
                    d_connec['Mamera'].pop('Antimano')
            #Zoologico - Silencio / Pasa por Silencio
            if any('Silencio' in s for s in path):
                if d_connec.get('Capuchinos') and d_connec['Capuchinos'].get('Teatros',):
                    d_connec['Capuchinos'].pop('Teatros')
                if d_connec.get('Mamera',) and d_connec['Mamera'].get('Antimano',):
                    d_connec['Mamera'].pop('Antimano')

        #Zoologico - Linea 4
        if sta_i in cl_mdata.direction['20'].keys() and \
        path[len(path)-1] in cl_mdata.direction['4'].keys():
            if d_connec.get('Capuchinos',) and d_connec['Capuchinos'].get('Teatros',):
                d_connec['Capuchinos'].pop('Teatros')
                
        #Las Adjuntas - Linea 4
        if sta_i in cl_mdata.direction['21'].keys() and \
        path[len(path)-1] in cl_mdata.direction['4'].keys():
            if d_connec.get('Capuchinos',) and d_connec['Capuchinos'].get('Teatros',):
                d_connec['Capuchinos'].pop('Teatros')
            if d_connec.get('Mamera',) and d_connec['Mamera'].get('Antimano',):
                d_connec['Mamera'].pop('Antimano')

        #Las Adjuntas - Linea 2 / Silencio
        if sta_i in cl_mdata.direction['21'].keys():
            #Las Adjuntas - Linea 2
            if path[len(path)-1] in cl_mdata.direction['2'].keys() and \
            path[len(path)-1] != 'Silencio':
                if d_connec.get('Mamera',) and d_connec['Mamera'].get('Antimano',):
                    d_connec['Mamera'].pop('Antimano')
            #Las Adjuntas - Silencio
            if path[len(path)-1] == 'Silencio':
                if d_connec.get('Capuchinos') and d_connec['Capuchinos'].get('Teatros',):
                    d_connec['Capuchinos'].pop('Teatros')
            #Las Adjuntas - Linea1 con paseo por linea 4
            union = list (set(path) & set(cl_mdata.direction['4'].keys()))
            inter = list(set(cl_mdata.direction['4'].keys()).difference(set(union)))
            if len(inter)==1 and inter[0] == 'direction':
                if d_connec.get('Mamera',) and d_connec['Mamera'].get('Antimano',):
                    d_connec['Mamera'].pop('Antimano')
                if d_connec.get('Capuchinos') and d_connec['Capuchinos'].get('Teatros',):
                    d_connec['Capuchinos'].pop('Teatros')
        return d_connec
        
    def get_direction(self,l_sta_part,cl_mdata):
        valor_dir,direction,ll,l=0,'',[],[]
        
        #~ print 'LIST', l_sta_part
        #Se divide l_sta_part por listas y se toma la ultima lista para 
        #buscar la direccion, esto por que a veces l_sta_part puede venir
        #de la siguiente forma: ['Antimano', 'Carapita', 'La Yaguara', 'La Paz', 'Artigas', 
        #~ 'Maternidad', 'Capuchinos', 'Teatros', 'Nuevo Circo'] y coloca direccion silencio 
        #~ en lugar de zona rental
        for i,j in zip(l_sta_part,l_sta_part[1::]):
            line = cl_mdata.line[i]
            if line == cl_mdata.line[j]:
                l.append(i)
            else:
                l.append(i)
                ll.append(l)
                l=[]
            if j == l_sta_part[-1]:
                l.append(j)
                ll.append(l)
        #~ print 'LL', ll
            
        if len(ll)>1 and (list(set(ll[-1])&set(cl_mdata.direction['2'].keys())) and \
        #Origen: Linea 4- Destino Linea 2.
             list(set(ll[-2])&set(cl_mdata.direction['4'].keys()))):
                direction = 'Las Adjuntas'
                return direction
        elif ll and len(ll[-1]) > 1:
            l_sta_part = ll[-1]
        elif ll and len(ll[-1])==1:
        #~ if la lista tiene una sola estacion, entonces no se puede determinar la direccion
        #~ porque no hay como restar, entonces accedo al diccionario
            direction = cl_mdata.direction2[l_sta_part[-1]][l_sta_part[-2]]
            return direction

        valor_dir = cl_mdata.direction[cl_mdata.line[l_sta_part[0]]] \
        [l_sta_part[0]]- \
        cl_mdata.direction[cl_mdata.line[l_sta_part[-1]]][l_sta_part[-1]]

        #Si es mayor o igual que 1, la transferencia esta en la segunda posicion de la tupla
        if valor_dir >=1:
            direction = cl_mdata.direction[cl_mdata.line[l_sta_part[0]]]['direction'][1]
        #Si es menor que 0, la transferencia esta en la primera posicion de la tupla
        elif valor_dir <= 0:
            direction = cl_mdata.direction[cl_mdata.line[l_sta_part[0]]]['direction'][0]

        if ll and ll[0][-1] in cl_mdata.direction['21'] and direction == 'Silencio':
            direction = 'Zona Rental'
        return direction

    def get_options(self,start,end):
        
        cl_mdata,l_sta_trans,l_sta_part = master_data(),[],[]
        l_path = self.find_all_paths(cl_mdata.graph,start,end)
        print start, end
        print 'PATHS', l_path
        print ''
        print ''

        if start in cl_mdata.direction['21'].keys():
            d_del = {}
            if end =='Silencio' or end in cl_mdata.direction['4'].keys():
                [d_del.update({len(path):l_path.index(path)}) for path in l_path]
                l_path.pop(d_del[max(d_del.keys())])
        
        #~ l_path.pop(0)
        
        for path in l_path:
            qty_trans,d_sta_trans,l_trans=0,{},[]
            l_path_end,l_sta_part = [],[]
            d_connec=deepcopy(cl_mdata.connec)

            if cl_mdata.line[path[0]] in ['21','20']:
                line='2'
            else:
                line=cl_mdata.line[path[0]]
            
            l_path_end.append({'text':'Aborde la estacion ' + path[0] + ' de la Linea ' + line,
                                  'stations':[]})

            for i,j in zip(path,path[1::]):
                l_sta_part.append(i)
                d_connec = self.line_2(i,cl_mdata,path,d_connec)
                l_trans, qty_trans = self.get_trans(path,cl_mdata,d_connec)
                
                if (i,j) in l_trans and len(l_sta_part) > 0:
                    
                    direction= self.get_direction(l_sta_part,cl_mdata)
                    print 'DIRECTION', direction

                    if cl_mdata.line[j] in ['21','20']:
                        line='2'
                    else:
                        line=cl_mdata.line[j]
                    
                    if start==i:
                        if  cl_mdata.connec3[1] in ','.join(path):
                            l_path_end.append({'text':'Realice Transferencia de la estacion '+ i + 
                            ' a la Linea ' + cl_mdata.line[path[path.index(j)+1]],'stations':[]})
                        else:
                            l_path_end.append({'text':'Realice Transferencia de la estacion '+ i + 
                            ' a la Linea ' + line + ' hasta la estacion ' + j,'stations':[]})
                    elif d_connec[i][j]==1:
                        direction and l_path_end.append({'text':'IIngrese al tren con direccion ' + 
                        direction,'stations':[]})
                        l_path_end.append({'text':'Contiiinue ' + str(len(l_sta_part)) + 
                        ' estaciones en esta linea hasta la estacion ' + l_sta_part[-1] + 
                        ' ->','stations':l_sta_part})
                        l_path_end.append({'text':'Realice Transferencia de tren en la estacion ' + 
                        l_sta_part[len(l_sta_part)-1],'stations':[]})
                    elif d_connec[i][j]==2 and cl_mdata.connec3[1] in ','.join(path):
                        direction and l_path_end.append({'text':'Ingre al tren con direccion ' + 
                        direction,'stations':[]})
                        l_path_end.append({'text':'Continueee ' + str(len(l_sta_part)) + 
                        ' estaciones en esta linea hasta la estacion ' + i + 
                        ' ->','stations':l_sta_part})
                        l_path_end.append({'text':'RRealicee Transferencia en la estacion '+ i + 
                        ' a la Linea ' + cl_mdata.line[path[path.index(j)+1]],'stations':[]})
                    elif d_connec[i][j] in [2,3]:
                        direction and l_path_end.append({'text':'Ingressse al tren con direccion '
                         + direction,'stations':[]})
                        l_path_end.append({'text':'Continueee ' + str(len(l_sta_part)) + 
                        ' estaciones en esta linea hasta la estacion ' + i +
                        ' ->','stations':l_sta_part})
                        l_path_end.append({'text':'Realicee Transferencia en la estacion '+ i + 
                        ' a la Linea ' + line + ' hasta la estacion ' + j,'stations':[]})
                    elif d_connec[i][j]==4:
                        direction and l_path_end.append({'text':'Ingrese al tren con direccion ' + 
                        direction,'stations':[]})
                        l_path_end.append({'text':'Continueee ' + str(len(l_sta_part)) + 
                        ' estaciones en esta linea hasta la estacion ' + i +
                        ' ->','stations':l_sta_part})
                        l_path_end.append({'text':'RRealicee Transferencia en la estacion '+ i +
                         ' a la Linea ' + line,'stations':[]})
                    elif d_connec[i][j]==5:
                        direction and l_path_end.append({'text':'Ingrese al tren con direccion ' + 
                        direction,'stations':[]})
                        l_path_end.append({'text':'Continueee ' + str(len(l_sta_part)+1) + 
                        ' estaciones en esta linea hasta la estacion ' + j +
                         ' ->','stations':l_sta_part})
                        if cl_mdata.connec3[2] in ','.join(path):
                            l_path_end.append({'text':'Realicee Transferencia en la estacion '+ j + 
                            ' a la Linea ' + cl_mdata.line[path[path.index(j)+1]],'stations':[]})
                        else:
                            l_path_end.append({'text':'Realicee Transferencia en la estacion '+ j + 
                            ' a la Linea ' + line,'stations':[]})
                    elif d_connec[i][j]==6:
                        direction and l_path_end.append({'text':'Ingrese al tren con direccion ' + 
                        direction,'stations':[]})
                        l_path_end.append({'text':'Continueee ' + str(len(l_sta_part)+1) + 
                        ' estaciones en esta linea hasta la estacion ' + j + 
                        ' ->','stations':l_sta_part})
                        l_path_end.append({'text':'Realice Transferencia de tren en la estacion '+
                         j,'stations':[]})
                    l_sta_part=[]
                if j==end or (l_sta_part and l_sta_part[-1] ==end):
                    l_sta_part=[]
            
            #~ print 'I %s J %s' % (i,j)

            [l_sta_part.append(i) for i,j in zip(path,path[1::]) if qty_trans==0]   
                
            if not any(j in s for s in l_sta_part):
                l_sta_part.append(j)
            

            if  (d_connec.get(i,) and d_connec[i].get(j,)) and d_connec[i][j] == 3 or \
            ((l_trans and l_trans[-1][1]==end) and \
             d_connec[i][j]!=4 and d_connec[i][j]!=1):
                #3: Para el caso en que luego de la transferencia no hay que rodar una estacion mas 
                #para Llegar.Con solo hacer la transferencia ya se llego al destino.
                #Si es de tipo 1 o 4 no debe entrar aqui porque necesito que continue las
                #estaciones que hace falta. TEST 44.
                pass
            else:
                if len(l_sta_part)>1:
                    sta1=l_sta_part[0]
                    sta2=l_sta_part[1]
                    if (d_connec.get(sta1,) and d_connec[sta1].get(sta2,))==4 and \
                    (cl_mdata.connec3[1] in ','.join(path)):
                        l_sta_part.pop(0) 
                        #Para el caso en que la transferencia es la 4 me sobra
                        #la estacion Plaza Venezuela, me da una estacion de mas.
                if len(l_sta_part)>=1:
                    
                    direction = self.get_direction(l_sta_part,cl_mdata)
                    print 'direction', direction
                    direction and l_path_end.append({'text':'Innnngrese al tren con direccion ' +
                    direction,'stations':[]})
                    l_path_end.append({'text':'CContinue ' + str(len(l_sta_part)) + 
                    ' estaciones en esta linea hasta la estacion ' + j + ' ->', \
                    'stations':l_sta_part})
            
            l_path_end.append({'text':'Usted ha llegado a su destino','stations':[]})
            d_sta_trans.update({'stations':len(path)})
            d_sta_trans.update({'transfers':qty_trans})
            d_sta_trans.update({'path':l_path_end})
            l_sta_trans.append(d_sta_trans)
        return l_sta_trans

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
    
    a= class_train_ccs.get_options('Carapita','Teatros')
    
    for i in a:
        print ''
        for j in i['path']:
            print j['text']
            
if __name__ == '__main__':
    main()
