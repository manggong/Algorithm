'''
2058. 자릿수 더하기
'''

import sys

sys.stdin = open("2058_input.txt")

# N = list(map(int, input().split()))
N = int(input())

sum = 0
for i in range(0, 4):
    if N <= 0:
        break;
    j = N % 10
    N = int(N / 10)
    sum = sum + j
print(sum)
