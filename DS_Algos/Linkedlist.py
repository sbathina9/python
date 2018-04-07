import pdb

class Node(object):
	def __init__(self, data):
		self.data =  data
		self.nextNode = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0
	
	def insertAtfront(self, data):
		if self.head == None:
			self.head = Node(data)
		else:
			new_head = Node(data)
			new_head.nextNode = self.head
			self.head = new_head

	def insertAtEnd(self,data):		
		if self.head == None:
			self.head = Node(data)
		else:
			myiter = self.head
			while myiter.nextNode is not None:
				myiter = myiter.nextNode
			myiter.nextNode = Node(data) 

	def printll(self):
		myiter = self.head
		while myiter is not None:
			print myiter.data
			myiter = myiter.nextNode
	def removeFront(self):
		myiter = self.head
		if myiter is None:
			return None
		else:
			self.head = myiter.nextNode
			value=myiter.data
			del(myiter)
			return value

	def removeEnd(self):
		current = self.head
		previous = self.head
		#pdb.set_trace()

		if current is None:
			return None
		else:
			if current.nextNode is None:
				value = current.data
				del(current)
				self.head = None
			else:
				while current.nextNode is not None:
					previous = current
					current = previous.nextNode
				value = current.data
				del(current)	
				previous.nextNode = None


myll = LinkedList()
myll.insertAtEnd(10)
myll.insertAtEnd(5)
myll.insertAtEnd(8)
#myll.insertAtEnd(4)
#myll.insertAtEnd(12)

#myll.printll()
myll.removeEnd()
myll.printll()