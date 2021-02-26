"""
n번째 피보나치 수열의 값 구하기
"""


def solution(n):
    if n <= 1:
        return n
    return solution(n-2) + solution(n-1)


n = 7

print(solution(n))
