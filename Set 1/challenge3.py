'''
Created on Oct 24, 2015

@author: Trinity
'''

import binascii
from Crypto.Util.strxor import strxor_c
from collections import Counter
import math

FREQUENCY_TABLE = {
    b'a':  0.08167,
    b'b':  0.01492,
    b'c':  0.02782,
    b'd':  0.04253,
    b'e':  0.1270,
    b'f':  0.02228,
    b'g':  0.02015,
    b'h':  0.06094,
    b'i':  0.06966,
    b'j':  0.00153,
    b'k':  0.00772,
    b'l':  0.04025,
    b'm':  0.02406,
    b'n':  0.06749,
    b'o':  0.07507,
    b'p':  0.01929,
    b'q':  0.00095,
    b'r':  0.05987,
    b's':  0.06327,
    b't':  0.09056,
    b'u':  0.02758,
    b'v':  0.00978,
    b'w':  0.02360,
    b'x':  0.00150,
    b'y':  0.01974,
    b'z':  0.00074,
}

def englishness(a):
    c = Counter(a.lower())
    total_characters = len(a)
    coefficient = sum(math.sqrt(FREQUENCY_TABLE.get(bytes([char]), 0) * y/total_characters) for char,y in c.items())
    return coefficient

def answer(s):
    print (s)
    def compfunc(items):
        return englishness(items[1])
    return max([(i, strxor_c(s,i)) for i in range(0,256)], key = compfunc)

if __name__ == '__main__':
    encodedS = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    S = binascii.unhexlify(encodedS)
    print (answer(S))
