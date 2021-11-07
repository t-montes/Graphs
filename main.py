"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""

import graph

def see(mtx:list):
    for i in mtx:
        print("\t",i)
    print("-"*50)

path:str = "Data/distances5.txt"
numVertices:int = 100
pathDisc: str = "Data/distancesDisconnected.txt"

def main():
    print(f"\nCreating Graph with {numVertices} vertices")
    g:graph.Graph = graph.loadGraph(path)
    gDisc: graph.Graph = graph.loadGraph(pathDisc)

    #TODO delete this
    cs1 = g.minimum_cost("dijkstra")
    #see(cs1)
    cs2 = g.minimum_cost("bellman_ford")
    #see(cs2)
    cs3 = g.minimum_cost("floyd_warschall")
    
    cs4 = g.minimum_cost("floyd_warschall2")
    print(cs3)
    print(cs4)
    print(gDisc.bfs())
    #print(cs1)
    #print(cs2)
    #print(cs3)

    #see(cs3)
    cs3 = g.minimum_cost("bellman_ford")
    #see(cs2)

if __name__ == "__main__":
    main()
