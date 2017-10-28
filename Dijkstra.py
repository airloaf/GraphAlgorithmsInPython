from PriorityQueue import PriorityQueue
import math

#Sample hardcoded graph
graph = {}
graph['A'] = [['B', 5], ['D', 9], ['E', 2]]
graph['B'] = [['A', 5], ['C', 2]          ]
graph['C'] = [['B', 2], ['D', 3]          ]
graph['D'] = [['A', 9], ['C', 3], ['F', 2]]
graph['E'] = [['A', 2], ['F', 3]          ]
graph['F'] = [['D', 2], ['E', 3]          ]

#Create a priority queue
priorityQueue = PriorityQueue()
#Set the positions of each equal to infinity except the start which is equal to 0
for i in graph.keys():
    priorityQueue.add(i, math.inf)
priorityQueue.decrease('A', 0)

#Map of the parents of each node
parentMap = {}
parentMap['A'] = None

#Map of the distances for each node
distanceMap = {}

def Dijkstra(graph, priorityQueue, parentMap, distanceMap):

    #Get the current node
    currentNode = priorityQueue.extractMin()

    #Update the distance of the current node
    distanceMap[currentNode[0]] = currentNode[1]

    #Get the neighbors of the current node
    #and update their values
    neighbors = graph[currentNode[0]]
    for i in neighbors:
        name = i[0]
        dist = i[1] + distanceMap[currentNode[0]]

        #Check if there exists a node in the heap map, if it has been remove it will not be there
        if priorityQueue.contains(name):
            #Check if the distance is greater in the map than in connection
            if priorityQueue.getValue(name) > dist:
                priorityQueue.decrease(name, dist)
                parentMap[name] = currentNode[0]

    #Check if there are any more elements to explore
    if priorityQueue.getSize() > 0:
        Dijkstra(graph, priorityQueue, parentMap, distanceMap)

Dijkstra(graph, priorityQueue, parentMap, distanceMap)

print(distanceMap)
print(parentMap)
