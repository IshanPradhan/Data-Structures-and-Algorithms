class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedto = {}
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedto[nbr] = weight
    
    def __str__(self):
        return str(self.id) + 'connected to: ' + str([x.id for x in self.connectedto])
    
    def getConnections(self):
        return self.connectedto.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self,nbr):
        return self.connectedto[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            new_vertex = self.addVertex(f)
        if t not in self.vertList:
            new_vertex = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

g = Graph()

for i in range(6):
    g.addVertex(i)

g.vertList

g.addEdge(0,1,2)
g.addEdge(0,3,3)
g.addEdge(1,3,4)
g.addEdge(1,5,6)
g.addEdge(1,4,10)
g.addEdge(4,6,15)
g.addEdge(5,6,13)

for vert in g:
    for weights in vert.getConnections():
        print("(%s , %s)" % (vert.getId(), weights.getId()))
