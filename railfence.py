import numpy
key = int(input('Insert Key: '))
word = input('Input Text: ').lower().replace(' ', '')
word_rail = numpy.array([x for x in word]).reshape(key, len(word)//key).transpose()
enc = ''.join(x for x in word_rail.flatten())
dec = ''.join(x for x in word_rail.transpose().flatten())
print('Encrypted Text: {}'.format(enc))
print('Decrypted Text: {}'.format(dec))