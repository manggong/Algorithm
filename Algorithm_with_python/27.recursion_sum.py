def solution(n):
    while n == 0:
        return 0
    return solution(n-1) + n


n = 10

print(solution(10))
