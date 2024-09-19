# -*- coding: utf-8 -*-
def alphabet_position(c):
    return ord(c) - 65

cases= int(input())
for i in range(cases):
    lines= int(input())
    hash= 0
    for j in range(lines):
        line= input()
        i= 0
        for c in line:
            hash+= alphabet_position(c) + j + i
            i+= 1
    print(hash)
