import wave

secret="qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
secret_bin=""
wav = wave.open("sample3.wav", 'rb')
bit_depth = wav.getsampwidth() * 8
print(bit_depth)
print(wav.getparams())
for a in range(10006,10007):
    wav.setpos(a)
    print(wav.readframes(1))
    print(f'{(wav.readframes(1)[0]):0>8b}', end=' ')
    print(f'{(wav.readframes(1)[1]):0>8b}', end=' ')
    print(f'{(wav.readframes(1)[2]):0>8b}', end=' ')
    print(f'{(wav.readframes(1)[3]):0>8b}', end=' ')
