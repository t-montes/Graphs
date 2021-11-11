"""@authors:
    Tony Santiago Montes Buitrago
    Juan Carlos Marin Morales
"""

import graph

def see(mtx):
    for i in mtx:
        print("\t",i)
    print("-"*50)

def printMenu():
    
    print("1 - Obtener la matriz de costos minimos utilizando Dijkstra")
    print("2 - Obtener la matriz de costos minimos utilizando Bellman Ford")
    print("3 - Obtener la matriz de costos minimos utilizando Floy Warschall")
    print("4 - Utilizar BFS para encontrar los componentes conectados")
    print("5 - Utilizar DFS Para saber si existe un ciclo en el grafo y obtener orden topologico")
    print("6 - Salir")

def main():
    print("Bienvenido a nuestra solucion de la tarea 5 de Dalgo :D\n")
    execute = True
    while execute:
        printMenu()
        opc = int(input("Seleccione una opcion para continuar: "))
        if opc == 1:
            print("Opcion Ejecutada: Matriz de costos minimos usando Dijkstra")
            file = input("Ingrese el nombre del archivo que contiene el grafo que desea cargar: ")
            file = "Data/"+file
            g: graph.Graph = graph.loadGraph(file)
            print("Se cargó un grafo con "+str(len(g.v))+" vertices y "+ str(len(g.e))+ " ejes.")
            see(g.all_dijkstra())
        elif opc == 2:
            print("Opcion Ejecutada: Matriz de costos minimos usando Bellman Ford")
            file = input("Ingrese el nombre del archivo que contiene el grafo que desea cargar: ")
            file = "Data/"+file
            g: graph.Graph = graph.loadGraph(file)
            print("Se cargó un grafo con "+str(len(g.v))+" vertices y "+ str(len(g.e))+ " ejes.")
            see(g.all_bellman_ford())
        elif opc == 3:
            print("Opcion Ejecutada: Matriz de costos minimos usando Floyd Warschall")
            file = input("Ingrese el nombre del archivo que contiene el grafo que desea cargar: ")
            file = "Data/"+file
            g: graph.Graph = graph.loadGraph(file)
            print("Se cargó un grafo con "+str(len(g.v))+" vertices y "+ str(len(g.e))+ " ejes.")
            see(g.floyd_warschall2())
        elif opc == 4:
            print("Opcion Ejecutada: Obtener componentes conectados mediante BFS")
            file = input("Ingrese el nombre del archivo que contiene el grafo que desea cargar: ")
            file = "Data/"+file
            g: graph.Graph = graph.loadGraph(file)
            print("Se cargó un grafo con "+str(len(g.v))+" vertices y "+ str(len(g.e))+ " ejes.")
            cc = g.bfs()
            print("Los componentes conectados son: ")
            print(cc)
        elif opc == 5:
            print("Opción Ejecutada: Comprobar si existe un ciclo y en caso negativo, obtener el orden topológico, mediante DFS")
            file = input("Ingrese el nombre del archivo que contiene el grafo que desea cargar: ")
            file = "Data/"+file
            g: graph.Graph = graph.loadGraph(file)
            cc = g.dfs()
            if cc[0]:
                print("El grafo tiene el ciclo:",cc[1])
            else:
                print("El grafo no tiene ciclos.\nUn orden topológico del grafo es:",cc[1])
        elif opc == 6:
            execute = False
        

if __name__ == "__main__":
    main()
