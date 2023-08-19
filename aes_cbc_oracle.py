from pwn import *

target_msg = b"CBC Magic!" + b"\x06" * 6  # padded message
conn = remote("aes.sstf.site", 1337)

ip = b''  # intermediate plaintext
for i in range(1, 17):
    payload = bytearray(b"A" * (17 - i))
    padding = bytes([c ^ i for c in ip])
    for j in range(256):
        payload[-1] = j
        iv = payload + padding
        conn.sendlineafter(b": ", iv.hex().encode())  # initial vector
        conn.sendlineafter(b": ", b"41" * 16)  # ciphertext: 'A'*16
        res = conn.recvline()
        if b"Try again." not in res:
            ip = bytes([j ^ i]) + ip
            print(i)
            break
iv = bytes([x ^ y for x, y in zip(ip, target_msg)])

conn.sendlineafter(b": ", iv.hex())
conn.sendlineafter(b": ", b"41" * 16)

print(conn.recvline().decode())
