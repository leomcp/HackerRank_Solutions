
class Vertex:
    def __init__(self, data):
        self.data = data 
        self.visited = False
        self.neighbours = []
        self.distance = 0
        
    def addNeighbour(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            
class Graph:
    def __init__(self, n):
        self.vertices = {}
        self.numOfNodes = n
        self.buildGraph()
        
    def buildGraph(self):
        for v in range(1, self.numOfNodes+1):
            self.vertices[str(v)] = None

    def _addVertex(self, v):
        self.vertices[str(v)] = Vertex(v)
        
    def connect(self, u, v):
        if self.vertices[str(u)] is None:
            self._addVertex(u)
        if self.vertices[str(v)] is None:
            self._addVertex(v)
        self.vertices[str(u)].addNeighbour(str(v))
        self.vertices[str(v)].addNeighbour(str(u))
        
    def _bfs(self, start_v):
        q = []
        q.append(start_v)
        self.vertices[start_v].visited = True 
        
        while len(q)>0:
            head_v = q[0]
            del(q[0])
            
            for n in self.vertices[head_v].neighbours:
                if self.vertices[n].visited == False:
                    q.append(n)
                    self.vertices[n].visited = True 
                    self.vertices[n].distance = self.vertices[head_v].distance + 6
    
    def find_all_distances(self, start_v):
        
        def print_all_distances():
            for v in sorted(self.vertices):
                if self.vertices[v] is None:
                    print(-1, end= " ")
                elif v != str(start_v):
                    if self.vertices[v].distance == 0:
                        print(-1, end = " ")
                    else:
                        print(self.vertices[v].distance, end= " ")
            print()
            
        if self.vertices:
            if str(start_v) not in self.vertices:
                return 
            self._bfs(str(start_v))
            
            print_all_distances()    

    def printGraph(self):
        if self.vertices:
            for v in sorted(self.vertices):
                if self.vertices[v]:
                    print("{} : {}".format(v, self.vertices[v].neighbours))
                else:
                    print("{} : None".format(v))
                
if __name__ == "__main__":
    
    q = int(input())
    for i in range(q):
        # n --> num of nodes m --> num of edges 
        n,m = [int(value) for value in input().split()]
        graph = Graph(n)
        for i in range(m):
            x,y = [int(x) for x in input().split()]
            graph.connect(x,y) 
        s = int(input())

        graph.printGraph()
        print("-"*50)
        graph.find_all_distances(s)