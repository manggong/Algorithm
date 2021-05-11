n = int(input())
times = sorted(list(map(int, input().split())))

hap = 0
prev_hap = 0

for time in times:
    prev_hap += time
    hap += prev_hap
print(hap)