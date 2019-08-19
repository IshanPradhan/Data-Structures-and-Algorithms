from collections import defaultdict

graph = defaultdict(list)

def add_edge(graph,u,v):
    graph[u].append(v)

def generate_edges(graph):
    edges = []
    for node in graph:
        for neghibours in graph[node]:
            edges.append((node,neghibours))
    return edges

add_edge(graph,'a','b')
add_edge(graph,'a','c')
add_edge(graph,'b','c')
add_edge(graph,'b','d')
add_edge(graph,'b','e')
add_edge(graph,'c','e')
add_edge(graph,'c','b')
add_edge(graph,'d','f')
add_edge(graph,'e','f')

print(graph)
