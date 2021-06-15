A, B, V = map(int,(input().split()))
hap = 0
cnt = 0

while(True):
    hap += A
    cnt += 1
    if hap >= V:
      print(cnt)
      break
    else:
        hap -= B