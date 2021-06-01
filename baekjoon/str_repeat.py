n = int(input())

for _ in range(n):
    R, S = input().split()
    for x in S:
        print(x*int(R), end='')
    print()