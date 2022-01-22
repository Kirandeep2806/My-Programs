#!/usr/bin/python3

# Put the text u desire in the main.txt file

with open("main.txt") as file:
    def patternMatching(string, key):
        found = False
        for string_start in range(len(string)-len(key)+1):
            temp = string_start
            start = 0
            for i in range(temp, temp+len(key)):
                if string[i] != key[start]:
                    break
                start += 1
            else:
                print(f"Pattern found from index {temp}-{temp+len(key)-1}")
                found = True
        if not found:
            print("Element not found")
key = input("Enter the pattern to be matched : ")
patternMatching(file.read(), key)
