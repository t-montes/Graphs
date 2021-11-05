"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""

from time import process_time as _process_time
import main

def timer(func):
    """Decorador que permite medir el tiempo en segundos que tarda una función.
    El parámetro opcional es el formato de impresión del tiempo (debe contener almenos un '%s')"""
    def inner(*args, **kwargs):
        t1 = _process_time()
        ret = func(*args, **kwargs)
        t2 = _process_time()
        print("La funcion '%s' tardó %f segundos."%(func.__name__, t2-t1))
        return ret
    return inner

class Graph():
    def __init__(self, nodes:list, edges:list):
        self.n = nodes
        self.e = edges
    
    """Dijkstra minimum cost algorithm"""
    @timer
    def dijkstra(self,font,kind=1):
        if kind==1:
            return self.__dijkstra1(font)
        elif kind==2:
            return self.__dijkstra2(font)
        else:
            return self.__dijkstra3(font)

    def __dijkstra1(self,font):
        ...
    
    def __dijkstra2(self,font):
        ...
    
    def __dijkstra3(self,font):
        ...
    
    """Bellman Ford minimum cost algorithm"""
    @timer
    def bellman_ford(self,font,kind=1):
        if kind==1:
            return self.__bellman_ford1(font)
        elif kind==2:
            return self.__bellman_ford2(font)
        else:
            return self.__bellman_ford3(font)

    def __bellman_ford1(self,font):
        ...
    
    def __bellman_ford2(self,font):
        ...
    
    def __bellman_ford3(self,font):
        ...
    
    """Floyd Warschall minimum cost algorithm"""
    @timer
    def floyd_warschall(self,font,kind=1):
        if kind==1:
            return self.__floyd_warschall1(font)
        elif kind==2:
            return self.__floyd_warschall2(font)
        else:
            return self.__floyd_warschall3(font)

    def __floyd_warschall1(self,font):
        ...
    
    def __floyd_warschall2(self,font):
        ...
    
    def __floyd_warschall3(self,font):
        ...
    
    """Depth First Search algorithm"""
    @timer
    def dfs(self,kind=1):
        if kind==1:
            return self.__dfs1()
        elif kind==2:
            return self.__dfs2()
        else:
            return self.__dfs3()
        
    def __dfs1(self):
        ...
        
    def __dfs2(self):
        ...
        
    def __dfs3(self):
        ...
        
    """Breadth First Search algorithm"""
    @timer
    def bfs(self,kind=1):
        if kind==1:
            return self.__bfs1()
        elif kind==2:
            return self.__bfs2()
        else:
            return self.__bfs3()
        
    def __bfs1(self):
        ...
        
    def __bfs2(self):
        ...
        
    def __bfs3(self):
        ...

@timer
def loadGraph(path:str, first='A') -> Graph:
    with open(path,'r') as file:
        lines:list = file.readlines()
    
    numbernodes:int = len(lines)

    Nodes:list = [i for i in range(first,first+numbernodes)] if (type(first) is int) else [
                chr(i) for i in range(ord(first),ord(first)+numbernodes)]
    Edges:list = []

    i:int = -1
    while (i := i+1) < len(lines):
        subline:list = [int(j) for j in lines[i].rstrip().split('\t')]
        j:int = -1
        while (j := j+1) < len(subline):
            if subline[j] > 0:
                #Tripla A -> B de costo C
                Edges.append((Nodes[i],Nodes[j],subline[j]))

    return Graph(Nodes,Edges)

if __name__ == "__main__":
    main.main()
