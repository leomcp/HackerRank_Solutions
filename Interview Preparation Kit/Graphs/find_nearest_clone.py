

class Vertex:
	def __init__(self, data, color):
		self.data  = data 
		self.neighbours = []
		self.color = color
		self.visited = False 
		self.distance = 0 

	def add_neighbour(self, v):
		self.neighbours.append(v)
		self.neighbours.sort()

class Graph:
	def __init__(self):
		self.vertices =  {}

	def add_vertex(self, v, c):
		if v not in self.vertices:
			self.vertices[v] = Vertex(v, c)

	def add_edge(self, v1, c1, v2, c2):
		if v1 not in self.vertices:
			self.add_vertex(v1, c1)
		if v2 not in self.vertices:
			self.add_vertex(v2, c2)
		self.vertices[v1].add_neighbour(v2)
		self.vertices[v2].add_neighbour(v1)

	def make_graph(self, graph_edges, graph_from, graph_to, ids):
		for idx in range(graph_edges):
			self.add_edge(graph_from[idx],ids[graph_from[idx]-1], graph_to[idx], ids[graph_to[idx]-1])
		self.print_graph()

	def _bfs(self, start_vertex):
		q = []

		self.vertices[start_vertex].visited = True 
		for neighbour in self.vertices[start_vertex].neighbours:
			q.append(neighbour)
			self.vertices[neighbour].distance = 1
		color_clone = self.vertices[start_vertex].color

		while len(q)>0:
			top_vertex = q[0]
			top_vertex_distance = self.vertices[top_vertex].distance
			top_vertex_color = self.vertices[top_vertex].color
			self.vertices[top_vertex].visited = True 
			del(q[0])

			if top_vertex_color == color_clone:
				print("{} : {} {}".format(start_vertex, top_vertex, top_vertex_color))
				return top_vertex_distance
			else:
				for neighbour in self.vertices[top_vertex].neighbours:
					if self.vertices[neighbour].visited==False:
						q.append(neighbour)
						self.vertices[neighbour].distance = top_vertex_distance + 1 
		return -1 


	def find_nearest_clone(self, start_vertex):
		if start_vertex in self.vertices:
			shortest_distance = self._bfs(start_vertex)
			return shortest_distance

	def print_graph(self):
		if self.vertices:
			for vertex in self.vertices:
				neighbours = self.vertices[vertex].neighbours
				color = self.vertices[vertex].color
				print("{} : {} {}".format(vertex, neighbours, color))

if __name__ == "__main__":

	g = Graph()

	graph_from = [1, 1, 2, 3]
	graph_to = [2, 3, 4, 5]
	ids = [1, 2, 3, 3, 2]
	val = 2

	graph_nodes = 5
	graph_edges = 4

	g.make_graph(graph_edges, graph_from, graph_to, ids)

	print(g.find_nearest_clone(val))