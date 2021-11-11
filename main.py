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
path2:str = "Data/distances5_2.txt"
numVertices:int = 5
pathDisc: str = "Data/distancesDisconnected.txt"

def main():
    print(f"\nCreating Graph with {numVertices} vertices")
    g:graph.Graph = graph.loadGraph(path)
    g2:graph.Graph = graph.loadGraph(path2)
    gDisc: graph.Graph = graph.loadGraph(pathDisc)

    #TODO delete this
    cs1 = g.minimum_cost("dijkstra")
    print(cs1)
    cs2 = g.minimum_cost("bellman_ford")
    print(cs2)
    cs3 = g.minimum_cost("floyd_warschall")
    
    cs4 = g.minimum_cost("floyd_warschall2")
    print(cs3)
    print(cs4)
    #print(gDisc.bfs())

    cs5 = g.dfs()
    print(cs5)
    print(g)

    cs6 = g2.dfs()
    print(cs6)
    #print(g2)

if __name__ == "__main__":
    main()
