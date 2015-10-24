'''
Created on Oct 24, 2015

@author: Trinity
'''
'''
Thanks to https://github.com/Lukasa/cryptopals/blob/master/cryptopals/challenge_one/five.py
for a better code than mine 
'''

import operator
from array import array
from binascii import hexlify
from itertools import cycle, imap

def to_byte(byte):
    if isinstance(byte, bytes):
        return ord(byte)
    else:
        return byte

def repeating_key_XOR(stream, key):
    stream = imap(to_byte, stream)
    key = imap(to_byte, key)
    
    return array('B', imap(operator.xor, stream, cycle(key))).tostring()

if __name__ == '__main__':
    x = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
    key = b'ICE'
    ExpectedAnswer = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    encrypted = repeating_key_XOR(x, key)
    hex_encrypted = hexlify(encrypted)
    print hex_encrypted
    print ExpectedAnswer
    if ExpectedAnswer != hex_encrypted:
        raise Exception(ExpectedAnswer + " != " + hex_encrypted)