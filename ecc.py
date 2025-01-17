def point_addition(P, Q, a, p, O=(None, None)):
    """
    Add two points P and Q on an elliptic curve defined by y^2 = x^3 + ax + b.

    Parameters:
    P, Q: Tuples representing points (x, y). Use O=(None, None) for the point at infinity.
    a: Coefficient of x in the elliptic curve equation.
    O: The point at infinity (default: (None, None)).

    Returns:
    Tuple representing the resulting point (x3, y3).
    """
    if P == O:
        return Q
    if Q == O:
        return P

    x1, y1 = P
    x2, y2 = Q

    # If P and -Q are additive inverses
    if x1 == x2 and y1 == -y2:
        return O

    if P != Q:
        # Slope for P != Q
        lam = ((y2 - y1) * pow((x2 - x1), -1, p)) % p
    else:
        # Slope for P == Q (tangent)
        lam = (3 * x1**2 + a) * pow((2 * y1), -1, p) % p

    # Calculate resulting point
    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)

def point_inverse(P, p):
    """
    Returns the inverse of point P, i.e., -P, on the elliptic curve modulo p.
    """
    if P == (None, None):
        return P
    x, y = P
    return (x, (-y) % p)

def point_subtraction(P, Q, a, p, O=(None, None)):
    """
    Subtract two points P and Q on an elliptic curve defined by y^2 = x^3 + ax + b (mod p).

    Parameters:
    P, Q: Tuples representing points (x, y). Use O=(None, None) for the point at infinity.
    a: Coefficient of x in the elliptic curve equation.
    p: The prime modulus for the finite field.
    O: The point at infinity (default: (None, None)).

    Returns:
    Tuple representing the resulting point (x3, y3).
    """
    # Step 1: Find the inverse of Q
    Q_inv = point_inverse(Q, p)
    
    # Step 2: Add P and -Q (i.e., P + (-Q)) using the point addition formula
    return point_addition(P, Q_inv, a, p, O)


def scalar_multiplication(P, n, a, p, O=(None, None)):
    """
    Perform scalar multiplication [n]P on an elliptic curve using the double-and-add algorithm.

    Parameters:
    P: Tuple representing the point (x, y) on the curve.
    n: Scalar multiplier (integer).
    a: Coefficient of x in the elliptic curve equation.
    p: Prime modulus for the finite field.
    O: The point at infinity (default: (None, None)).

    Returns:
    Tuple representing the resulting point (x, y).
    """
    R = O
    Q = P

    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q, a, p, O)
        Q = point_addition(Q, Q, a, p, O)
        n //= 2

    return R

def bsgs(G, Q, p, n, a):
    """
    Solve [k]G = Q on an elliptic curve using Baby-Step Giant-Step.
    G: Generator point
    Q: Target point
    p: Prime modulus
    n: Order of the curve
    """
    m = int(n**0.5) + 1
    # Baby steps: Compute [i]G for i in range(m)
    baby_steps = {scalar_multiplication(G, i, a, p): i for i in range(m)}
    
    # Giant steps: Compute Q - [j * m]G for j in range(m)
    mG = scalar_multiplication(G, m, a, p)
    current = Q
    for j in range(m):
        if current in baby_steps:
            return j * m + baby_steps[current]
        current = point_subtraction(current, mG, a, p)
    return None  # No solution found


# Function to count points on the elliptic curve y^2 = x^3 + ax + b mod p
def count_points_on_curve(p, a, b):
    count = 1  # Starting with the point at infinity
    
    for x in range(p):
        rhs = (x**3 + a * x + b) % p  # Right-hand side: x^3 + ax + b
        # Check if there is a square root of rhs modulo p
        if pow(rhs, (p - 1) // 2, p) == 1:  # This checks if rhs is a quadratic residue modulo p
            count += 2  # Two solutions for y (y and -y)
        elif rhs == 0:
            count += 1  # Only one solution y = 0
            
    return count


# Example usage
def main():
    # Example elliptic curve: y^2 = x^3 + ax + b with a = 2, b = 3
    # a = 497
    a = 2
    O = (None, None)  # Point at infinity
    # p = 9739
    p = 310717010502520989590157367261876774703

    # P = (493,5564)
    # xQa = 4726
    # R = (4403,5202)
    G = (179210853392303317793440285562762725654,105268671499942631758568591033409611165)

    # y_squared = (xQa**3 + 497*xQa + 1768) % p
    # y = pow(y_squared, (p+1)//4, p)
    # print(y, p-y)
    # Qa = (xQa, p-y)
    
    # for i in range(p//2, p+1):
    #     result = scalar_multiplication(G, i, a, p)
    #     i += 1
    #     if result == (280810182131414898730378982766101210916,291506490768054478159835604632710368904):
    #         print(i)
    #         break


    # Count the points on the curve
    # curve_order = count_points_on_curve(p, a, b)
    # print(curve_order)


    result = bsgs(G, (280810182131414898730378982766101210916,291506490768054478159835604632710368904), p, 15, a)

    # Qb = [nb]G = [1829]G = (4221, 4874)
    # [nb]Qa = [na]Qb = S = (7929, 707)
    print("P + Q =", result)

if __name__ == "__main__":
    main()
