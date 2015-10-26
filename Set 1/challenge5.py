'''
Created on Oct 24, 2015

@author: Trinity
'''

import binascii
from Crypto.Util.strxor import strxor


def repeatedXOR(s, key):
    return bytes([ s[i] ^ key[i % len(key)] for i in range(len(s))])

x = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key = b'ICE'
ExpectedAnswer = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

if __name__ == "__main__":
    answerDecode = repeatedXOR(x, key)
    answer = binascii.hexlify(answerDecode).decode('ascii')
    print ("Expected : " + ExpectedAnswer)
    print ("Answer :   " + answer)
    if ExpectedAnswer != answer:
        raise Exception (answer + " != " + ExpectedAnswer)
    