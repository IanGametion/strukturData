import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxint
        self.visited = False
        self.previous = None
        
    def addNeighbor(self, neighbor, weight = 0):
        self.adjacent[neighbor] = weight
        
    def getConnection(self):
        return self.adjacent.keys()
    
    def getVertexid(self):
        return self.id
    
    def getWeight(self, neighbor):
        return self.adjacent[neighbor]
    
    def setDistance(self, dist):
        self.distance = dist
        
    def getDistance(self):
        return self.distance
    
    def setPrevious(self, prev):
        self.previous = prev
        
    def setVisited(self):
        self.visited = True
        
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
class Graph:
    def __init__(self):
        self.vertDict = {}