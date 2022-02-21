#!/usr/bin/python3

v = int(input("Enter the number of vertices: "))
graph = [[0 for __ in range(v)] for _ in range(v)]

for i in range(v):
    edge = list(map(int, input(f"Enter the {i} matrix data : ").split()))
    graph[i] = edge

def DFS(currNode, graph, visited=set()):
    visited.add(currNode)
    print(currNode, end=" ")
    for pos,i in enumerate(graph[currNode]):
        if i and (pos not in visited):
            DFS(pos, graph, visited)

DFS(0, graph)
