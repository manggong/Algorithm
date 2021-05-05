# 현재 나이트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 아스키로 바꿔서 인덱스 파악함 a부터 첫번째 컬럼

# 나이트가 이동할 수 있는 방법들
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인 함

answer = 0

for step in steps:
    # 이동하고자 하는 위치 확인
        next_row = row + step[0]
        next_column = column + step[1]
        # 해당 위치로 이동이 가능하다면 카운트를 증가
        if next_row >= 1 and next_column <= 8 and next_column >= 1 and next_column <= 8:
            answer += 1
print(answer)