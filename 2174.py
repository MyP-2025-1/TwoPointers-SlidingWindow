# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(input())
    captured = set()
    for x in range(n):
        captured.add(input())
    missing = 151 - len(captured)
    print(f"Falta(m) {missing} pomekon(s).")
