import math

def abs_sign(a):
    if a>=0:
        return a
    else:
        return -a

def abs_squrae(a):
    b = a*a
    return math.sqrt(b)

print(abs_sign(5))
print(abs_squrae(25))