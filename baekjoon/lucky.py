n = input()
length = len(n)
hap = 0

for i in range(length // 2):
    hap += int(n[i])

for j in range(length // 2, length):
    hap -= int(n[j])

if hap == 0:
    print('LUCKY')
else:
    print('READY')