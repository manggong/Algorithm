def find_max(numbers):
    maxNumber = numbers[0]
    for i in range(1,len(numbers)):
        if maxNumber < numbers[i]:
            maxNumber = numbers[i]
    return maxNumber


print(find_max([4,5,6,7,8]))
