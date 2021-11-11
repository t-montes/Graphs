"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""

import queue
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
    def __init__(self, vertices:list, edges:dict, adjMatrix: list):
        self.v = vertices
        self.e = edges
        self.m = adjMatrix
    
    def minimum_cost(self,algorithm="dijkstra"):
        if algorithm == "dijkstra":
            return self.all_dijkstra()
        elif algorithm == "bellman_ford":
            return self.all_bellman_ford()
        elif algorithm == "floyd_warschall2":
            return self.floyd_warschall2()
        else:
            return self.floyd_warschall()
    
    def dijkstra(self,font):
        """Dijkstra minimum cost algorithm"""
        vset:set = set(self.v)
        costs:list = []
        m:set = {font}
        for i in self.v:
            costs.append(0 if (i == font) else self.e.get((font,self.v[i]),float("inf")))
        while m != vset:
            w:int = min(vset.difference(m), key = lambda e: costs[e])
            m.add(w)
            for v in vset.difference(m):
                costs[v] = min(costs[v], costs[w]+self.e.get((w,v),float("inf")))
        return costs
    
    @timer
    def all_dijkstra(self):
        mins:list = []
        for i in self.v:
            mins.append(self.dijkstra(i))
        return mins
    
    def bellman_ford(self,font):
        """Bellman Ford minimum cost algorithm"""
        costs:list = [float("inf")]*len(self.v)
        costs[font] = 0

        for i in range(len(self.v)-1):
            for edge in self.e:
                costs[edge[1]] = min(costs[edge[1]], costs[edge[0]]+self.e[edge])
        return costs

    @timer
    def all_bellman_ford(self):
        mins:list = []
        for i in self.v:
            mins.append(self.bellman_ford(i))
        return mins
    
    @timer
    def floyd_warschall(self):
        """Floyd Warschall minimum cost algorithm"""
        n:int = len(self.v)
        m:list = [[[0 for x in range(n)] for y in range(n)]for k in range(n+1)]

        k:int = 0
        while k <= n:
            i:int = 0
            while (i < n):
                j:int = 0
                while j<n:
                    if k == 0:
                        if self.m[i][j] == -1:
                            m[k][i][j] = float("inf")
                        else:
                            m[k][i][j] = self.m[i][j]
                    else:
                        m[k][i][j] = min(m[k-1][i][j],m[k-1][i][k-1]+m[k-1][k-1][j])
                    j+=1
                i+=1
            k+=1
        
        return m[n]
    
    def floyd_warschall2(self):
        n = len(self.v)
        m = [[0 for x in range(n)] for y in range(n)]
        k = 0
        while k <= n:
            i = 0
            while i < n:
                j= 0
                while j < n:
                    if k == 0:
                        if self.m[i][j] == -1:
                            m[i][j] = float("inf")
                        else:
                            m[i][j] = self.m[i][j]
                    elif k > 0 and i != k and j != k:
                        m[i][j] = min(m[i][j],m[i][k-1]+m[k-1][j])
                    j+=1
                i+=1
            k+=1
        return m

    @timer
    def dfs(self):
        """Depth First Search algorithm"""
        """Returns a duo with:
        1. A boolean: True if the Graph contains cycle(s)
        2. Any cycle of the Graph if (1) is True; 
           A topology order of the Graph if (1) is False
        """
        ...

    @timer
    def bfs(self):
        """Breadth First Search algorithm"""
        """Precondition: Graph is acyclic and Graph is undirected"""
        answer:list = []
        connectedComponents:list = []
        q:queue.Queue = queue.Queue()
        visited = [False]*len(self.v)
        while len(answer) < len(self.v):
            font = getFirstNotVisited(visited)
            q.enqueue(font)
            visited[font] = True
            component = []
            while not (q.isEmpty()):
                next = q.dequeue()
                answer.append(next)
                component.append(next)
                for v in self.v:
                    if (self.m[next][v]>0 and not visited[v]):
                        q.enqueue(v)
                        visited[v] = True
            connectedComponents.append(component)
        return connectedComponents
    
    def __repr__(self):
        rp:str = f"\n{'*'*20}GRAPH{'*'*20}\n"
        rp += "Vertices:\n"
        for i in self.v:
            rp += f"\t{chr(8226)} {i}\n"
        rp += "Edges:\n"
        for i in self.e:
            rp += f"\t{chr(8226)} {i[0]} -> {i[1]} (cost = {self.e[i]})\n"
        return rp

def getFirstNotVisited(v: list):
    i = 0
    while v[i]:
        i+=1
    return i

@timer
def loadGraph(path:str) -> Graph:
    with open(path,'r') as file:
        lines:list = file.readlines()

    if lines[len(lines)-1] == '\n':
        lines = lines[:-1]
    numbervertices:int = len(lines)

    Vertices:list = [i for i in range(numbervertices)]
    Edges:dict = {}
    Matrix: list = []

    i:int = -1
    while (i := i+1) < len(lines):
        subline:list = []
        for j in lines[i].rstrip().split('\t'):
            try:
                subline.append(int(j))
            except ValueError as e:
                print(f"Invalid line {i}: {e.args[0]}")
                subline.append(0)
        if len(subline) > numbervertices : 
            print(f"Invalid line {i}: contains {len(subline)} vertices; should be {numbervertices}.")
            subline = subline[:numbervertices]
        elif len(subline) < numbervertices :
            print(f"Invalid line {i}: contains {len(subline)} vertices; should be {numbervertices}")
            subline = subline + [0]*(numbervertices - len(subline))
        Matrix.append(subline)
        j:int = -1
        while (j := j+1) < len(subline):
            if subline[j] > 0:
                #{(A -> B) : Costo C}
                Edges[Vertices[i],Vertices[j]] = subline[j]
    
    return Graph(Vertices,Edges,Matrix)

if __name__ == "__main__":
    main.main()
