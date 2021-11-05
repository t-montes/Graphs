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
    def __init__(self, nodes:list, edges:list, adjMatrex: list):
        self.n = nodes
        self.e = edges
        self.m = adjMatrex
    
    """Dijkstra minimum cost algorithm"""
    @timer
    def dijkstra(self,font):
        ...
    
    def all_dijkstra(self):
        mins:list = []
        for i in self.v:
            mins.append(self.dijkstra(i))
        return mins
    
    """Bellman Ford minimum cost algorithm"""
    @timer
    def bellman_ford(self,font):
        ...
        
    def all_bellman_ford(self):
        mins:list = []
        for i in self.v:
            mins.append(self.bellman_ford(i))
        return mins
    
    """Floyd Warschall minimum cost algorithm"""
    @timer
    def floyd_warschall(self,font):
        ...
    
    def all_floyd_warschall(self):
        mins:list = []
        for i in self.v:
            mins.append(self.floyd_warschall(i))
        return mins
    
    """Depth First Search algorithm"""
    @timer
    def dfs(self,kind=1):
        ...
        
    """Breadth First Search algorithm"""
    @timer
    def bfs(self,kind=1):
        ...

@timer
def loadGraph(path:str, first='A') -> Graph:
    with open(path,'r') as file:
        lines:list = file.readlines()
    
    numbernodes:int = len(lines)

    Vertex:list = [i for i in range(first,first+numbernodes)] if (type(first) is int) else [
                chr(i) for i in range(ord(first),ord(first)+numbernodes)]
    Edges:list = []

    Matrix: list = []

    i:int = -1
    while (i := i+1) < len(lines):
        subline:list = [int(j) for j in lines[i].rstrip().split('\t')]
        Matrix.append(subline)
        j:int = -1
        while (j := j+1) < len(subline):
            if subline[j] > 0:
                #Tripla A -> B de costo C
                Edges.append((Vertex[i],Vertex[j],subline[j]))
    return Graph(Vertex,Edges, Matrix)

if __name__ == "__main__":
    main.main()
