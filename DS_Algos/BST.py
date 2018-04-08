class TNode(object):
  def __init__(self, data):
    self.data = data
    self.leftchild = None
    self.rightchild = None


class BinarySearchTree(object):
	"""docstring for ClassName"""
	def __init__(self, rootNode=None):
		self.rootNode = rootNode

	def insertNode(self, node_to_insert):
		if node_to_insert is None:
			return

		if self.rootNode is None:
			self.rootNode = node_to_insert
		else:
			self.insert(self.rootNode, node_to_insert)

	def insert(self, rootNode=None, node_to_insert=None):
		if rootNode is None:
			rootNode = node_to_insert
			return rootNode
		else:
			
			if node_to_insert.data < rootNode.data:
				if rootNode.leftchild is not None:
					self.insert(rootNode.leftchild,node_to_insert)
				else:
					rootNode.leftchild = node_to_insert
			else:
				if rootNode.rightchild is not None:
					self.insert(rootNode.rightchild, node_to_insert)
				else:
					rootNode.rightchild = node_to_insert
	def traverse_bst(self, type="inorder"):
		mylist =[]
		if type is "postorder":
		  self.postorder_traversal(self.rootNode, 0, mylist)
		elif type is "preorder":
		  self.preorder_traversal(self.rootNode,0,mylist)
		else:
		  self.inorder_traversal(self.rootNode, 0, mylist)
		#mylist.sort(key=lambda tup: tup[1])
		print mylist

	"""Traverse the left node, root node, right node"""
	def inorder_traversal(self,rootNode, level, mylist):
		if rootNode is not None:
			level=level+1
			self.inorder_traversal(rootNode.leftchild, level, mylist)
			mylist.append( (rootNode.data, level) )
			#print "%s,%s" % (rootNode.data, level)
			self.inorder_traversal(rootNode.rightchild, level, mylist)

	"""Traverse the root node, left node, right node"""
	def preorder_traversal(self,rootNode, level, mylist):
		if rootNode is not None:
			level=level+1
			mylist.append( (rootNode.data, level) )
			self.preorder_traversal(rootNode.leftchild, level, mylist)
			self.preorder_traversal(rootNode.rightchild, level, mylist)
	
	"""Traverse the left node, right node, root node"""
	def postorder_traversal(self,rootNode, level, mylist):
		if rootNode is not None:
			level=level+1
			self.postorder_traversal(rootNode.rightchild, level, mylist)
			self.postorder_traversal(rootNode.leftchild, level, mylist)
			mylist.append( (rootNode.data, level) )

	def BFS(self):
		queue = []
		collect_contents = []
		if self.rootNode is None:
			return None
		else:
			queue.append(self.rootNode)
			while len(queue) > 0:
				mynode = queue.pop(0)
				collect_contents.append(mynode.data)
				if mynode.leftchild is not None:
					queue.append(mynode.leftchild)	
				if mynode.rightchild is not None:
					queue.append(mynode.rightchild)
		print ','.join( str(x) for x in collect_contents)

	def max_value(self):
		if self.rootNode is not None:
			self.max(self.rootNode)

	def max(self,rootNode):
		if rootNode.rightchild is None:
			print rootNode.data
		else:
			self.max(rootNode.rightchild)
	def min_value(self):
		if self.rootNode is not None:
			self.min(self.rootNode)
	def min(self, rootNode):
		if rootNode.leftchild is None:
			print rootNode.data
		else:
			self.min(rootNode.leftchild)

t1 = TNode(10)
t2 = TNode(5)
t3 = TNode(3)
t4 = TNode(4)
t5 = TNode(12)
t6 = TNode(6)
t7 = TNode(11)

bst = BinarySearchTree()
bst.insertNode(t1)
bst.insertNode(t2)
bst.insertNode(t3)
bst.insertNode(t4)
bst.insertNode(t5)
bst.insertNode(t6)
bst.insertNode(t7)

bst.traverse_bst()
bst.traverse_bst(type="preorder")
bst.traverse_bst(type="postorder")
bst.BFS()

bst.max_value()		
bst.min_value()

