def prime(num):
    if num == 1:
        return False
    else:
        limit = round(num/2)
        x = [i for i in range(1, limit + 1) if num % i == 0]

        if 1 in x:
            x.remove(1)

        return True if x == [] else False

prime_list = [2]
i = 3

while len(prime_list) != 10001:
    if prime(i) is True:
        prime_list.append(i)
        print(len(prime_list))
    i += 2

print(max(prime_list))