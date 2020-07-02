"""
1933. 간단한 N의 약수
"""

import sys

sys.stdin = open("1933_input.txt")

N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i, end=' ')

