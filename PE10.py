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
difference = 0

for i in range(1, 2000000, 2):
    if prime(i):
        prime_list.append(i)
        print(f'Adding {i}')