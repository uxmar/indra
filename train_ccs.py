


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

    def get_trans(self,list_path,class_mdata,dict_connec):
        list_tu_trans=[]
        qty_trans=0
        
        for path in list_path:
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
                    else:
                        list_tu_trans.append((i,j))
                        qty_trans = qty_trans + 1
                    
        return list_tu_trans, qty_trans

    def line_2(self,list_sta_partial,class_mdata,path,dict_connec):
        
        flag=False
        
        #Zona Rental - Las Adjuntas / Zona Rental - Zoologico
        if list_sta_partial[0] in class_mdata.direction['4'].keys() and \
        path[len(path)-1] in class_mdata.direction['99'].keys():
            if dict_connec.get('Teatros',) and \
            dict_connec['Teatros'].get('Capuchinos',):
                dict_connec['Teatros'].pop('Capuchinos')
            if dict_connec.get('Mamera',) and \
            dict_connec['Mamera'].get('Ruiz Pineda',):
                dict_connec['Mamera'].pop('Ruiz Pineda')
        
        #Silencio - Las Adjuntas / Silencio - Zoologico
        if list_sta_partial[0] in class_mdata.direction['2'].keys() and \
        path[len(path)-1] in class_mdata.direction['99'].keys():
            if dict_connec.get('Mamera',) and \
            dict_connec['Mamera'].get('Caricuao',):
                dict_connec['Mamera'].pop('Caricuao')
        
        #Zoologico - Zona Rental
        if list_sta_partial[0] in class_mdata.direction['20'].keys() and \
        path[len(path)-1] in class_mdata.direction['4'].keys():
            if dict_connec.get('Capuchinos',) and \
            dict_connec['Capuchinos'].get('Teatros',):
                dict_connec['Capuchinos'].pop('Teatros')
            if dict_connec.get('Ruiz Pineda',) and \
            dict_connec['Ruiz Pineda'].get('Mamera',):
                dict_connec['Ruiz Pineda'].pop('Mamera')
                p
        #Las Adjuntas - Zona Rental
        #~ print 'list_sta_partial',list_sta_partial
        if list_sta_partial[0] in class_mdata.direction['21'].keys():
            for i in path:
                if i in class_mdata.direction['4'].keys():
                    flag=True 
                if flag:
                    if dict_connec.get('Capuchinos',) and \
                    dict_connec['Capuchinos'].get('Teatros',):
                        dict_connec['Capuchinos'].pop('Teatros')
                    if dict_connec.get('Mamera',) and \
                    dict_connec['Mamera'].get('Antimano',):
                        dict_connec['Mamera'].pop('Antimano')
            
        
        #Zoologico - Silencio
        if list_sta_partial[0] in class_mdata.direction['20'].keys() and \
        path[len(path)-1] in class_mdata.direction['2'].keys():
            if dict_connec.get('Caricuao',) and \
            dict_connec['Caricuao'].get('Mamera',):
                dict_connec['Caricuao'].pop('Mamera')
        
        #Las Adjuntas - Silencio
        if list_sta_partial[0] in class_mdata.direction['21'].keys() and \
        path[len(path)-1] in class_mdata.direction['2'].keys():
            if dict_connec.get('Mamera',) and \
            dict_connec['Mamera'].get('Antimano',):
                dict_connec['Mamera'].pop('Antimano')
        return dict_connec
        
    def get_direction(self,list_sta_partial,class_mdata):
        
        valor_dir=0
        direction=''
        pos_stab=0
        #~ if len(list_sta_partial) >=2:
            #~ pos_stab=len(list_sta_partial)-2
        #~ else:
        
        if list_sta_partial:
        
            pos_stab=len(list_sta_partial)-2

            #~ print 'list_sta_partial',list_sta_partial
            #~ print 'VALOR 1->', class_mdata.direction[class_mdata.line \
            #~ [list_sta_partial[0]]] \
            #~ [list_sta_partial[0]]
            #~ print 'Estaciones', class_mdata.direction[class_mdata.line \
            #~ [list_sta_partial[0]]]
            #~ 
            #~ print ''
            #~ 
            #~ print 'VALOR 2->',class_mdata.direction \
            #~ [class_mdata.line[list_sta_partial[pos_stab]]] \
            #~ [list_sta_partial[pos_stab]]
            #~ print 'Estaciones', class_mdata.direction \
            #~ [class_mdata.line[list_sta_partial[pos_stab]]]
            

            valor_dir = class_mdata.direction[class_mdata.line \
            [list_sta_partial[0]]] \
            [list_sta_partial[0]]-class_mdata.direction \
            [class_mdata.line[list_sta_partial[pos_stab]]] \
            [list_sta_partial[pos_stab]]

            #~ print ''
            
            #Si es mayor o igual que 1, la transferencia esta en la segunda posicion de la tupla
            if valor_dir >=1:
                direction = class_mdata.direction[class_mdata.line[list_sta_partial[0]]]['direction'][1]
            #Si es menor que 0, la transferencia esta en la primera posicion de la tupla
            elif valor_dir < 0:
                direction = class_mdata.direction[class_mdata.line[list_sta_partial[0]]]['direction'][0]
        
        return direction, pos_stab

    def get_options(self,start,end):
        
        class_mdata = master_data()
        list_path = self.find_all_paths(class_mdata.graph,start,end)
        list_sta_trans,list_sta_partial,llist_sta_partial= [],[],[]
        dict_transitory={}

        print start, end
        print 'PATHS', list_path
        print ''
        print ''
        
        for path in list_path:
            qty_trans,dict_sta_trans=0,{}
            list_path_end,list_sta_partial = [],[]
            dict_connec=deepcopy(class_mdata.connec)

            line='2'
            if not class_mdata.line[path[0]] in ['21','20']:
                line=class_mdata.line[path[0]]
            list_path_end.append({'text':'Aborde la estacion ' + path[0] + ' de la Linea ' + line,
                                  'stations':[]})

            for i,j in zip(path,path[1::]):
                list_sta_partial.append(i)
                dict_connec = self.line_2(list_sta_partial,class_mdata,path,dict_connec)
                list_trans, qty_trans = self.get_trans(list_path,class_mdata,dict_connec)
                
                if (i,j) in list_trans:
                    
                    direction, pos_stab = self.get_direction(list_sta_partial,class_mdata)
                    line='2'
                    if not class_mdata.line[j] in ['21','20']:
                        line=class_mdata.line[j]
                    direction and list_path_end.append({'text':'Ingrese al tren con direccion ' + direction,
                                                        'stations':[]})
                    if dict_connec[i][j]:
                        if str(len(list_sta_partial)) > 1:
                            list_path_end.append({'text':'Continue ' + str(len(list_sta_partial)) + ' estaciones en esta linea hasta la estacion ' + list_sta_partial[len(list_sta_partial)-1] + ' ->',
                                                  'stations':list_sta_partial})
                        list_path_end.append({'text':'Realice Transferencia de tren en la estacion ' + list_sta_partial[len(list_sta_partial)-1],
                                              'stations':[]})
                    else:
                        if len(list_sta_partial) > 1:
                            list_path_end.append({'text':'Continue ' + str(len(list_sta_partial)) + ' estaciones en esta linea hasta la estacion ' + i + ' ->',
                                                  'stations':list_sta_partial})
                        list_path_end.append({'text':'Realice Transferencia en la estacion '+ i + ' a la Linea ' + line + ' hasta la estacion ' + j,
                                              'stations':[]})

                    llist_sta_partial.append(list_sta_partial)
                    list_sta_partial=[]
            
            direction, pos_stab = self.get_direction(list_sta_partial,class_mdata)
            
            direction and list_path_end.append({'text':'Ingrese al tren con direccion ' + direction,
                                                'stations':[]})
            llist_sta_partial.append(list_sta_partial)
            if len(list_sta_partial)>1:
                list_path_end.append({'text':'Continue ' + str(len(list_sta_partial)) + ' estaciones en esta linea hasta la estacion ' + j + ' ->',
                                      'stations':list_sta_partial})
            list_path_end.append({'text':'Usted ha llegado a su destino',
                                  'stations':[]})

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
    
    print class_train_ccs.get_options('Agua Salud','Teatros')
    #~ print class_train_ccs.get_options('Altamira','Las Adjuntas')
    #~ print class_train_ccs.transfer_qty()
    
    #~ class_train_ccs.get_list_path_decription()

    #~ class_train_ccs.recursive_dfs(class_master_data.graph,'')

if __name__ == '__main__':
    main()
