import math

def factors(num):
    limit = round(num/2)
    x = []
    for i in range(1, limit + 1):
        if num % i == 0:
            x.append(i)
    x.append(num)

    return x

def prime(num):
    x = factors(num)
    if 1 in x:
        x.remove(1)

    return True if x == [num] else False

def primefactors(num):
    x = []
    for i in range(1, round(math.sqrt(num))):
        if num % i == 0:
            if prime(i) is True:
                x.append(i)

    return x

print(max(primefactors(600851475143)))