"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""

import graph

def see(mtx:list):
    for i in mtx:
        print("\t",i)
    print("-"*50)

path:str = "Data/distances100.txt"
numVertices:int = 100

def main():
    print(f"\nCreating Graph with {numVertices} vertices")
    g:graph.Graph = graph.loadGraph(path)

    #TODO delete this
    cs1 = g.minimum_cost("dijkstra")
    #see(cs1)
    cs2 = g.minimum_cost("bellman_ford")
    #see(cs2)
    cs3 = g.minimum_cost("floyd_warschall")
    #see(cs3)

if __name__ == "__main__":
    main()
