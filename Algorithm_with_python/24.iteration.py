def solution(n):
    hap = 0
    for i in range(1, n+1):
        hap += i * i
    return hap


def solution2(n):
    return n*(n+1)*(n*2+1)/6
    # return n * 2


n = 10

print(solution2(n))
