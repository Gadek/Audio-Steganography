import wave

def set_bit(v, index, x):
  """Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value."""
  mask = 1 << index   # Compute mask, an integer with just bit 'index' set.
  v &= ~mask          # Clear the bit indicated by the mask (if x is False)
  if x:
    v |= mask         # If x was True, set the bit indicated by the mask.
  return v            # Return the result, we're done.

secret="qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
secret_bin=""
wav = wave.open("sample3.wav", 'rb')
bit_depth = wav.getsampwidth() * 8
print(bit_depth)
print(wav.getparams())
for a in range(10006,10007):
    wav.setpos(a)
    print(wav.readframes(1)[0])
    print(wav.readframes(1)[1])
    print(wav.readframes(1)[2])
    print(wav.readframes(1)[3])
    print(f'{(wav.readframes(1)[0]):0>8b}', end=' ')
    print(f'{(wav.readframes(1)[1]):0>8b}', end=' ')
    print(f'{(wav.readframes(1)[2]):0>8b}', end=' ')
    print(f'{(wav.readframes(1)[3]):0>8b}', end=' ')




val = 15
print()
print(bin(val))
val = set_bit(val,0,0)
val = set_bit(val,1,0)
print(bin(val))
