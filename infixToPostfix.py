#!/usr/bin/env python3

import numpy as np
from math import ceil

expr = "(" + input("Enter the expression : ") + ")"
size = ceil(len(expr)/2)

class Stack:
    def __init__(self, stackSize):
        self.tos = -1
        self.stackSize = stackSize
        self.stack = np.array([None]*size)
        self.postfixExpr = ""
    
    def precedence(self, op):
        if op == "^":
            return 3
        elif op == "/" or op == "*" or op == "%":
            return 2
        elif op == "+" or op == "-":
            return 1
        else:
            return 0

    def isOperator(self, op):
        if op == "^" or op == "/" or op == "*" or op == "%" or op == "+" or op == "-":
            return True
        return False
    
    def push(self, data):
        if data == "(":
            self.tos += 1
            self.stack[self.tos] = data
        
        elif data == ")":
            while self.stack[self.tos] != "(":
                self.pop()
            self.stack[self.tos] = None
            self.tos -= 1

        elif self.isOperator(data) and self.precedence(data) > (self.precedence(self.stack[self.tos]) or 0):
            self.tos += 1
            self.stack[self.tos] = data

        elif self.isOperator(data) and self.precedence(data) <= (self.precedence(self.stack[self.tos]) or 0):
            while self.precedence(self.stack[self.tos]) >= self.precedence(data):
                self.pop()
            self.tos += 1
            self.stack[self.tos] = data

        else:
            self.postfixExpr += data
            
            
    def pop(self):
        if self.tos == -1:
            print("Invalid Expression!")
            quit(0)
        else:
            self.postfixExpr += self.stack[self.tos]
            self.stack[self.tos] = None
            self.tos -= 1

    def getPostFixExpr(self):
        if self.tos == -1:
            return self.postfixExpr
        else:
            return "Invalid Expression!"


s = Stack(size)
for i in expr:
    s.push(i)
    
print(s.getPostFixExpr())