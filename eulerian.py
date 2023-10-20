import sys
import os
from collections import defaultdict

# Fonction pour lire un graphe depuis un fichier donné en paramètre.
def read_graph(filename): 
    graph = defaultdict(list)
    with open(filename, 'r') as file:
        vertices, edges = map(int, file.readline().split())
        
        # Lecture des coordonnées des sommets (ignorées dans ce code)
        for i in range(vertices):
            x, y = map(float, file.readline().split())
            
        # Lecture des arêtes du graphe.
        for _ in range(edges):
            u, v, weight = map(int, file.readline().split())
            graph[u].append((v, weight))
            graph[v].append((u, weight))
    return vertices, graph

# Fonction pour déterminer si le graphe est pseudo-eulérien.
def is_pseudo_eulerian(graph, vertices):
    odd_degrees = sum(len(neighbors) % 2 for neighbors in graph.values())
    
    if odd_degrees == 0:
        return "Le graphe est pseudo-eulérien (semi-eulérien)."
    
    if odd_degrees == 2:
        return "Le graphe est pseudo-eulérien (semi-eulérien)."
    
    return "Le graphe n'est ni eulérien ni pseudo-eulérien (semi-eulérien)."

# Fonction pour trouver un chemin pseudo-eulérien à l'aide de l'algorithme de Fleury
def fleury(graph, vertices):
    def dfs(u):
        for v, w in graph[u]:
            if (u, v) not in visited and (v, u) not in visited:
                visited.add((u, v))
                dfs(v)
                path.append((u, v))

    result = is_pseudo_eulerian(graph, vertices)
    if "pseudo-eulérien" not in result:
        return None

    # Trouver un sommet de degré impair pour démarrer l'algorithme
    start_vertex = None
    for vertex, neighbors in graph.items():
        if len(neighbors) % 2 == 1:
            start_vertex = vertex
            break

    if start_vertex is None:
        start_vertex = next(iter(graph.keys()))

    path = []
    visited = set()
    dfs(start_vertex)

    return path

# Fonction pour calculer la distance totale d'un chemin
def compute_total_distance(path, graph):
    total_distance = 0
    for u, v in path:
        for neighbor, weight in graph[u]:
            if neighbor == v:
                total_distance += weight
    return total_distance

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python eulerian.py input_file.txt")
    else:
        input_file = os.path.join("instances", sys.argv[1])  # Ajouter "instances/" au chemin du fichier

        vertices, graph = read_graph(input_file)
        eulerian_path = fleury(graph, vertices)

    if eulerian_path:
        total_distance = compute_total_distance(eulerian_path, graph)
        print("Eulerian Path:", eulerian_path)
        print("Total Distance:", total_distance)
    else:
        print("No Eulerian Path found.")
