""" 
Autores: Juan David Bernal, Jean Karlo Buitrago
Mayo del 2024

Proyecto final arboles y grafos
"""

import random
import os

def createRandomDirectedGraph(n, probability=0.005):
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < probability:
                graph[i].append(j)
    
    # Asegurar que no haya nodos sin conexiones de salida
    for i in range(n):
        if not graph[i]:
            while True:
                j = random.randint(0, n-1)
                if i != j:
                    graph[i].append(j)
                    break
    
    # Asegurar que no haya nodos sin conexiones de entrada
    for j in range(n):
        hasIncoming = False
        for i in range(n):
            if j in graph[i]:
                hasIncoming = True
                break
        if not hasIncoming:
            while True:
                i = random.randint(0, n-1)
                if i != j and j not in graph[i]:
                    graph[i].append(j)
                    break

    return graph

def saveGraphToFile(graph, filename):
    with open(filename, 'w') as file:
        for node, edges in enumerate(graph):
            file.write(f"{node}: {' '.join(map(str, edges))}\n")

if __name__ == "__main__":
    n = int(input("Introduce el número de nodos: "))
    graph = createRandomDirectedGraph(n)
    
    # Guardar el archivo en el mismo directorio que el script
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(currentDirectory, "graph.txt")
    
    saveGraphToFile(graph, filePath)
    print(f"Grafo guardado en {filePath}")