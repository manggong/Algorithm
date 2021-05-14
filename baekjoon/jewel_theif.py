import sys
import heapq
N, K = map(int, sys.stdin.readline().split())

jewels = []
bags = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())   # 무게, 가격
    heapq.heappush(jewels, (M, V))
for _ in range(K):
    heapq.heappush(bags, int(sys.stdin.readline()))

res = 0
jewels_able = []

while bags:
    bag = heapq.heappop(bags)

    while jewels and bag >= jewels[0][0]:
        heapq.heappush(jewels_able, -heapq.heappop(jewels)[1])
		# print(jewels_able)
        
    if jewels_able:
        res += -(heapq.heappop(jewels_able))
    elif not jewels:
        break

print(res)