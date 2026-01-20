#transposition cipher

"""
Description

A Transposition cipher is a method of encryption by which the positions held by units
of plaintext (which are commonly characters or groups of characters) are shifted according to
a regular system, so that the ciphertext constitutes a permutation of the plaintext. That is, the
order of the units is changed (the plaintext is reordered). Mathematically a bijective function
is used on the characters&#39; positions to encrypt and an inverse function to decrypt.
Transposition Ciphers does not substitute one symbol for another, instead it changes the
location of the symbols.

A symbol in the first position of the plaintext may appear in the tenth position of the
ciphertext. A symbol in the eight position in the plaintext may appear in the first position of
the ciphertext. A transposition cipher reorders (transposes) the symbols. Simple
transposition ciphers, which were used in the past, are keyless.

There are two methods for permutation of characters. In the first method, the text is written
into a table column by column and then transmitted row by row. In the second method, the
text is written into a table row by row and then transmitted column by column.
"""

import numpy as np

def method1_encryption(text):
    arr = []
    text = text.replace(" ", "") # Remove spaces
    for i in text:
        arr.append(i)
    row1 = arr[::2] 
    row2 = arr[1::2]
    print("\nMethod 1 of Transposition Cipher: ")
    print("List:")
    result = row1 + row2
    print(result)
    cipher = "".join(result) # Writing outcome as a string
    print("\nCipher text: ")
    print(cipher)

method1_encryption("meet me at the park")


def method2_encryption(text):
    # Remove spaces and pad to 16 characters
    clean_text = text.replace(" ", "")
    padded = clean_text.ljust(16, 'X')  # adding x as filler
    print("\nMethod 2 of the Transposition Cipher: ")
    # Fill 4x4 grid row-wise
    arr = np.array(list(padded)).reshape(4, 4)
    print("Grid:")
    print(arr)

    # Read column-wise to form cipher text
    cipher = ""
    for i in range(4):  # Here i is for col & j is for row 
        for j in range(4):
            cipher += arr[j, i]

    print("\nCipher text: ")
    print(cipher)

method2_encryption("meat me at the park")



