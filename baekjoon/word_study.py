words = input().upper()
word_list = list(set(words))
cnt_list = []

for x in word_list:
    cnt = words.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1: # 제일 큰수가 1개를 초과 한다면,
    print('?')
else:
    max_number_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(word_list[max_number_index])