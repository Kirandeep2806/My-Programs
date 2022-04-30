from random import *
from math import *


class Node:
    def __init__(self, key, levels):
        self.key = key
        self.next = [None]*(levels+1)


class skiplist:
    def __init__(self, maxlevel, x):
        self.maxlevel = maxlevel
        self.header = Node(-1, self.maxlevel)
        self.x = x
        self.levels = 0

    def randomlevel(self):
        lvl = 0
        while(random() < self.x and lvl < self.maxlevel):
            lvl += 1
        return lvl

    def Insertion(self):
        key = int(input("Enter the value to be inserted: "))
        update = [None]*(self.maxlevel+1)
        ptr = self.header
        for i in range(self.levels, -1, -1):
            while ptr.next[i] and ptr.next[i].key < key:
                ptr = ptr.next[i]
            update[i] = ptr
        ptr = ptr.next[0]
        if ptr == None or ptr.key != key:
            newlevel = self.randomlevel()
            if newlevel > self.levels:
                for i in range(self.levels+1, newlevel+1):
                    update[i] = self.header
                self.levels = newlevel
            new = Node(key, self.levels)
            for i in range(newlevel+1):
                new.next[i] = update[i].next[i]
                update[i].next[i] = new

    def display(self):
        print("\n*****Skip List******")
        ptrd = self.header
        for i in range(self.levels+1):
            print("Elements at level "+str(i)+":", end=" ")
            node = ptrd.next[i]
            while(node != None):
                print(node.key, end=" ")
                node = node.next[i]
            print("\n")


n = int(input("Enter the no of elements to be inserted: "))
max = int(log(n, 2)+1)
l1 = skiplist(max, 0.5)
for i in range(n):
    l1.Insertion()
l1.display()
