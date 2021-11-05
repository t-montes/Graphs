"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""

import graph

path:str = "Data/distances5.txt"

def main():
    g:graph.Graph = graph.loadGraph(path,first=0)
    
if __name__ == "__main__":
    main()
