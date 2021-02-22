"""
재귀로 배열의 최댓값 구하기
"""


def solution(arr, n):
    if n == 1:
        return arr[0]
    find_max = solution(arr, n-1)
    if find_max > arr[n-1]:
        return find_max
    else:
        return arr[n-1]


arr = [15, 656, 78, 13, 45, 78, 266]

print(solution(arr, len(arr)))
