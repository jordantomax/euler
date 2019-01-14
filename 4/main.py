def is_palindrome(num):
    stringified = str(num)
    length = len(stringified)

    for i in range(length / 2):
        if stringified[i] != stringified[(-1 * i) - 1]:
            return False
    return True


# examples
# 999 999
# 998 999
# 998 998
# 997 998


def find_largest_palindrome_of_2_multiples(digits):
    multiple = int(digits * "9")
    range_length = int("9" + ((digits - 1) * "0"))
    palindrome = 0

    for i in reversed(range(multiple + 1)):
        for j in reversed(range(i + 1)):
            product = i * j

            if product < palindrome:
                break
            elif is_palindrome(product):
                palindrome = product

    return palindrome


result = find_largest_palindrome_of_2_multiples(3)
print(result)
