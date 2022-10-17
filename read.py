from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import sys
from my_crypto import *


def check_illegal_chars(text) -> list:
    ascii_message = [ord(a) for a in text]
    illegal_chars = [chr(ascii_char) for ascii_char in ascii_message if len(bin(ascii_char)[2:]) > 7]
    return illegal_chars

secret = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

#Check if secret message has illegal characters
illegal_chars = check_illegal_chars(secret)

if len(illegal_chars)>0:
    print("Error: Illegal characters:", ", ".join(illegal_chars), file=sys.stderr)
    exit(1)

wave_file_path = "C:\\Users\\rados\\Desktop\\udost\\audio-steganography\\example1.wav"
samplerate, data = wavfile.read(wave_file_path)
try:
    channels = data.shape[1]
except IndexError:
    channels = 1

# Print basic information about wave file
print(f"number of channels = {channels}")
frames = data.shape[0]
print(f"number of frames = {frames}")
length = frames / samplerate
print(f"length = {length}s")

# Check if provided wave file can store our secret message
if frames*channels < len(secret) * 7:
    print("Error: Secret is too long", file=sys.stderr)
    exit(1)


my_key = 2
bin_message = string_to_bin_list(secret)
bin_ciphertext = encrypt_bin_message(my_key, bin_message)


# time = np.linspace(0., length, frames)
#
# try:
#     for i in range(0,channels):
#         plt.plot(time, data[:, i], label=f"Channel {i}")
# except IndexError:
#     plt.plot(time, data[:], label="Channel")
# plt.legend()
# plt.xlabel("Time [s]")
# plt.ylabel("Amplitude")
# plt.show()




# Decrypt message
bin_plaintext = decrypt_bin_message(my_key, bin_ciphertext)

# Convert message to string
string_message = bin_list_to_string(bin_plaintext)
print(string_message)


