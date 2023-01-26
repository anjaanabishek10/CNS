import numpy
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = input('Insert Key: ').lower().replace(' ', '')
word = input('Input Text: ').lower().replace(' ', '')
key_arr = numpy.array([alpha.index(x) for x in key]).reshape(int(len(key)**0.5), int(len(key)**0.5))
word_arr = numpy.array([alpha.index(x) for x in word]).reshape(int(len(key)**0.5), int(len(word)/(len(key)**0.5)))
enc_arr = numpy.matmul(key_arr, word_arr) % 26
enc = ''.join([alpha[x] for x in enc_arr.flatten()])
inv_key_arr = numpy.linalg.inv(key_arr) % 26
dec_arr = numpy.matmul(inv_key_arr, enc_arr) % 26
dec = ''.join([alpha[int(x)] for x in dec_arr.flatten()])
print('Encrypted Text: {}'.format(enc))
print('Decrypted Text: {}'.format(dec))