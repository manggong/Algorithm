n = int(input())

count = 0

bag_types = [5,3]

for bag in bag_types:
    count += n // bag
    n %= bag

print(count)