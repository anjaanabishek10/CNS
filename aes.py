from Crypto.Cipher import AES
key = b'0123456798765432'
word = b'{}'.format(input('Input Text: ').lower().replace(' ', ''))
cipher = AES.new(key)
enc = cipher.encrypt(word)
dec = cipher.decrypt(enc)
print('Key: {}'.format(key))
print('Encrypted Text: {}'.format(enc))
print('Decrypted Text: {}'.format(dec))