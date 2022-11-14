import numpy as np
import matplotlib.pyplot as plt
def set_LSB(value: str, bits: str) -> str:
    '''Sets given bits on least significant bits'''
    return value[:len(value) - len(bits)] + bits


def find_illegal_chars(text) -> list:
    ascii_message = [ord(a) for a in text]
    illegal_chars = [chr(ascii_char) for ascii_char in ascii_message if len(bin(ascii_char)[2:]) > 8]
    return illegal_chars

def ciphertext_ready(bin_ciphertext, last_bits):
    bin_ciphertext_to_enumerate_help = "".join(bin_ciphertext)
    bin_ciphertext_to_enumerate = []
    for i in range(0,len(bin_ciphertext_to_enumerate_help),last_bits):
        bin_ciphertext_to_enumerate.append(bin_ciphertext_to_enumerate_help[i:i+last_bits])
    return bin_ciphertext_to_enumerate

def hide_data(data, bin_ciphertext, random_locations_key, last_bits, channels):
    bin_ciphertext_to_enumerate = ciphertext_ready(bin_ciphertext, last_bits)
    # print("bin ciphertext ready", bin_ciphertext_to_enumerate)
    flatten_list = data.flatten()

    for i, (location, bits) in enumerate(zip(random_locations_key, bin_ciphertext_to_enumerate)):
        val = flatten_list[location]
        sign = -1 if val<0 else 1
        bin_val = bin(val)[2:].strip('b')
        new_bin_val = set_LSB(bin_val, bits)
        new_val = int(new_bin_val,2)*sign
        # print(bin_val,bits,new_bin_val)
        flatten_list[location] = new_val

    return np.reshape(flatten_list, (-1,channels))

def reveal_data(data, random_locations_key, last_bits):
    flatten_list = data.flatten()
    output_string = ""
    output_list = []
    for i, location in enumerate(random_locations_key):
        val = flatten_list[location]
        string_val_bin = bin(val)[2:].strip('b')
        # print("string_val_bin:", string_val_bin)
        output_string += string_val_bin[len(string_val_bin)-last_bits:]
        # print("string_val_bin[len(string_val_bin)-last_bits:]:", string_val_bin[len(string_val_bin)-last_bits:])

    for i in range(0,len(output_string),8):
        output_list.append(output_string[i:i+8])
        # print(output_string[i:i+8])

    return output_list

def plot(length, samplerate, data, channels):
    frames = int(samplerate * length)
    time = np.linspace(0., length, frames)
    # try:
    #     for i in range(0,channels):
    #         plt.plot(time, data[:, i], label=f"Channel {i}")
    # except :
    #     plt.plot(time, data[:], label="Channel")
    if channels>1:
        for i in range(0, channels):
            plt.plot(time, data[:, i], label=f"Channel {i}")
    else:
        plt.plot(time, data, label="Channel")

    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()