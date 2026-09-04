import math
# 1. Choose two small primes 
p = 61
q = 53

# 2. Compute Modulus (n) and Totient (phi)
n = p * q
phi = (p - 1) * (q - 1)

# 3. Choose Public Exponent (e) that is coprime to phi
e = 17
while math.gcd(e, phi) != 1:
    e += 2

# 4. Compute Private Exponent (d) using Python's built-in modular inverse
d = pow(e, -1, phi)

# Exported Keys
PUBLIC_KEY = (e, n)
PRIVATE_KEY = (d, n)


def encrypt(public_key, plaintext):
    """Encrypts a string into a list of integers."""
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]


def decrypt(private_key, ciphertext):
    """Decrypts a list of integers back into a string."""
    d, n = private_key
    return "".join([chr(pow(char, d, n)) for char in ciphertext])


#trial..
if __name__ == "__main__":
    message = "Hello GitHub"
    print(f"Original:  {message}")

    encrypted = encrypt(PUBLIC_KEY, message)
    print(f"Encrypted: {encrypted}")

    decrypted = decrypt(PRIVATE_KEY, encrypted)
    print(f"Decrypted: {decrypted}")
