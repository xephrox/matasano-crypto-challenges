'''
Created on Oct 26, 2015

@author: Trinity
'''

import binascii
import itertools

def decodefile(filename):
    f = open(filename, 'r')
    for line in f:
        if line[-1] == '\n':
            line = line[:-1]
        s = binascii.unhexlify(line)
        yield s 

def score(line):
    block_size = 16
    blocks = [line[i:i+block_size] for i in range(0, len(line), block_size)]
    perms = itertools.combinations(blocks, 2)
    score = 0
    for p in perms:
        if (p[0] == p[1]):
            score += 1
    return score

if __name__ == "__main__":
    lines = decodefile('extra/8.txt')
    line_number = 0
    for l in lines:
        if score(l) > 0:
            print (line_number)
        line_number += 1