start, term, end = map(int, input().split())

answer = start

for i in range(start, end):
    answer += term
print(answer)