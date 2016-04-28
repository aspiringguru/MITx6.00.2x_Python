#https://github.com/aspiringguru/
#https://courses.edx.org/courses/course-v1:MITx+6.00.2x_5+1T2016/info
#working for problem set Problem 2-1, Week 5.

# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# next line imports everything from `graph.py` as if it was defined in this file!
from graph import *

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here
# describing how you will model this problem as a graph.

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    g = WeightedDigraph()
    #Load map from file - open file
    with open(mapFilename) as file:
        #read each line in file.
        for line in file:
            #assumes each line in file contains integers separated by spaces (suitable for .split)
            val1, val2, w, ow = line.split()
            n1 = Node(val1)
            n2 = Node(val2)
            #create WeightedEdge object with data from file
            edg = WeightedEdge(n1,n2,w,ow)
            # add Nodes & WeightedEdge objects to graph.
            #NB: if nodes already exist, "Duplicate node" Printed by Digraph.addNode(node)
            #catch exceptions to prevent failure.  expect large number of duplicate nodes since bidirectional graph.
            try:
                g.addNode(n1)
                print "node n1 added:", n1
            except ValueError, e:
                print e
            try:
                g.addNode(n2)
                print "node n2 added:", n2
            except ValueError, e:
                print e
            try:
                g.addEdge(edg)
                print " WeightedEdge added: ", edg
            except ValueError, e:
                print e

    return g

#print load_map("mit_map.txt")
print "________"
mitMap = load_map("mit_map.txt")
print isinstance(mitMap, Digraph)
print "________"
print isinstance(mitMap, WeightedDigraph)
print "________"
print "mitMap="
print mitMap
print "mitMap.howManyNodes=", mitMap.howManyNodes()
print "mitMap.howManyEdges=", mitMap.howManyEdges()
#print mitMap.edges
#print mitMap.nodes
