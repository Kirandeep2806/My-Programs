#!/usr/bin/env python3

import numpy as np
from math import ceil

expr = input("Enter the expression : ")
size = ceil(len(expr)/2)

class Stack:
    def __init__(self, stackSize):
        self.tos = -1
        self.stackSize = stackSize
        self.stack = np.array([None]*size)

    def isOperator(self, op):
        if op == "^" or op == "/" or op == "*" or op == "%" or op == "+" or op == "-":
            return True
        return False
    
    def push(self, data):
        if self.isOperator(data):
            if data == "+":
                operation_res = self.stack[self.tos-1] + self.stack[self.tos]
            elif data == "-":
                operation_res = self.stack[self.tos-1] - self.stack[self.tos]
            elif data == "/":
                operation_res = self.stack[self.tos-1] / self.stack[self.tos]
            elif data == "*":
                operation_res = self.stack[self.tos-1] * self.stack[self.tos]
            elif data == "%":
                operation_res = self.stack[self.tos-1] % self.stack[self.tos]
            else:
                operation_res = self.stack[self.tos-1] ** self.stack[self.tos]
            self.pop()
            self.stack[self.tos] = operation_res
        else:
            self.tos += 1
            self.stack[self.tos] = int(data)

    def pop(self):
        if self.tos == -1:
            print("Stack Underflow")
        else:
            self.stack[self.tos] = None
            self.tos -= 1

    def getRes(self):
        return self.stack[self.tos]


s = Stack(size)
for i in expr:
    s.push(i)
print(s.getRes())