#!/usr/bin/python3

from collections import defaultdict
from typing import List

def defaultValueOfGraph() -> List:
    return []

def createGraph():
    graph = defaultdict(defaultValueOfGraph) # This can also be replace with defaultdict(list)

    # Programmed in a way that the nodes are of numeric type i.e., 1,2,3,4,......
    for i in range(1, int(input("Enter the no.of nodes you are having : "))+1):
        graph[i] = list(map(int, input("Enter the adjacent nodes of node {} : ".format(i)).split()))

    return graph

if __name__ == "__main__":
    g = createGraph()
    print(g)
