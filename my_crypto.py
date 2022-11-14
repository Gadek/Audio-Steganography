def string_to_bin_list(text: str|bytes) -> list:
    '''Convert a string to an array of ascii characters in binary format'''

    if isinstance(text, str):
        text = bytes(text, 'utf-8')

    # [113, 119, 101, 114, 116]
    ascii_message = [a for a in text]
    # ['1110001', '1110111', '1100101', '1110010', '1110100']
    bin_ascii_message = [f'{bin(ascii_char)[2:]:0>8}' for ascii_char in ascii_message]
    return bin_ascii_message

def bin_list_to_bytes(bin_message: list) -> bytes:
    '''Convert an array of ascii characters in binary format to a string'''

    output_bytearray = bytearray()
    
    for bin_char in bin_message:
        binary_int = int(bin_char, 2)
        output_bytearray.append(binary_int)
    
    return bytes(output_bytearray)
