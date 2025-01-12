import random
from helpers import get_prime_of_bit_length
from hashlib import sha256
from sympy import isprime

DSS_SETS_OF_LENGTH = {
    1: (1024, 160),
    2: (2048, 224),
    3: (2048, 256),
    4: (3072, 256),
}

WARNINGS = {
    'global_public_keys': 'You need to generate global public keys first.',
    'user_private_key': 'You need to generate user private key first.',
    'user_public_key': 'You need to generate user public key first.',
    'sign_message': 'You should sign the message first',
}


def set_global_public_key(set_index):
    global N
    (L, N) = DSS_SETS_OF_LENGTH[set_index]
    global p
    global q
    p = 0

    while not (isprime(p) and p.bit_length() == L):
        q = get_prime_of_bit_length(N)
        k = random.randint(2 ** (L - N - 1), 2 ** (L - N) - 1)
        p = (k * q) + 1

    global g
    g = 1

    while g <= 1:
        h = random.randint(2, p - 2)
        g = pow(h, k, p)


def get_user_private_key():
    if 'q' not in globals():
        raise Exception(WARNINGS['global_public_keys'])

    return random.randint(1, q - 1)


def get_user_public_key(private_key):
    if not ('g' in globals() and 'p' in globals()):
        raise Exception(WARNINGS['global_public_keys'])

    if private_key == 0:
        raise Exception(WARNINGS['user_private_key'])

    return pow(g, private_key, p)


def signing(message, private_key):
    if not ('g' in globals() and 'p' in globals() and 'q' in globals()):
        raise Exception(WARNINGS['global_public_keys'])

    if private_key == 0:
        raise Exception(WARNINGS['user_private_key'])

    r = 0
    s = 0

    while s == 0:
        k = random.randint(1, q - 1)
        r = pow(g, k, p) % q

        if r == 0:
            continue

        s = pow(k, -1, q) * (H(message) + private_key*r) % q

    return {'message': message, 'r': r, 's': s}


def verification(signed_message, public_key):
    if not ('g' in globals() and 'p' in globals() and 'q' in globals()):
        raise Exception(WARNINGS['global_public_keys'])

    if public_key == 0:
        raise Exception(WARNINGS['user_public_key'])

    if signed_message == {}:
        raise Exception(WARNINGS['sign_message'])

    (message, r, s) = (signed_message['message'], signed_message['r'], signed_message['s'])

    if not (0 < r < q and 0 < s < q):
        return False

    w = pow(s, -1, q)
    u1 = H(message) * w % q
    u2 = r * w % q
    v = pow(g, u1, p) * pow(public_key, u2, p) % p % q

    return v == r


def H(text):
    text_bytes = str.encode(text)
    hashed_bytes = sha256(text_bytes).digest()

    hashed = int.from_bytes(hashed_bytes, 'big')

    while hashed > pow(2, N):
        hashed = hashed // 2

    return hashed
