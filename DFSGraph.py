#!/usr/bin/python3

from createGraph import createGraph

def DFSGraphTraversal(currNode, visited, graph):
    visited.add(currNode)
    print(currNode, end=" ")
    for node in graph[currNode]:
        if node not in visited:
            DFSGraphTraversal(node, visited, graph)

def DFSMain(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            DFSGraphTraversal(node, visited, graph)

if __name__ == "__main__":
    graph = createGraph()
    DFSMain(graph)
