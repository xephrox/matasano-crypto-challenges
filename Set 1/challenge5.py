'''
Created on Oct 24, 2015

@author: Trinity
'''

import binascii
from Crypto.Util.strxor import strxor

'''
def sxor(char1, char2):
    return chr(ord(char1)^ord(char2))

def repeatedXOR(s, key):
    return bytes([sxor(s[i],key[i % len(key)]) for i in range(len(s))])
'''

x = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key = b'ICE'
newkey = ( key*(len(x)/len(key)) ) + key[:len(x)%len(key)]
ExpectedAnswer = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

if __name__ == "__main__":
    answerDecode = strxor(x, newkey)
    answer = binascii.hexlify(answerDecode).decode('ascii')
    print "Expected :" + ExpectedAnswer
    print "Answer : " + answer
    if ExpectedAnswer != answer:
        raise Exception (answer + " != " + ExpectedAnswer)
    