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

    def get_options(self):
        class_mdata = master_data()
        list_path = self.find_all_paths(class_mdata.graph,'Gato Negro','Teatros')
        list_sta_trans= []
        
        for path in list_path:
            qty_trans=0
            dict_sta_trans = {'stations':None,'transfers':None}
            
            for i,j in zip(path,path[1::]):
                if class_mdata.connection.get(i,) and j==class_mdata.connection[i]: #Puedo Obtener las transferencias
                    qty_trans = qty_trans + 1
                    
            dict_sta_trans.update({'stations':len(path)})
            dict_sta_trans.update({'transfers':qty_trans})
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
        
    print class_train_ccs.get_options()
    #~ print class_train_ccs.transfer_qty()


if __name__ == '__main__':
    main()
