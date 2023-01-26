from Crypto.Cipher import DES
key = b'01234567'
word = b'{}'.format(input('Input Text: ').lower().replace(' ', ''))
cipher = DES.new(key)
enc = cipher.encrypt(word)
dec = cipher.decrypt(enc)
print('Key: {}'.format(key))
print('Encrypted Text: {}'.format(enc))
print('Decrypted Text: {}'.format(dec))