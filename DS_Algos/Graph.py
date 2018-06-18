from __future__ import print_function
from collections import defaultdict

class Node(object):
    def __init__(self, value):
        self.value = value
        self.isvisited = False
    def __str__(self):
        return (self.value)

class Graph(object):
    def __init__(self):
        self.vertices = defaultdict(list)

    def addEdge(self, start, end):
        self.vertices[start].append(end)

    def BFS(self, start):

        if start is None:
            return None

        queue = []
        queue.append(start)

        while(len(queue) > 0):
            element = queue.pop(0)
            if element.isvisited is False:
                element.isvisited = True
                print (element.value)
                for item in self.vertices[element]:
                    if item.isvisited is False:
                        queue.append(item)

    def DFS(self, start):
        if start is None:
            return None
        start.isvisited = True
        for item in self.vertices[start]:
            if item.isvisited is False:
                self.DFS(item)
        print (start.value)

    def DFS_iterate(self, start):
        if start is None:
            return None
        staging, visited = [], []
        staging.append(start)
        while len(staging) > 0:
            for item in staging:
                print (item.value, end='')
            for item in visited:
                print (item.value, end='')
            s = staging.pop(0)
            s.isvisited = True
            visited.append(s)
            for item in self.vertices[s]:
                if item.isvisited is False:
                    staging.append(item)
        for item in visited:
            print (item.value)

g = Graph()
node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

g.addEdge(node0, node1)
g.addEdge(node0, node2)
g.addEdge(node1, node2)
g.addEdge(node2, node0)
g.addEdge(node2, node3)
g.addEdge(node3, node3)
 
print ("Following is Breadth First Traversal"
                           " (starting from vertex 2)")
#g.BFS(node2)
print ("Following is Depth First Traversal"
                           " (starting from vertex 2)")
g.DFS_iterate(node2)

