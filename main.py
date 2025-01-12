import dsa

if __name__ == '__main__':
    private_key = 0
    public_key = 0
    signed_message = {}

    print('DSA demo')

    while True:
        print('1. Generate global public keys')
        print('2. Generate user private key')
        print('3. Generate user public key')
        print('4. Sign message')
        print('5. Verify signed message')

        match input():
            case '1':
                print('Choose set of lengths (L, N) from recommended sets:')
                print(dsa.DSS_SETS_OF_LENGTH)
                set_index = int(input())

                if set_index not in dsa.DSS_SETS_OF_LENGTH:
                    print('Improper choice')
                    continue

                dsa.set_global_public_key(set_index)
                print('Global public keys generated')

            case '2':
                try:
                    private_key = dsa.get_user_private_key()
                    print('User private key generated')
                except Exception as e:
                    print(e)

            case '3':
                try:
                    public_key = dsa.get_user_public_key(private_key)
                    print('User public key generated')
                except Exception as e:
                    print(e)

            case '4':
                try:
                    signed_message = dsa.signing(input('Message: '), private_key)
                    print('Signed message:')
                    print(signed_message)
                except Exception as e:
                    print(e)

            case '5':
                try:
                    if dsa.verification(signed_message, public_key):
                        print('Message verified')
                    else:
                        print('Message not verified')
                except Exception as e:
                    print(e)

            case _ :
                break
