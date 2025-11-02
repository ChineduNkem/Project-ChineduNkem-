cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cipher = bytes.fromhex(cipher_hex)

for key in range(256):
    decoded = bytes([b ^ key for b in cipher])
    if b"crypto" in decoded:
        print(decoded)
        break
