#vighnere cipher 

plaintext = "harshwardhan"

key = 5

mode = 'encrypt'

ledger = "abcdefghijklmnopqrstuvwxyz 1234567890"

ciphertext = ''

for i in plaintext:

    textIndex = ledger.find(i)

    if mode == 'encrypt':
        cipherindex = textIndex + key
    elif mode == 'decrypt':
        cipherindex = textIndex - key

    if cipherindex >= len(ledger):
        cipherindex = cipherindex - len(ledger)
    elif cipherindex < 0:
        cipherindex =  cipherindex + len(ledger)

    ciphertext = ciphertext + ledger[cipherindex]

    
print(ciphertext)
