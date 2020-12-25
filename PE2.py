final = 0
fibonacci = [1, 2]
index = -1
sum_list = []

while final < 4000000:
    index += 1
    final = fibonacci[index] + fibonacci[index + 1]
    if final < 4000000:
        fibonacci.append(final)

for index, value in enumerate(fibonacci):
    if value % 2 == 0:
        sum_list.append(value)

print(sum(sum_list))