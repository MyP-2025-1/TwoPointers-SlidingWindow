# -*- coding: utf-8 -*-

def caesar(s, k):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = ""
    for x in s:
        i = ord(x)-ord("A")
        c += alphabet[(i-k) % len(alphabet)]
    return c

if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        k = int(input())
        print(caesar(s, k))
