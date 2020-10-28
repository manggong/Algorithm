def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
    return fact

print(factorial(3))