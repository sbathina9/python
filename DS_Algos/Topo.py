from collections import defaultdict
'''
iterate through the list of the nodes and pick the one not visited
Set the node as visited
Find all the children and do a DFS on them till we reach a node with no children or all visited. Add that to the stack
Backtrack and add all nodes part of that direction
reverse the list and print

'''
class Node(object):
    def __init__(self, name):
        self.name = name
        self.visited = False

class Graph(object):
    def __init__(self, node_list):
        self.node_list = node_list
        self.pointsTo = defaultdict(list)

    def addEdge(self, start, end):
        self.pointsTo[start].append(end)

    def Topo_sort(self):
        stack = []

        for item in node_list:
            if item.visited is False:
                self.Topo_Util(stack, item)
        stack = stack[::-1]

        for item in stack:
            print (item.name)

    def Topo_Util(self, stack, node):

        if node in self.pointsTo:
            node.visited=True
            mylist = self.pointsTo[node]
            for item in mylist:
                if item.visited is False:
                    self.Topo_Util(stack, item)
        else:
            node.visited=True
            
        stack.append(node)

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node_list = [node5, node4, node2, node3, node0, node1]

g = Graph(node_list)
g.addEdge(node5, node2);
g.addEdge(node5, node0);
g.addEdge(node4, node0);
g.addEdge(node4, node1);
g.addEdge(node2, node3);
g.addEdge(node3, node1);

g.Topo_sort()

