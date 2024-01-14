import sys
import base64
import re
from Crypto.Util.number import *
from pwn import *

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

# ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
# print("Here is your flag:")
# print("".join(chr(o ^ 0x32) for o in ords))

# ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
# print("".join(chr(o) for o in ords))

# hex_str = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
# decd = bytes.fromhex(hex_str)
# print("".join(chr(o) for o in decd)) # hex()

# hex_str = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
# bytes_data = bytes.fromhex(hex_str)
# print(base64.b64encode(bytes_data))

# msg = long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269)
# print("".join(chr(o) for o in msg))

# string = "label"
# print(xor(string, 13))/

# KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
# KEY1b = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
# KEY12b = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
# KEY2b = xor(KEY1b, KEY12b)
# KEY23b = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
# KEY3b = xor(KEY23b, KEY2b)
# FLAGb = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
# flag = xor(FLAGb, KEY3b, KEY2b, KEY1b).decode()
# print(flag)

# hex_str = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
# decd = bytes.fromhex(hex_str)
# a = 0
# while True:
#     xrd = xor(decd, a)
#     flag = "".join(chr(o) for o in xrd)
#     if flag.startswith('crypto{'):
#         print(flag)
#         print("key is", a)
#         break
#     a += 1

hex_str = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
decd = bytes.fromhex(hex_str)
keyb = xor(decd, b'crypto{')
fullkey = "".join(chr(o) for o in keyb)
print(fullkey)
flagb = xor(decd, b'myXORkey')
print(flagb.decode())
