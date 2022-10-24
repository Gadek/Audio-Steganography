from scipy.io import wavfile
from my_crypto import *
from utils import *
import random

def read_from_file(path, last_bits, cipher_key, seed, secret_length):
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

    random.seed(seed)

    random_locations_key = sorted(random.sample(range(0, frames * channels), int(secret_length * 7 / last_bits)))

    revealed_data = reveal_data(stego_data_revealed, random_locations_key, last_bits)

    # Decrypt message
    bin_plaintext = decrypt_bin_message(int(cipher_key), revealed_data)
    # Convert message to string
    string_message = bin_list_to_string(bin_plaintext)
    print(string_message)
    return string_message



