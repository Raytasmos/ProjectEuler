divisors = 0
triangle_number = 1
triangle_counter = 1

while divisors <= 500:
    for i in range(1, triangle_number + 1):
        if triangle_number % i != 0:
            continue
        else:
            divisors += 1
    if divisors <= 500:
        divisors = 0
        triangle_counter += 1
        triangle_number += triangle_counter
    print(f"Checked {triangle_number}")

print(triangle_number)
