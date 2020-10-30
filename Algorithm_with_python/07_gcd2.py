def gcd2(a,b):
    if b == 0:
        return a
    return gcd2(b,a%b)

print(gcd2(16,12))

# 나머지 연산은 두 수의 MIN 값을 구하지 않아도 똑같이 나옴