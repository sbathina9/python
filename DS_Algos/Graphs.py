class GNode(object):
	def __init__(self, data):
		self.data = data
		self.node_isVisted = False
		self.neighbors=[]

class Graphs(object):

	def BFS(self, node):
		queue = []
		if node is not None:
			queue.append(node)
			
			while len(queue) !=0 :

				#Pop the first element
				node = queue.pop(0)
				if node.node_isVisted is not True:
					#Set it to be visited
					node.node_isVisted = True
					#Visit its neighbors and collect them to the queue
					for neighbor in node.neighbors:
						queue.append(neighbor)
					print node.data	
				
				
		else:
			return
	def DFS(self,node):
		if node is not None:
			if node.node_isVisted is False:
				node.node_isVisted = True
				print node.data
				for neighbor in node.neighbors:
					self.DFS(neighbor)
node1 =  GNode('A')
node2 =  GNode('B')
node3 =  GNode('C')
node4 =  GNode('D')
node5 =  GNode('E')
node6 =  GNode('F')
node7 =  GNode('G')
'''
	  A 
  B			C
D   G     E   F
'''
node1.neighbors=[node2, node3]
node2.neighbors=[node4, node7]
node3.neighbors=[node5, node6]

mygraph = Graphs()
#mygraph.BFS(node1)
mygraph.DFS(node1)
