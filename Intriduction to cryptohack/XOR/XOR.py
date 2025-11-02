text = "label"
key = 13

result = ''.join(chr(ord(c) ^ key) for c in text)
print(result)
 #Each character in the string "label" is XORed with the integer 13. The XOR operation flips bits where the key’s bits are 1, transforming the text. Converting the XORed values back to characters gives "aloha"