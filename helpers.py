import sympy

def get_prime_of_bit_length(n):
    candidate_min = 2**(n - 1) + 1
    candidate_max = 2**n - 1
    candidate = sympy.randprime(candidate_min, candidate_max + 1)

    return candidate