from pwn import *

KEY1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
KEY2 = xor(KEY1,bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'))
KEY3 = xor(KEY2,bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'))
flag = xor(KEY3,xor(KEY1,xor(KEY2,bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'))))

print(flag)

#so what i did was i first decoded KEY1 from hex into bytes
#then i recovered KEY2 by XORing KEY1 with the provided (KEY2 ^ KEY1) value
#then i did the same with KEY3
#so for my final steps what i did was that , i reovered flag by XORing together the chain (FLAG ^ KEY1 ^ KEY3 ^ KEY2) with
#KEY1 , KEY2 and KEY3 ,Because XOR is associative/commutative and self inverting , the repeated keys cancel out and leave the flag