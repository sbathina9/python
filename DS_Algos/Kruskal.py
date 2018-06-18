'''
1. Sort all the edges
2. For each edge start_node, end_node and weight; find the parent. Parent is different then merge
3. If parent is same cycle
'''
class Node(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

class Edge(object):
    def __init__(self, start, end, weight):
        self.start_node = start
        self.end_node = end
        self.weight = weight

    def __cmp__(self, otherEdge):
        return self.cmp(self.weight, otherEdge.weight)

    def __lt__(self,otherEdge):
        return self.weight < otherEdge.weight


class Kruskal(object):
    def __init__(self, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.edges = sorted( self.edges, key = lambda x: x.weight)
        print (len(self.edges))


    def findParent(self, node):
        if node.parent == None:
            return node
        else:
            return self.findParent(node.parent)

    def algo(self):
        min_path_weight = 0
        for item in self.edges:
           start = item.start_node
           end = item.end_node
           weight =  item.weight
           start_parent = self.findParent(start)
           end_parent = self.findParent(end)

           if start_parent != end_parent:
               print (start.name, end.name, weight)
               end_parent.parent = start_parent
               self.nodes.remove(end_parent)
               min_path_weight = min_path_weight + weight

        print (len(self.nodes), min_path_weight)

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node_list = [node1, node2, node3, node4, node5]

edge1 = Edge(node1, node2, 2)
edge2 = Edge(node1, node3, 1)
edge3 = Edge(node1, node4, 3)
edge4 = Edge(node3, node5, 6)
edge5 = Edge(node3, node4, 5)
edge6 = Edge(node2, node4, 4)
edge7 = Edge(node4, node5, 7)
edge_list = [edge1, edge2, edge3, edge4, edge5, edge6, edge7]


kruskal = Kruskal(edge_list, node_list)
kruskal.algo()
