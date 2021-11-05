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
        costs:list = [float("Inf")]*len(self.n)
        matrix:list = self.m

        costs[font] = 0

        for i in range(len(self.n)-1):
            for edge in self.e:
                costs[edge[1]] = min(costs[edge[1]],costs[edge[0]]+edge[2])
        return costs


    @timer  
    def all_bellman_ford(self):
        mins:list = []
        for i in self.n:
            mins.append(self.bellman_ford(i))
        return mins
    
    """Floyd Warschall minimum cost algorithm"""
    @timer
    def floyd_warschall(self):
        n = len(self.n)
        m = [[[0 for x in range(n)] for y in range(n)]for k in range(n+1)]
        k = 0
        
        while k <= n:
            i = 0
            while (i < n):
                j = 0
                while j<n:
                    if k == 0:
                        if self.m[i][j] == -1:
                            m[k][i][j] = float("Inf")
                        else:
                            m[k][i][j] = self.m[i][j]
                    else:
                        m[k][i][j] = min(m[k-1][i][j],m[k-1][i][k-1]+m[k-1][k-1][j])
                    j+=1
                i+=1
            k+=1
        
        return m[n]
    
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
