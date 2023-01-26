alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = input('Insert Key: ').lower().replace(' ', '')
word = input('Input Text: ').lower().replace(' ', '')
key = key * (len(word)//len(key) + 1)
enc = ''.join([alpha[(alpha.index(word[x]) + alpha.index(key[x])) % 26] for x in range(len(word))])
dec = ''.join([alpha[(alpha.index(enc[x]) - alpha.index(key[x])) % 26] for x in range(len(word))])
print('Encrypted Text: {}'.format(enc))
print('Decrypted Text: {}'.format(dec))