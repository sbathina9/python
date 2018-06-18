'''
Shortest path algo
'''
from __future__ import print_function
import heapq

class Node(object):
    def __init__(self, name):
        self.name = name
        self.pointsTo = []
        self.minDistance = float('inf')
        self.ancestor = None

    def __cmp__(self, otherV):
        return self.cmp(self.minDistance, otherV.minDistance)

    def __lt__(self, otherV):
        return self.minDistance < otherV.minDistance

class Edge(object):

    def __init__(self, weight, start, end):
        self.start = start
        self.end = end
        self.weight = weight

class Shortest_Path(object):
    def __init__(self, start_vertex):
        self.start_vertex = start_vertex
        self.start_vertex.minDistance=0

    def shortDistance(self):

        queue = []
        heapq.heappush(queue, self.start_vertex)

        while len(queue) > 0:
            vertex = heapq.heappop(queue)

            for child in vertex.pointsTo:
                sv = child.start
                ev = child.end
                weight = child.weight

                newDistance =  weight + sv.minDistance

                if newDistance < ev.minDistance:
                    ev.minDistance =  newDistance
                    ev.ancestor = sv
                heapq.heappush(queue,ev)

    def printPath(self, targetVertex):
        node = targetVertex
        print ("The cost is %d" % node.minDistance)
        while node is not None:
            print (node.name, end="")
            node = node.ancestor
        print("")

node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");
node5 = Node("E");
node6 = Node("F");
node7 = Node("G");
node8 = Node("H");

edge1 = Edge(5,node1,node2);
edge2 = Edge(8,node1,node8);
edge3 = Edge(9,node1,node5);
edge4 = Edge(15,node2,node4);
edge5 = Edge(12,node2,node3);
edge6 = Edge(4,node2,node8);
edge7 = Edge(7,node8,node3);
edge8 = Edge(6,node8,node6);
edge9 = Edge(5,node5,node8);
edge10 = Edge(4,node5,node6);
edge11 = Edge(20,node5,node7);
edge12 = Edge(1,node6,node3);
edge13 = Edge(13,node6,node7);
edge14 = Edge(3,node3,node4);
edge15 = Edge(11,node3,node7);
edge16 = Edge(9,node4,node7);

node1.pointsTo.append(edge1);
node1.pointsTo.append(edge2);
node1.pointsTo.append(edge3);
node2.pointsTo.append(edge4);
node2.pointsTo.append(edge5);
node2.pointsTo.append(edge6);
node8.pointsTo.append(edge7);
node8.pointsTo.append(edge8);
node5.pointsTo.append(edge9);
node5.pointsTo.append(edge10);
node5.pointsTo.append(edge11);
node6.pointsTo.append(edge12);
node6.pointsTo.append(edge13);
node3.pointsTo.append(edge14);
node3.pointsTo.append(edge15);
node4.pointsTo.append(edge16);


sp = Shortest_Path(node1)
sp.shortDistance()
sp.printPath(node4)


                
