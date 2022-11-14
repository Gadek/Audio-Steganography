from scipy.io import wavfile
from my_crypto import *
from utils import *
from padding import gen_padding
import random

import aes

def read_from_file(path, last_bits, cipher_key, seed, secret_length):
    # secret_length might be longer because of padding
    secret_length += len(gen_padding(secret_length, last_bits))

    # add aes padding len
    aes_padding_len = 16 - secret_length % 16
    
    if aes_padding_len == 0:
        aes_padding_len += 16
    
    secret_length += aes_padding_len

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

    random_locations_key = sorted(random.sample(range(0, frames * channels), int(secret_length * 8 / last_bits)))

    revealed_data = reveal_data(stego_data_revealed, random_locations_key, last_bits)
    
    # Convert message to bytes
    encrypted_message = bin_list_to_bytes(revealed_data)

    # Decrypt message
    string_message = aes.decrypt(encrypted_message, cipher_key)
    
    print(string_message)
    return string_message
