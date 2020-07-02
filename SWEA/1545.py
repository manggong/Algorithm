"""
1545. 거꾸로 출력해 보아요
"""

import sys

sys.stdin = open("1545_input.txt")

N = int(input())
decrease = N
for i in range(0,N+1):
    decrease = N - i
    print( decrease,end=' ')