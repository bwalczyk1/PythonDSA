import dsa

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dsa.set_global_public_key()
    private_key = dsa.get_user_private_key()
    public_key = dsa.get_user_public_key(private_key)

    signed_message = dsa.signing('ALA MA KOTA', private_key)
    print(dsa.verification(signed_message, public_key))
