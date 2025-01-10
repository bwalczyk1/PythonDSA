import sympy

def get_prime_of_bit_length(n, excluding = []):
    candidate_min = 2**(n - 1) + 1
    candidate_max = 2**n - 1
    candidate = sympy.randprime(candidate_min, candidate_max + 1)

    while candidate in excluding:
        candidate = sympy.nextprime(candidate)

        if candidate > candidate_max:
            candidate = sympy.nextprime(candidate_min - 1)

    return candidate