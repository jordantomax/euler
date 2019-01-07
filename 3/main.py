max = 600851475143


def find_biggest_prime(num):
    factor = 2

    while num > factor:
        if num % factor == 0:
            num = num / factor
        else:
            factor += 1
    return factor


result = find_biggest_prime(max)
print(result)
