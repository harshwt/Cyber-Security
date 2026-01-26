#deffie-hellman key exchange

n = 11
p = 7

#pow(priv num, exponent, mod)
x = 3 #alice private number be x
a = pow(p, x, n) #alice's public key

y = 4    #bob's private number be y
b = pow(p, y, n)  #bob's public key

#exhange key...

shared_secret_alice = pow(b, x, n)
shared_secret_bob = pow(a, y, n)

print(shared_secret_alice)
print(shared_secret_bob)

