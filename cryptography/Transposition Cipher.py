#transposition cipher
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


