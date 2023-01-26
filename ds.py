from hashlib import sha256
sha2561 = sha256()
data = input("Input Message: ")
sha2561.update(data.encode())
hash = sha2561.hexdigest()
sign = data + hash
enc = ''.join([chr(ord(x) + 11)for x in sign])
dec = ''.join([chr(ord(x) - 11)for x in enc])
rdata = dec[0:len(data)]
sha2562 = sha256()
sha2562.update(rdata.encode())
rhash = sha2562.hexdigest()
if (hash == rhash):
    print("Original Hash: {}".format(hash))
    print("Signature: {}".format(enc))
    print("Received Hash: {}".format(rhash))
    print("No change in data")