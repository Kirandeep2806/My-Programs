#!/usr/bin/python3

v = int(input("Enter the number of vertices: "))
graph = [[0 for __ in range(v)] for _ in range(v)]

for i in range(v):
    edge = list(map(int, input(f"Enter the {i} matrix data : ").split()))
    graph[i] = edge

def BFS(currNode, graph):
    visited = set()
    queue = []
    queue.append(currNode)
    visited.add(currNode)
    print(currNode, end=" ")
    while queue:
        head = queue.pop(0)
        for pos, i in enumerate(graph[head]):
            if i and (pos not in visited):
                queue.append(pos)
                visited.add(pos)
                print(pos, end=" ")

BFS(0, graph)
