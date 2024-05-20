""" 
Autores: Juan David Bernal, Jean Karlo Buitrago
Mayo del 2024

Proyecto final arboles y grafos
"""

def readGraphFromFile(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        graph = []
        for line in lines:
            parts = line.strip().split(':')
            node = int(parts[0].strip())
            edges = list(map(int, parts[1].strip().split())) if len(parts) > 1 and parts[1].strip() else []
            while len(graph) <= node:
                graph.append([])
            graph[node] = edges
    return graph

def tarjanAp(graph):
    def apAux(v):
        nonlocal time
        visited[v] = True
        disc[v] = low[v] = time
        time += 1
        children = 0

        for w in graph[v]:
            if not visited[w]:
                parent[w] = v
                children += 1
                apAux(w)

                low[v] = min(low[v], low[w])

                if parent[v] is None and children > 1:
                    ap[v] = True
                if parent[v] is not None and low[w] >= disc[v]:
                    ap[v] = True
            elif w != parent[v]:
                low[v] = min(low[v], disc[w])

    n = len(graph)
    visited = [False] * n
    disc = [float('inf')] * n
    low = [float('inf')] * n
    parent = [None] * n
    ap = [False] * n
    time = 0

    for i in range(n):
        if not visited[i]:
            apAux(i)

    articulationPoints = [index for index, value in enumerate(ap) if value]
    
    # Contar el número de aristas que llevan a cada nodo
    inDegree = [0] * n
    for i in range(n):
        for j in graph[i]:
            inDegree[j] += 1
    
    # Ordenar los puntos de articulación por el número de aristas entrantes de mayor a menor
    articulationPoints.sort(key=lambda x: inDegree[x], reverse=True)
    
    return articulationPoints, inDegree

if __name__ == "__main__":
    import os
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "graph.txt")
    
    graph = readGraphFromFile(file_path)
    ap, in_degree = tarjanAp(graph)
    
    if not ap:
        print("No hay puntos de articulación")
    else:
        print("Puntos de articulación (ordenados por cantidad de aristas entrantes):")
        for node in ap:
            print(f"Nodo {node} con {in_degree[node]} aristas entrantes")