'''
Created on Oct 25, 2015

@author: Trinity
'''

import base64
import challenge3
import challenge5
import itertools

def HammingDistance(x, y):
    return sum([bin(x[i] ^ y[i]).count('1') for i in range(len(x))])

def test():
    x = b'this is a test'
    y = b'wokka wokka!!!'
    expectedD = 37
    D = HammingDistance(x, y)
    if (D != expectedD):
        raise Exception("Test Drive Fail")
    
def FindKeyLength(x, k):
    blocks = [x[i:i+k] for i in range(0, len(x), k)][0:4]
    perms = list(itertools.combinations(blocks, 2))
    values = [HammingDistance(p[0], p[1])/float(k) for p in perms][0:6]
    return sum(values)/len(values)

def FindKey(x, k):
    blocks = [x[i:i+k] for i in range(0, len(x), k)]
    transposed_blocks = list(itertools.zip_longest(*blocks, fillvalue = 0))
    key = [challenge3.answer(bytes(x))[0] for x in transposed_blocks]
    return bytes(key)

if __name__ == "__main__":
    test()
    x = base64.b64decode(open('extra/6.txt', 'r').read())
    key_length = min(range(2,41), key = lambda k: FindKeyLength(x,k))
    key = FindKey(x, key_length)
    y = challenge5.repeatedXOR(x, key)
    print (key.decode("ascii"))
    print (y.decode("utf-8"))
    

