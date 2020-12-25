def palindrome(int_number):
    str_number = str(int_number)
    length = len(str_number)
    x = round(length / 2)

    # even
    if length % 2 == 0:
        if str_number[:x] == str_number[:x-1:-1]:
            return('True')
        else:
            return('False')

    # odd
    else:
        if str_number[:x] == str_number[:x:-1]:
            return('True')
        else:
            return('False')

greatest = 0

for i in range(500, 1000):
    for j in range(500, 1000):
        if palindrome(j*i) == 'True':
            if (j*i) > greatest:
                greatest = j*i

print(greatest)