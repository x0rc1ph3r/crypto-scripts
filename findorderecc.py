from Crypto.Util.number import inverse

# Define the curve parameters
p = 310717010502520989590157367261876774703
a = 2
b = 3

# Generator point G
g_x = 179210853392303317793440285562762725654
g_y = 105268671499942631758568591033409611165
G = (g_x, g_y)

# Function to perform point addition
def point_addition(P, Q, a, p):
    if P == (None, None):
        return Q
    if Q == (None, None):
        return P

    x1, y1 = P
    x2, y2 = Q

    # If P and -Q are additive inverses, return the point at infinity
    if x1 == x2 and y1 == (-y2 % p):
        return (None, None)

    if P != Q:
        # Slope for P != Q
        lam = ((y2 - y1) * pow((x2 - x1), -1, p)) % p
    else:
        # Slope for P == Q (point doubling)
        lam = (3 * x1**2 + a) * pow((2 * y1), -1, p) % p

    # Calculate resulting point
    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)

# Function to perform point multiplication using double and add
def double_and_add(P, n, a, p):
    R = (None, None)  # Identity element (point at infinity)
    Q = P

    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q, a, p)
        Q = point_addition(Q, Q, a, p)  # Point doubling
        n = n // 2

    return R

# Find the order of the curve by checking successive multiplications of G
def find_order(G, a, p):
    n = 1
    point = G
    while point != (None, None):  # Identity point at infinity
        point = double_and_add(G, n, a, p)
        n += 1
    return n

# Test and find the order of the curve
order = find_order(G, a, p)
print(f"The order of the curve is: {order}")
