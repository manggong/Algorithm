n = input()
b = int(n, 16)

temp = 0
for i in range(1,16):
    temp = b*i
    print("B*{0:X}={1:X}".format(i,temp))