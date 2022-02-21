#!/usr/bin/python3

s = input("Enter a string : ")
subStr = input("Enter the string to be searched : ")

def generateHash(string, mod=13):
    strLen = len(string)
    hash = 0
    for pos, substr in enumerate(string):
        hash += ord(substr)*10**(strLen-pos-1)
    return hash % mod

def patternMatching(string, key, mod=13):
    hash = generateHash(string[0:len(key)], mod)
    keyHash = generateHash(key, mod)
    print("Keyhash", keyHash, "Hash", hash)
    if hash == keyHash:
        print(f"Pattern found at index 0")
    else:
        for i in range(len(string)-len(key)):
            hash = ((hash - ord(string[i])*10**(len(key)-1))*10 + ord(string[i+len(key)])) % mod
            # print(string[i+1:i+len(key)+1], hash)
            if hash == keyHash:
                if string[i+1:i+len(key)+1] == key:
                    print(f"Pattern found at index {i+1}")
                    break
        else:
            print("Element not found")

patternMatching(s, subStr)
