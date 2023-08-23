from pwn import *
from sage.all import *


def gcd(a, b): 
    while b:
        a, b = b, a % b
    return a.monic()

def franklinreiter(C1, C2, e, N, a, b):
    P.<X> = PolynomialRing(Zmod(N))
    g1 = (a*X + b)^e - C1
    g2 = X^e - C2
    print('Result')
    result = -gcd(g1, g2).coefficients()[0]
    return hex(int(result))[2:]

p = remote('52.59.124.14', '10008')
print(p.recvline())
N = int(p.recvline().decode())
print('N =', N)
e = 1337
flag_len = 42

for i in range(flag_len, 0, -1):
    try:
        print(p.recvline())
        c1 = int(p.recvline().decode())
        print('c1 =', c1)
        print(p.recvline())
        p.sendline(b'dummy')
        c2 = int(p.recvline().decode())
        print('c2 =', c2)
        guess = bytes.fromhex(franklinreiter(c2, c1, e, N, 1, 2^((35 + i)*8))).split()[11:]
        to_send = b''
        for i in guess:
            to_send += i
        print(to_send)
        p.sendline(to_send)
    except EOFError:
        exit()