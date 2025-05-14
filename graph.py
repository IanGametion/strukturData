class vertex:
    def __init__(self, node):
        self.id = node
        self.visited = False

    def getvertexid(self):
        return self.id
    
    def setvertexid(self, id):
        self.id = id

    def setvisited(self, visited):
        self.visited = visited

    def getConnections(self, G):
        return G.adjMatrix[self.id]
    
    def addNeighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)

    def __str__(self):
        return str(self.id)
    
class Graph:
    def __init__(self, numVert, cost = 0):
        self.adjMatrix = [[-1] * numVert for _ in range(numVert)]
        self.numVert = numVert
        self.vertices = []
        for i in range(0, numVert):
            newvert = vertex(i)
            self.vertices.append(newvert)

    def setVertex (self, vtx, id):
        if 0 <= vtx < self.numVert:
            self.vertices[vtx].setvertexid(id)

    def getVertex (self, n):
        for vertin in range (0, self.numVert):
            if n == self.vertices[vertin].getvertexid():
                return vertin
        return -1
        
    def addEdge (self, frm, to, cost = 0):
        if self.getVertex(frm) != -1 and self.getVertex(to) != -1:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            #hilangkan jika ada arah
            self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost

    def getVertices (self):
        vertices = []
        for vertin in range (0, self.numVert):
            vertices.append(self.vertices[vertin].getvertexid())
        return vertices
        
    def printMatrix (self):
        for u in range (0, self.numVert):
            row = []
            for v in range (0, self.numVert):
                row.append(self.adjMatrix[u][v])
            print(row)
            
    def getEdges (self):
        edges = []
        for v in range (0, self.numVert):
            for u in range (0, self.numVert):
                if self.adjMatrix[u][v] != -1:
                    vid = self.vertices[v].getvertexid()
                    wid = self.vertices[u].getvertexid()
                    edges.append((vid, wid, self.adjMatrix[u][v]))
        return edges
        
if __name__ == "__main__":
    G = Graph(5)
    G.setVertex(0, "A")
    G.setVertex(1, "B")
    G.setVertex(2, "C")
    G.setVertex(3, "D")
    G.setVertex(4, "E")
    print("Graph data:")
    G.addEdge("A", "E", 10)
    G.addEdge("A", "C", 12)
    G.addEdge("C", "B", 30)
    G.addEdge("B", "E", 40)
    G.addEdge("E", "D", 50)
    G.printMatrix()
    print(G.getEdges())