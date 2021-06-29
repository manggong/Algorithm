data = input()

answer = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or answer <=1:
        answer += num # 0, 1 이면 더함
    else:
        answer *= num
print(answer)