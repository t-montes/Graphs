"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""

class Graph():
    def __init__(self):
        ...
    
    """Dijkstra minimum cost algorithm"""
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
        
def loadGraph(path:str, first_state='0') -> Graph:
    ...
