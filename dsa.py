import random
from helpers import get_prime_of_bit_length

DSS_sets_of_length = [
    (128, 16),
    (1024, 160),
    (2048, 224),
    (2024, 256),
    (3072, 256)
]


def set_global_public_key():
    global N
    # (L, N) = random.choice(DSS_sets_of_length)
    (L, N) = DSS_sets_of_length[0]
    global p
    global q
    p = 0
    q = 0

    p_list = []
    q_list = []

    p_list.append(get_prime_of_bit_length(L))

    while p == 0:
        # Try q
        q_candidate = get_prime_of_bit_length(N, q_list)

        for p_candidate in p_list:
            if (p_candidate - 1) % q_candidate == 0:
                p = p_candidate
                q = q_candidate
                break

        if p != 0:
            break

        q_list.append(q_candidate)

        # Try p
        p_candidate = get_prime_of_bit_length(L, p_list)

        for q_candidate in q_list:
            if (p_candidate - 1) % q_candidate == 0:
                p = p_candidate
                q = q_candidate
                break

        p_list.append(p_candidate)

    # h = random.randint(2, p - 2)
    h = 2
    g_candidate = pow(h, int((p - 1) / q), p)

    while g_candidate <= 1:
        h = random.randint(2, p - 2)
        g_candidate = pow(h, int((p - 1) / q), p)

    global g
    g = g_candidate


def get_user_private_key():
    return random.randint(1, q - 1)


def get_user_public_key(private_key):
    return pow(g, private_key, p)


def signing(message, private_key):
    r = 0
    s = 0

    while s == 0:
        k = random.randint(1, q - 1)
        r = pow(g, k, p) % q

        if r == 0:
            continue

        s = (hash_N(message) + private_key*r) / k % q

    return message, r, s


def verification(signed_message, public_key):
    (message, r, s) = signed_message

    if not (0 < r < q and 0 < s < q):
        return False

    w = 1 / s % q
    u1 = hash_N(message) * w % q
    u2 = r * w % q
    v = pow(g, u1) * pow(public_key, u2) % p % q

    return v == r


def hash_N(text):
    hashed = hash(text)

    while hashed > pow(2, N):
        hashed = hashed // 2

    return hashed
