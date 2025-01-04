import random
import helpers

DSS_sets_of_length = [
    (1024, 160),
    (2048, 224),
    (2024, 256),
    (3072, 256)
]


def set_global_public_key():
    # (L, N) = random.choice(DSS_sets_of_length)
    (L, N) = DSS_sets_of_length[0]
    global p
    p = helpers.get_prime_of_bit_length(L)
    global q
    q = helpers.get_prime_of_bit_length_that_divides(N, p - 1)

    for h in range(2, p - 1):
        if h**((p-1)/q) % p > 1:
            global g
            g = h*(p - 1)/q % p
            break


def get_user_private_key():
    return random.randint(1, q - 1)


def get_user_public_key(private_key):
    return g**private_key % p


def signing(message, private_key):
    k = random.randint(1, q - 1)
    r = (g**k % p) % q
    s = (k**-1 * (hash(message) + private_key*r)) % q

    return message, r, s


def verification(signed_message, public_key):
    (message_prim, r_prim, s_prim) = signed_message
    w = s_prim**-1 % q
    u1 = (hash(message_prim) * w) % q
    u2 = r_prim*w % q
    v = ((g*u1*public_key*u2) % p) % q

    return r_prim == v
