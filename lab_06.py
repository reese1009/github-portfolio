def encode(password):
    en_pass = ""  # string

    for char in password:  # encodes individual digits into int
        en_pass = en_pass + str((int(char) + 3) % 10)  # shifts digits 3

    return en_pass


def decode(encoded_password):
    decoded_pass = ""
    for char in encoded_password:
        decoded_pass = decoded_pass + str((int(char) - 3) % 10)
        # 3 digit shift

    return decoded_pass


if __name__ == "__main__":
    function = True

    while function:
        print('Menu')
        print('-' * 13)
        print('1. Encode\n2. Decode\n3. Exit')
        option = int(input('\nPlease enter an option: '))

        if option == 1:  # encode password
            print('Please enter your password to encode: ', end='')
            password = input()
            encoded_password = (encode(password))
            print('Your password has been encoded and stored!\n')

        if option == 2:  # decode password
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {password}.\n')

        if option == 3:  # end the loop
            break
