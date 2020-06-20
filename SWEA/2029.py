count = int(input())
 
for i in range(1,count+1):
	a, b = list(map(int, input().split()))
	mok, rest = int(a/b), int(a%b)
	print("#"+str(i), mok, rest)