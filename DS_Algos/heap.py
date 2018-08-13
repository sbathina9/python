from random import randint

class Heap(object):
	def __init__(self):
		self.size = 0
		self.heap = []

	def parent(self, index):
		if index % 2 == 0:
			return (index-2)/2
		else:
			return (index -1)/2
			
	def heappush(self, value, max = False):
		self.heap.append(value)
		self.size = self.size + 1

		if self.size == 1:
			return

		index = self.size-1
		parent =  self.parent(index)

		while (parent >=0):

			if max == True:
				if self.heap[parent] < self.heap[index]:
					self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
				else:
					break
			else:
				if self.heap[parent] > self.heap[index]:
					self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
				else:
					break
			index = parent
			parent =self.parent(parent)

	def heappop(self, max = False):

		if self.size <= 0:
			return None

		top = self.heap[0]
		self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
		self.size = self.size - 1

		index = 0

		while(index < self.size):
			left_child =  2*index + 1
			right_child = 2*index + 2


			if left_child < self.size:
				childToSwap = None

				if right_child >= self.size:
					childToSwap = left_child 
				else:
					if max is False:
						if self.heap[left_child] < self.heap[right_child]:
							childToSwap = left_child
						else:
							childToSwap = right_child
					else:
						if self.heap[left_child] > self.heap[right_child]:
							childToSwap = left_child
						else:
							childToSwap = right_child
				if max is False:										
					if self.heap[index] > self.heap[childToSwap]:
						self.heap[index], self.heap[childToSwap] = self.heap[childToSwap], self.heap[index]
					else:
						break
				else:
					if self.heap[index] < self.heap[childToSwap]:
						self.heap[index], self.heap[childToSwap] = self.heap[childToSwap], self.heap[index]
					else:
						break

				index = childToSwap
			else:
				break
		return top

	def heapprint(self):
		for index in range(0, self.size):
			print(self.heap[index], index)

h = Heap()


for i in range(1,101):
	h.heappush(randint(0,1000), max = True)
h.heapprint()

for i in range(1,102):
	print ("Heap pop value ", h.heappop(max = True))
