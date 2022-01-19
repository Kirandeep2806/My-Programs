#!/usr/bin/python3

from createGraph import createGraph

graph = createGraph()

def DFSGraphTraversal(currNode, visited):
    visited.add(currNode)
    print(currNode, end=" ")
    for node in graph[currNode]:
        if node not in visited:
            DFSGraphTraversal(node, visited)

def DFSMain():
    visited = set()
    for node in graph:
        if node not in visited:
            DFSGraphTraversal(node, visited)

DFSMain()
