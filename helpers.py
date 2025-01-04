import random


def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i*i <= n:
        print('checking ' + str(i))

        if n % i == 0:
            print('divisor: ' + str(i))
            return False

        i += 2

    print('is prime')
    return True


def get_prime_of_bit_length(n):
    checked = []

    while True:
        x = random.randint(2**(n - 1) + 1, 2**n - 1)

        if x in checked:
            continue

        print(x)

        if is_prime(x):
            return x

        checked.append(x)


def get_prime_of_bit_length_that_divides(n, p):
    checked = []

    while True:
        x = random.randint(2**(n - 1) + 1, 2**n - 1)

        if x in checked:
            continue

        print(x)

        if p % x == 0 and is_prime(x):
            return x

        checked.append(x)
