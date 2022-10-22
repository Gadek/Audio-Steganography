from scipy.io import wavfile
import sys
from my_crypto import *
from utils import *
import random

def write_to_file(path_src, path_dst, last_bits, cipher_key, secret):
    print(path_src)
    print(path_dst)
    print(last_bits)
    print(cipher_key)
    print(secret)
    # last_bits = 1
    # secret = "qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM" * 300
    # secret = "1"
    b = (len(secret) * 7) % last_bits
    print(b)
    j = 0
    for i in range(0, 100):
        if (last_bits * i - b) % 7 == 0:
            j = i
            break

    x = int((last_bits * j - b) / 7)
    padding = "@" * x
    padded_secret = secret + padding
    print(len(padded_secret) % 7)
    # Check if secret message has illegal characters
    illegal_chars = find_illegal_chars(padded_secret)

    if len(illegal_chars) > 0:
        print("Error: Illegal characters:", ", ".join(illegal_chars), file=sys.stderr)
        exit(1)

    # path_src = "C:\\Users\\rados\\Desktop\\udost\\audio-steganography\\sinwave1.wav"
    samplerate, data = wavfile.read(path_src)

    # Make sure data type is compatible
    # if type(data[0][0]) not in [np.int16, np.int32, np.uint8]:
    #     print("Error: Data type of wave file is incompatible", file=sys.stderr)
    #     exit(1)

    try:
        channels = data.shape[1]
    except IndexError:
        channels = 1

    # Print basic information about wave file
    print(f"number of channels = {channels}")
    frames = data.shape[0]
    print(f"samplerate = {samplerate}")
    print(f"number of frames = {frames}")
    length = frames / samplerate
    print(f"length = {length}s")

    # Check if provided wave file can store our secret message
    if frames * channels * last_bits < len(padded_secret) * 7:
        print("Error: Secret is too long", file=sys.stderr)
        exit(1)

    cipher_key = 6
    bin_message = string_to_bin_list(padded_secret)
    bin_ciphertext = encrypt_bin_message(cipher_key, bin_message)
    random.seed(110)

    random_locations_key = sorted(random.sample(range(0, frames * channels), int(len(padded_secret) * 7 / last_bits)))
    # print(random_locations_key)
    multiplier_key = 100000
    stego_data = hide_data(data, bin_ciphertext, random_locations_key, last_bits, channels)
    # plot(length, samplerate, stego_data, channels)

    # path_dst = "C:\\Users\\rados\\Desktop\\udost\\audio-steganography\\stego1.wav"
    wavfile.write(path_dst, samplerate, stego_data.astype(np.int16))

    samplerate, stego_data_revealed = wavfile.read(path_dst)

    revealed_data = reveal_data(stego_data_revealed, random_locations_key, last_bits)
    # print(revealed_data)
    # Decrypt message
    bin_plaintext = decrypt_bin_message(cipher_key, revealed_data)

    # print(bin_plaintext)
    # Convert message to string
    string_message = bin_list_to_string(bin_plaintext)
    print(string_message)
    print()