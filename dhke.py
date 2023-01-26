p = int(input('Prime Number: '))
g, a, b = 3, 2, 3
A, B = (g ** a) % p, (g ** b) % p
Sa, Sb = (B ** a) % p, (A ** b) % p
print("Public Key A: {}".format(A))
print("Public Key B: {}".format(B))
print("Private Key A: {}".format(a))
print("Private Key B: {}".format(b))
print("Secret Key A: {}".format(Sa))
print("Secret Key B: {}".format(Sb))
print("Key Exchange Success")