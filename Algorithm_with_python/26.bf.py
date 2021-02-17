"""
n명 중 2명을 뽑아 짝을 만드는 알고리즘
"""


def solution(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print(arr[i], "-", arr[j])


arr = ['yang', 'kim', 'sol']

solution(arr)
