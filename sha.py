from hashlib import sha1
sha1 = sha1()
sha1.update(input("Input Message: ").encode())
hash = sha1.hexdigest()
print(hash)