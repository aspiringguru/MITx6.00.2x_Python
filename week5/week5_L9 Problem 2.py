class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->(' + str(self.weight) + ')'\
            + str(self.dest)

class Digraph(object):
    def __init__(self):
        self.nodes = set([])#list
        self.edges = {}#dictionary
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]#nodes that can be reached in one step from the input node
    def hasNode(self, node):#test if a node is in the graph
        return node in self.nodes
    def __str__(self):#'nice' representation of the graph
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]

class Graph(Digraph):
    # Graph extends Digraph, inherits methods & attributes
    #
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result

'''
def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0].nodes[1]))
    g.addEdge(Edge(nodes[1].nodes[2]))
    g.addEdge(Edge(nodes[2].nodes[3]))
    g.addEdge(Edge(nodes[3].nodes[4]))
    g.addEdge(Edge(nodes[3].nodes[5]))
    print g

testSP()
'''

#code above from graph.py
#code below from problem definition Week 5 L9 problem 2
"""
Consider our representation of permutations of students in a line from Problem 1.
In this case, we will consider a line of _THREE_ students, Alice, Bob, and Carol (denoted A, B, and C).
Using the Graph class created in the lecture, we can create a graph with the design chosen in Problem 1.
To recap, vertices represent permutations of the students in line;
edges connect two permutations _IF_ one can be made into the other by swapping two adjacent students.
"""

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)
    #print "g.hasNode(n)=", g.hasNode(n)
    #print "node n=", n

#print g#returns null since no edges assigned yet.
#print type(g)
print "_____________________"

"""
Notes:
 - messy print statements to be commented out.
 - not the most optimal algorythm? it works but rather rough and ugly.
 - would appreciate seeing a tidy solution.
"""
for n in nodes:
    print "==================================="
    nodeNname = n.getName()
    for y in nodes:
        if y==n:
            #print "skipping self test against same node"
            pass
        else:
            nodeYname = y.getName()
            print "nodeNname=", nodeNname, " nodeYname=",nodeYname
            for i in [0,1]:
                count = 0
                nodeYnameForward = nodeYname[i:i+2]
                nodeYnameBackward = nodeYnameForward[::-1]
                print "i=", i, " nodeNname[i:i+2]=", nodeNname[i:i+2], " nodeYname[i:i+2]=", nodeYnameForward, " nodeYnameForward[::-1]=", nodeYnameBackward
                if nodeNname[i:i+2]==nodeYnameForward:
                    count += 1
                    print "nodeNname[i:i+2]==nodeYnameForward is TRUE, count=", count
                elif nodeNname[i:i+2]==nodeYnameBackward:
                    count += 1
                    print "nodeNname[i:i+2]==nodeYnameBackward is TRUE, count=", count
            #print "at end of loop, count=", count
                if count ==1:
                    print "edge found, can swap two students in queue to match"
                    #if edge already in graph, do not add. use g.childrenOf(node) - returns list, check if node in list.
                    tempList = g.childrenOf(n)
                    if y not in tempList:
                        print "****adding edge composed of node ", n, " & ",y
                        g.addEdge(Edge(n, y))
                    else:
                        print "node already in g.childrenOf(n), no edge added"
                else:
                    print "no edge found"

print "printing graph"
print g
print "printing edges"
print "========================"
#childrenOf(self, node)
for n in nodes:
    #print g.childrenOf(n)
    #print type(g.childrenOf(n))
    print "_____________________"
    print "node =", n.getName()
    for n in g.childrenOf(n):
        print n
#









#Add the appropriate edges to the graph.

"""
Write your code in terms of the nodes list from the code above.
For each node, think about what permutation is allowed.
A permutation of a set is a rearrangement of the elements in that set.
In this problem, you are only adding edges between nodes whose permutations
are between elements in the set beside each other .
For example, an acceptable permutation (edge) is between
"ABC" and "ACB" but not between "ABC" and "CAB".

if 2 of the 3 match, then an edge exists
"""


