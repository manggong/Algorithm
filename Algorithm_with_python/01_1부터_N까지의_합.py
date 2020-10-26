def solution(number):
    hap = 0
    for i in range(1,number+1):
        hap = hap + i
    return hap

print(solution(100))