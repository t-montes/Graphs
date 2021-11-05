"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""

import graph

printl = print
def print(*args,**kwargs):
    printl(*args,**kwargs)
    printl("-"*50)

path:str = "Data/distances5.txt"

def main():
    g:graph.Graph = graph.loadGraph(path,first=0)
    
    cs1 = g.minimum_cost("dijkstra")
    cs2 = g.minimum_cost("bellman_ford")
    cs3 = g.minimum_cost("floyd_warschall")

    print(cs1)
    print(cs2)
    print(cs3)


if __name__ == "__main__":
    main()
