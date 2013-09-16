from stations import master_data

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

    def get_trans(self,list_path,class_mdata):
        list_tu_trans=[]
        qty_trans=0
        
        for path in list_path:
            for i,j in zip(path,path[1::]):
                if class_mdata.connec.get(i,) and j in class_mdata.connec[i].keys(): 
                    list_tu_trans.append((i,j))
                    qty_trans = qty_trans + 1
        
        return list_tu_trans, qty_trans

    def line_2(self,list_sta_partial,class_mdata,path):
        
        dict_connec = class_mdata.connec
        
        #Zona Rental - Las Adjuntas / Zona Rental - Zoologico
        if list_sta_partial[0] in class_mdata.direction['4'].keys() and \
        path[len(path)-1] in class_mdata.direction['99'].keys():
            if class_mdata.connec.get('Teatros',) and \
            class_mdata.connec['Teatros'].get('Capuchinos',):
                class_mdata.connec['Teatros'].pop('Capuchinos')
            if class_mdata.connec.get('Mamera',) and \
            class_mdata.connec['Mamera'].get('Ruiz Pineda',):
                class_mdata.connec['Mamera'].pop('Ruiz Pineda')
        
        #Silencio - Las Adjuntas / Silencio - Zoologico
        if list_sta_partial[0] in class_mdata.direction['2'].keys() and \
        path[len(path)-1] in class_mdata.direction['99'].keys():
            if class_mdata.connec.get('Mamera',) and \
            class_mdata.connec['Mamera'].get('Caricuao',):
                class_mdata.connec['Mamera'].pop('Caricuao')
        
        #Zoologico - Zona Rental
        if list_sta_partial[0] in class_mdata.direction['20'].keys() and \
        path[len(path)-1] in class_mdata.direction['4'].keys():
            if class_mdata.connec.get('Capuchinos',) and \
            class_mdata.connec['Capuchinos'].get('Teatros',):
                class_mdata.connec['Capuchinos'].pop('Teatros')
            if class_mdata.connec.get('Ruiz Pineda',) and \
            class_mdata.connec['Ruiz Pineda'].get('Mamera',):
                class_mdata.connec['Ruiz Pineda'].pop('Mamera')
                
        #Las Adjuntas - Zona Rental
        if list_sta_partial[0] in class_mdata.direction['21'].keys() and \
        path[len(path)-1] in class_mdata.direction['4'].keys():
            if class_mdata.connec.get('Capuchinos',) and \
            class_mdata.connec['Capuchinos'].get('Teatros',):
                class_mdata.connec['Capuchinos'].pop('Teatros')
            if class_mdata.connec.get('Ruiz Pineda',) and \
            class_mdata.connec['Ruiz Pineda'].get('Mamera',):
                class_mdata.connec['Ruiz Pineda'].pop('Mamera')
        
        #Zoologico - Silencio
        if list_sta_partial[0] in class_mdata.direction['20'].keys() and \
        path[len(path)-1] in class_mdata.direction['2'].keys():
            if class_mdata.connec.get('Caricuao',) and \
            class_mdata.connec['Caricuao'].get('Mamera',):
                class_mdata.connec['Caricuao'].pop('Mamera')
        
        #Las Adjuntas - Silencio
        if list_sta_partial[0] in class_mdata.direction['21'].keys() and \
        path[len(path)-1] in class_mdata.direction['2'].keys():
            if class_mdata.connec.get('Caricuao',) and \
            class_mdata.connec['Caricuao'].get('Mamera',):
                class_mdata.connec['Caricuao'].pop('Mamera')

    def get_direction(self,list_sta_partial,class_mdata):
        
        valor_dir=0
        direction=''
        
        pos_stab=len(list_sta_partial)-1
        valor_dir = class_mdata.direction[class_mdata.line \
        [list_sta_partial[0]]] \
        [list_sta_partial[0]]-class_mdata.direction \
        [class_mdata.line[list_sta_partial[pos_stab]]] \
        [list_sta_partial[pos_stab]]
    
        if valor_dir >=1:
            direction = class_mdata.direction[class_mdata.line[list_sta_partial[0]]]['direction'][1]
        elif valor_dir < 0:
            direction = class_mdata.direction[class_mdata.line[list_sta_partial[0]]]['direction'][0]
            
        return direction, pos_stab

    def get_options(self,start,end):
        class_mdata = master_data()
        list_path = self.find_all_paths(class_mdata.graph,start,end)
        list_sta_trans= []
        list_sta_partial=[]
        llist_sta_partial=[]

        print start, end

        print 'PATHS', list_path

        print ''
        print ''

        for path in list_path:
            qty_trans=0
            dict_sta_trans = {}
            list_path_end = []
            list_sta_partial=[]
            
            if class_mdata.line[path[0]] in ['21','20']:
                line='2'
            else:
                line=class_mdata.line[path[0]]
            
            list_path_end.append('Aborde la estacion ' + path[0] + ' de la Linea ' + line)
            
            for i,j in zip(path,path[1::]):
                list_sta_partial.append(i)
                #~ if class_mdata.connection.get(i,) and j==class_mdata.connection[i]: 
                    #~ qty_trans = qty_trans + 1  #se puede retornar de la funcion get_trans

                self.line_2(list_sta_partial,class_mdata,path)
                list_trans, qty_trans = self.get_trans(list_path,class_mdata)
                
                if (i,j) in list_trans:
                    
                    direction, pos_stab = self.get_direction(list_sta_partial,class_mdata)
                    
                    print 'Desde', list_sta_partial[0]
                    print 'Hasta', list_sta_partial[pos_stab]
                    print 'valor_dir',valor_dir
                    
                    if class_mdata.line[j] in ['21','20']:
                        line='2'
                    else:
                        line=class_mdata.line[j]
                        
                    list_path_end.append('Ingrese al tren con direccion ' + direction)
                    print 'list_sta_partial', list_sta_partial

                    if class_mdata.connec[i][j]:
                        list_path_end.append('Continue ' + str(len(list_sta_partial)) + ' estaciones en esta linea hasta la estacion ' + list_sta_partial[pos_stab])
                        list_path_end.append('Realice Transferencia de tren en la estacion ' + list_sta_partial[pos_stab])
                    else:
                        list_path_end.append('Continue ' + str(len(list_sta_partial)) + ' estacionesss en esta linea hasta la estacion ' + i)
                        list_path_end.append('Realice Transferencia en la estacion '+ i + ' a la Linea ' + line + ' hasta la estacion ' + j)

                    llist_sta_partial.append(list_sta_partial)
                    list_sta_partial=[]

            list_sta_partial.append(j)
            direction, pos_stab = self.get_direction(list_sta_partial,class_mdata)
            
            list_path_end.append('Ingrese al tren con direccion ' + direction)
            llist_sta_partial.append(list_sta_partial)
            list_path_end.append('Continue ' + str(len(list_sta_partial)+1) + ' estaciones en esta linea hasta la estacion ' + j)
            list_path_end.append('Usted ha llegado a su destino')

            dict_sta_trans.update({'stations':len(path)})
            dict_sta_trans.update({'transfers':qty_trans})
            dict_sta_trans.update({'path':list_path_end})
            list_sta_trans.append(dict_sta_trans)
        
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
    
    print class_train_ccs.get_options('Sabana Grande','Zoologico')
    #~ print class_train_ccs.transfer_qty()
    
    #~ class_train_ccs.get_list_path_decription()

    #~ class_train_ccs.recursive_dfs(class_master_data.graph,'')

if __name__ == '__main__':
    main()
