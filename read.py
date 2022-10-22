from scipy.io import wavfile
import sys
from my_crypto import *
from utils import *
import random

def read_from_file(path, last_bits, cipher_key):
    samplerate, stego_data_revealed = wavfile.read(path)
    try:
        channels = stego_data_revealed.shape[1]
    except IndexError:
        channels = 1

    # Print basic information about wave file
    print(f"number of channels = {channels}")
    frames = stego_data_revealed.shape[0]
    print(f"samplerate = {samplerate}")
    print(f"number of frames = {frames}")
    length = frames / samplerate
    print(f"length = {length}s")

#tymaczasowo
    secret="qwerty"
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
    random.seed(110)

    random_locations_key = sorted(random.sample(range(0, frames * channels), int(len(padded_secret) * 7 / last_bits)))



    revealed_data = reveal_data(stego_data_revealed, random_locations_key, last_bits)
    # print(revealed_data)
    # Decrypt message
    bin_plaintext = decrypt_bin_message(int(cipher_key), revealed_data)

    # print(bin_plaintext)
    # Convert message to string
    string_message = bin_list_to_string(bin_plaintext)
    print(string_message)
    print()




