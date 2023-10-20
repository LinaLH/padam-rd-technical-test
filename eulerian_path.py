from collections import defaultdict

def read_graph(filename):
    graph = defaultdict(list)
    with open(filename, 'r') as file:
        vertices, edges = map(int, file.readline().split())
        for i in range(vertices):
            x, y = map(float, file.readline().split())
        for _ in range(edges):
            u, v, weight = map(int, file.readline().split())
            graph[u].append((v, weight))
            graph[v].append((u, weight))
    return vertices, graph

#def is_pseudo_eulerian(graph, vertices):
#    odd_degrees = sum(len(neighbors) % 2 for neighbors in graph.values())
#    return odd_degrees == 2  # Le graphe est pseudo-eulerien s'il a exactement deux sommets de degré impair.

def is_pseudo_eulerian(graph, vertices):
    odd_degrees = sum(len(neighbors) % 2 for neighbors in graph.values())
    
    if odd_degrees == 0:
        return "Le graphe est pseudo-eulérien (semi-eulérien)."
    
    if odd_degrees == 2:
        return "Le graphe est pseudo-eulérien (semi-eulérien)."
    
    return "Le graphe n'est ni eulérien ni pseudo-eulérien (semi-eulérien)."


def fleury(graph, vertices):
    def dfs(u):
        for v, w in graph[u]:
            if (u, v) not in visited and (v, u) not in visited:
                visited.add((u, v))
                dfs(v)
                path.append((u, v))

    if not is_pseudo_eulerian(graph, vertices):
        return None

    start_vertex = next(v for v, neighbors in graph.keys() if len(neighbors) % 2 == 1)
    path = []
    visited = set()
    dfs(start_vertex)

    return path

def compute_total_distance(path, graph):
    total_distance = 0
    for u, v in path:
        for neighbor, weight in graph[u]:
            if neighbor == v:
                total_distance += weight
    return total_distance

if __name__ == "__main__":
    vertices, graph = read_graph("instances/hard_to_choose.txt")
    result = is_pseudo_eulerian(graph, vertices)
    
    if "pseudo-eulérien" in result:
        eulerian_path = fleury(graph, vertices)

        if eulerian_path:
            total_distance = compute_total_distance(eulerian_path, graph)
            print("Eulerian Path:", eulerian_path)
            print("Total Distance:", total_distance)
        else:
            print("No Eulerian Path found.")
    else:
        print(result)