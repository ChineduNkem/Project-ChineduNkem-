from pwn import xor


flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

print(xor(flag, 'crypto{'.encode()))   # -> reveals the repeating key (or a hint of it)
print(xor(flag, 'myXORkey'.encode()))  # -> prints the decrypted plaintext (the flag)
