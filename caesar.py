alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = input('Input Text: ').lower().replace(' ', '')
enc = ''.join(alpha[(alpha.index(x) + 3) % 26] for x in word)
dec = ''.join(alpha[(alpha.index(x) - 3) % 26] for x in enc)
print('Encrypted Text: {}'.format(enc))
print('Decrypted Text: {}'.format(dec))