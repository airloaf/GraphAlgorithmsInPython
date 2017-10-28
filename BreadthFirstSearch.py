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

def BFS(g, hasVisited, queue):
    #Check if there is something in the queue
    current = queue[0]
    queue.pop(0)
    hasVisited[current] = True

    #print the current node
    print(current)

    #Get the neighbors of the current node
    neighbors = g[current]

    #For each neighbor check if it has not been visited
    for i in neighbors:
        if not hasVisited[i] and i not in queue:
            queue.append(i)

    if len(queue) > 0:
        BFS(g, hasVisited, queue)
    else:
        return


visited = {}
for i in graph.keys():
    visited[i] = False

queue = ['A']

BFS(graph, visited, queue)
