# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : ['G'],
    'G' : ['H'],
    'H' : []
}

visited = []

def dfs(visited, graph, node):
    if node not in visited:
        print node
        visited.append(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

dfs(visited, graph, "A")