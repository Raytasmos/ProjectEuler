from math import sqrt

def prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(2, round(sqrt(num)) + 1):
            if num % i == 0:
                return False
        else:
            return True

def primes(num):
    primes_list = [i for i in range(3, num + 1, 2)]
    primes_list.insert(0, 2)

    for index, value in enumerate(primes_list):

        if value == 0:
            continue

        elif not prime(value):
            primes_list[index] = 0

        elif prime(value):
            for index_j, value_j in enumerate(primes_list[index:]):
                    if value_j % value == 0:
                        primes_list[index_j] = 0

    primes_list = [i for i in primes_list if i != 0]

    return primes_list

print(sum(primes(2000000)))
