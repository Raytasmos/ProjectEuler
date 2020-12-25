def smalldiv(num):
    test = num
    while True:
        for i in range(2, num + 1):
            if test % i != 0:
                break
        else:
            return f'Smallest dividend = {test}'
        test += num

print(smalldiv(20))