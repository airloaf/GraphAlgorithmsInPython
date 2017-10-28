class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.map = {}

    #Retrieve and pop min element
    def extractMin(self):

        #Get the root element
        pair = self.heap[0]
        valueToReturn = pair

        #Remove the root from the map
        self.map.pop(pair[0])

        #If there is more elements in the array
        if len(self.map) > 0:

            #Get the last pair
            lastPair = self.heap[len(self.heap) - 1]

            #Remove the last element and make it the root
            self.heap.pop()
            self.heap[0] = lastPair

            #Move that key up!
            self.map[lastPair[0]] = 0

            #Bubble down to make sure it mainains the heap property
            self.bubbleDown(0)

        #There is no more elements so remove the element in the heap
        else:
            self.heap.pop()

        #Return the min value
        return valueToReturn

    def bubbleDown(self, pos):

        pair = self.heap[pos]

        #Get the children's positions
        leftChildPos = 2*pos + 1
        rightChildPos = 2*pos + 2

        if rightChildPos > len(self.heap) - 1 or leftChildPos > len(self.heap) - 1:
            return

        #Get the children of the node at the position
        leftChild = self.heap[leftChildPos]
        rightChild = self.heap[rightChildPos]

        #Check if the left child needs to swap with the current node
        if leftChild[1] < rightChild[1]:
            if leftChild[1] < pair[1]:

                #Swap the indices
                self.map[leftChild[0]] = pos
                self.map[pair[0]] = leftChildPos

                #Swap the values
                temp = pair
                self.heap[pos] = leftChild
                self.heap[leftChildPos] = temp

                self.bubbleDown(leftChildPos)

        #Check if the right child needs to swap with the current node
        else:
            if rightChild[1] < pair[1]:
                # Swap the indices
                self.map[rightChild[0]] = pos
                self.map[pair[0]] = rightChildPos

                # Swap the values
                temp = pair[1]
                self.heap[pos] = rightChild
                self.heap[rightChildPos] = temp

                self.bubbleDown(rightChildPos)

    #Add new item to the heap
    def add(self, k, v):

        self.map[k] = len(self.heap)

        self.heap.append([k, v])
        self.bubbleUp(len(self.heap) - 1)

    #Inserted method to bubble up value
    def bubbleUp(self, pos):

        pair = self.heap[pos]
        parentPos = int((pos - 1) / 2)

        #Check if the parent's position is less than 0
        if parentPos < 0:
            return

        parent = self.heap[parentPos]

        #Check if the parent is greater than the current
        if parent[1] > pair[1]:

            #Swap the pair in the map
            self.map[pair[0]] = parentPos
            self.map[parent[0]] = pos

            #Swap the pair in the heap
            temp = pair
            self.heap[pos] = parent
            self.heap[parentPos] = temp

            #Changed occurred, keep bubbling
            self.bubbleUp(parentPos)

    #Check if there exists a key
    def contains(self, k):
        return k in self.map

    #Decrease that key by a value
    def decrease(self, k, v):
        if not self.contains(k):
            return

        #Decrease node to value v
        self.heap[self.map[k]][1] = v

        #Bubble up to ensure heap property
        self.bubbleUp(self.map[k])


    def getValue(self, k):
        pos = self.map[k]
        return self.heap[pos][1]

    def getSize(self):
        return len(self.heap)

    def printHeap(self):
        print(self.heap)

    def printMap(self):
        print(self.map)

    def printAll(self):
        self.printHeap()
        self.printMap()