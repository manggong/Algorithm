N = input()

numbers = list(map(int,N))

separate = int(N) - (max(numbers) * len(numbers))

if separate < 0:
    print(0)
else:
    print(separate)