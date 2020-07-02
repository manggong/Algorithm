'''
2019. 더블더블
'''

import sys

sys.stdin = open("2019_input.txt")

N = int(input())

for i in range(0,N+1):
    print(2**i, end=' ')