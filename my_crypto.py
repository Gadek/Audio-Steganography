def string_to_bin_list(text: str) -> list:
    '''Convert a string to an array of ascii characters in binary format'''

    # [113, 119, 101, 114, 116]
    ascii_message = [ord(a) for a in text]
    # ['1110001', '1110111', '1100101', '1110010', '1110100']
    bin_ascii_message = [f'{bin(ascii_char)[2:]:0>7}' for ascii_char in ascii_message]
    return bin_ascii_message


def encrypt_bin_message(key, bin_plaintext: list) -> list:
    '''Do simple transposition cipher'''

    ciphertext = []
    for bin_char in bin_plaintext:
        ciphertext.append(bin_char[key:]+bin_char[:key])
    return ciphertext


def decrypt_bin_message(key, ciphertext: list) -> list:
    decypher_key = 7-key
    plaintext = []
    for bin_char in ciphertext:
        plaintext.append(bin_char[decypher_key:]+bin_char[:decypher_key])
    return plaintext


def bin_list_to_string(bin_message: list) -> str:
    '''Convert an array of ascii characters in binary format to a string'''

    output_string = ""
    for bin_char in bin_message:
        binary_int = int(bin_char, 2)
        output_string += chr(binary_int)
    return output_string

