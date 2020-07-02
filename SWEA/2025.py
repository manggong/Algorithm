"""
2025. N줄덧셈
"""

import sys

sys.stdin = open("2025_input.txt")

N = int(input())

hap = 0
for i in range(1,N+1):
    hap += i
print(hap)