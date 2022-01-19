#!/usr/bin/python3

from createGraph import createGraph

graph = createGraph()
queue = []

# No recursion is required cz we will traverse in a level like manner

def BFSGraphTraversal(currNode):
    visited = set()
    queue.append(currNode)
    print(currNode, end=" ")
    visited.add(currNode)
    while queue:
        front = queue.pop(0)
        for node in graph[front]:
            if node not in visited:
                visited.add(node)
                queue.append(node)
                print(node, end=" ")

BFSGraphTraversal(__import__("random").randint(1,len(graph)))
