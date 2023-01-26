import numpy
key = input('Insert Key: ').lower().replace(' ', '')
key_sort = [x for x in key]
key_sort.sort()
word = input('Input Text: ').lower().replace(' ', '')
word_arr = numpy.array([x for x in word]).reshape(len(word)//len(key), len(key)).transpose()
enc_arr = numpy.array([word_arr[key.find(x)] for x in key_sort])
enc = ''.join(x for x in enc_arr.flatten())
dec_arr = numpy.array([enc_arr[key_sort.index(x)] for x in key]).transpose()
dec = ''.join(x for x in dec_arr.flatten())
print('Encrypted Text: {}'.format(enc))
print('Decrypted Text: {}'.format(dec))