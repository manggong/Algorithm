def factorial2(number):
    if number <= 1:
        return 1
    return number * (number - 1)


print(factorial2(3))
