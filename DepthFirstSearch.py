graph = {}
graph['A'] = ['B', 'S']
graph['S'] = ['A', 'C', 'G']
graph['B'] = ['A']
graph['C'] = ['D', 'E', 'F', 'S']
graph['D'] = ['C', 'E']
graph['E'] = ['D', 'H']
graph['F'] = ['C', 'G']
graph['G'] = ['S', 'F']
graph['H'] = ['E', "G"]

def DFS(graph, visited, stack):
    current = stack[len(stack) - 1]
    visited[current] = True;

    print(current)

    neighbors = graph[current]

    for i in neighbors:
        if not visited[i] and i not in stack:
            stack.append(i)
            DFS(graph, visited, stack)

    stack.pop()


visited = {}
for i in graph.keys():
    visited[i] = False

stack = ['A']

DFS(graph, visited, stack)
