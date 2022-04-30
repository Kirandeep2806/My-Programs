#!/usr/bin/python3

size = ["SMALL", "NORMAL", "HUGE"]

[print(size[(int(input())+1)%3]) for _ in range(int(input()))]
