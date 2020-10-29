def gcd(a,b):
    i = min(a,b)
    while True:
        if a%i == 0 and b%i == 0:
            return i
        i = i-1

print(gcd(2,4))

# 둘 중에 작은 수를 뽑고 선정된 작은 수에서 -1을 하면서 공통으로 나눠 질 때 까지 루프를 돔