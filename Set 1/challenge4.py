'''
Created on Oct 24, 2015

@author: Trinity
'''

import binascii
import challenge3
from Crypto.Util.strxor import strxor_c

def decodefile(filename):
    f = open(filename, 'r')
    for line in f:
        if line[-1] == '\n':
            line = line[:-1]
        s = binascii.unhexlify(line)
        yield s

def findXORLine(generator):
    lines = [challenge3.answer(l)[1] for l in generator]
    def compfunc(i):
        return challenge3.englishness(lines[i])
    maxI = max(range(len(lines)), key=compfunc)
    return lines[maxI]

print (findXORLine(decodefile('extra/4.txt')).decode("ascii"))

        


