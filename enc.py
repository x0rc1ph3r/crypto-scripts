from pwn import *
from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l

# flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽'
# # a = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# for char in flag:
#     print(bytes.fromhex(hex(ord(char))[2:]).decode(), end = '')

# flag_enc = bytes.fromhex('551257106e1a52095f654f510a6b4954026c1e0304394100043a1c5654505b6b')
# plain = b'a'*32
# cipher = bytes.fromhex('034605413d190050083d1951533d1902053d1903003d1902553d190403500f3d')

# # output, given input is 'python3 -c "print('a'*49968);print('a'*32)" | nc mercury.picoctf.net 36449' as the key length is 5000,
# # last 32 digits of key are used to encode the plaintext

# key = xor(plain, cipher)
# print(xor(key,flag_enc).decode())

# flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5c) + chr(0x01) + chr(0x57) + chr(0x2a) + chr(0x17) + chr(0x5e) + chr(0x5f) + chr(0x0d) + chr(0x3b) + chr(0x19) + chr(0x56) + chr(0x5b) + chr(0x5e) + chr(0x36) + chr(0x53) + chr(0x07) + chr(0x51) + chr(0x18) + chr(0x58) + chr(0x05) + chr(0x57) + chr(0x11) + chr(0x3a) + chr(0x0f) + chr(0x0a) + chr(0x5b) + chr(0x57) + chr(0x41) + chr(0x55) + chr(0x0c) + chr(0x59) + chr(0x14)

# print(xor(bytes(flag_enc, 'utf-8'), b'enkidu').decode())

# print('picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}')

# print(chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39))

# pos_pw_list = ["158f", "1655", "d21e", "4966", "ed69", "1010", "dded", "844c", "40ab", "a948", "156c", "ab7f", "4a5f", "e38c", "ba12", "f7fd", "d780", "4f4d", "5ba1", "96c5", "55b9", "8a67", "d32b", "aa7a", "514b", "e4e1", "1230", "cd19", "d6dd", "b01f", "fd2f", "7587", "86c2", "d7b8", "55a2", "b77c", "7ffe", "4420", "e0ee", "d8fb", "d748", "b0fe", "2a37", "a638", "52db", "51b7", "5526", "40ed", "5356", "6ad4", "2ddd", "177d", "84ae", "cf88", "97a3", "17ad", "7124", "eff2", "e373", "c974", "7689", "b8b2", "e899", "d042", "47d9", "cca9", "ab2a", "de77", "4654", "9ecb", "ab6e", "bb8e", "b76b", "d661", "63f8", "7095", "567e", "b837", "2b80", "ad4f", "c514", "ffa4", "fc37", "7254", "b48b", "d38b", "a02b", "ec6c", "eacc", "8b70", "b03e", "1b36", "81ff", "77e4", "dbe6", "59d9", "fd6a", "5653", "8b95", "d0e5"]


# import hashlib

# ### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
# def str_xor(secret, key):
#     #extend key to secret length
#     new_key = key
#     i = 0
#     while len(new_key) < len(secret):
#         new_key = new_key + key[i]
#         i = (i + 1) % len(key)
#     return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
# ###############################################################################

# flag_enc = open('level5.flag.txt.enc', 'rb').read()
# correct_pw_hash = open('level5.hash.bin', 'rb').read()


# def hash_pw(pw_str):
#     pw_bytes = bytearray()
#     pw_bytes.extend(pw_str.encode())
#     m = hashlib.md5()
#     m.update(pw_bytes)
#     return m.digest()


# def level_5_pw_check():
#     for word in open('dictionary.txt', 'r'):
#         user_pw = word.strip()
#         user_pw_hash = hash_pw(user_pw)

#         if( user_pw_hash == correct_pw_hash ):
#             print(word)
#             print("Welcome back... your flag, user:")
#             decryption = str_xor(flag_enc.decode(), user_pw)
#             print(decryption)
#             return



# level_5_pw_check()

# flag = b'xakgK\Nsmn;j8j<9;<?=l?k88mm1n9i1j>:8k?l0u'
# for i in range(100):
#     a = ''
#     for j in flag:
#         a += xor(i, j).decode()
#     if a.startswith('pico'):
#         print(a)

# data1 = "\x9dn\x93\xc8\xb2\xb9A\x8b\xc1\xc5\xdca\xc6\x97\x94\x8cf\x91\x91\xc1\x893\x94\x9e\xc9\xdda\x91\xc4\xc8\xddb\xc0\x92\xc1\x8c7\x95\x93\xc8\x90\x00\x00"
# data2 = "\xf1\xa7\xf0\x07\xed"
# for i in range(len(data1)):
#     print(chr(ord(data1[i]) ^ ord(data2[4 - (i % 5)])), end = '')

# ascis = [128, 322, 353, 235, 336, 73, 198, 332, 202, 285, 57, 87, 262, 221, 218, 405, 335, 101, 256, 227, 112, 140]
# ascis = [432, 331, 192, 108, 180, 50, 231, 188, 105, 51, 364, 168, 344, 195, 297, 342, 292, 198, 448, 62, 236, 342, 63]
# alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
# for i in ascis:
#     a = pow(i, 39, 41)
#     print(alphas[a-1], end='')

# 4636878989
# 93089
# 836623060
# ct = 107524013451079348539944510756143604203925717262185033799328445011792760545528944993719783392542163428637172323512252624567111110666168664743115203791510985709942366609626436995887781674651272233566303814979677507101168587739375699009734588985482369702634499544891509228440194615376339573685285125730286623323
# n = 27566996291508213932419371385141522859343226560050921196294761870500846140132385080994630946107675330189606021165260590147068785820203600882092467797813519434652632126061353583124063944373336654246386074125394368479677295167494332556053947231141336142392086767742035970752738056297057898704112912616565299451359791548536846025854378347423520104947907334451056339439706623069503088916316369813499705073573777577169392401411708920615574908593784282546154486446779246790294398198854547069593987224578333683144886242572837465834139561122101527973799583927411936200068176539747586449939559180772690007261562703222558103359
# b = pow(ct, 3, n)
# print(b)

# a = [172, 209, 217, 196, 199, 200, 213, 214, 147, 219, 148, 222, 199, 148, 214, 196, 214, 214, 150, 208, 197, 207, 148, 209, 202, 194, 197, 148, 209, 151, 213, 148, 200, 214, 194, 148, 214, 194, 203, 151, 213, 199, 224]
# for i in a:
#     print(chr(i - 99),end = '')


# import random
# from math import gcd

# def is_prime(n, k=5):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     for _ in range(k):
#         a = random.randint(2, n - 2)
#         if gcd(a, n) != 1 or pow(a, n - 1, n) != 1:
#             return False
#     return True

# def generate_prime(bits):
#     while True:
#         p = random.getrandbits(bits)
#         # Ensure the number is odd
#         p |= 1
#         if is_prime(p):
#             return p

# # Generate two distinct primes of similar bit length
# bits = 1024  # Change this to desired bit length
# p = generate_prime(bits)
# q = generate_prime(bits)

# print(f"p: {p}")
# print(f"q: {q}")
