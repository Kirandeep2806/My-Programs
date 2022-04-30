#!/usr/bin/python3

from createGraph import createGraph

# No recursion is required cz we will traverse in a level like manner
queue = []

def BFSGraphTraversal(currNode, graph):
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

if __name__ == "__main__":
    graph = createGraph()
    BFSGraphTraversal(__import__("random").randint(1,len(graph)), graph)
