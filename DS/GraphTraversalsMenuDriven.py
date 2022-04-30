#!/usr/bin/python3

from BFSGraph import BFSGraphTraversal
from DFSGraph import DFSMain
from createGraph import createGraph

graph = createGraph()
while True:
    choice = int(input("1.DFS\t2.BFS\t3.Exit\nChoose one :"))
    if choice == 1:
        print("DFS graph traversal :", end=" ")
        DFSMain(graph)
        print()
    elif choice == 2:
        print("BFS graph traversal :", end=" ")
        BFSGraphTraversal(__import__("random").randint(1,len(graph)), graph)
        print()
    else:
        exit(0)
