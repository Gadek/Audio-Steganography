def gen_padding(secret_len, last_bits):
    b = (secret_len * 8) % last_bits
    # print(b)
    j = 0
    for i in range(0, 100):
        if (last_bits * i - b) % 8 == 0:
            j = i
            break

    x = int((last_bits * j - b) / 8)
    padding = "@" * x

    return padding
