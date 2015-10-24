'''
Created on Oct 23, 2015

@author: Trinity
'''

import binascii
from Crypto.Util.strxor import strxor

def reverse_engineer():
    encodedS = '1c0111001f010100061a024b53535009181c'
    encodedT = '686974207468652062756c6c277320657965'
    encodedExpectedU = '746865206b696420646f6e277420706c6179'

    S = binascii.unhexlify(encodedS)
    T = binascii.unhexlify(encodedT)
    ExpectedU = binascii.unhexlify(encodedExpectedU)

    U = strxor(S, T)
    print U
    print ExpectedU
    if U != ExpectedU:
        raise Exception (U + '!=' + ExpectedU)

if __name__ == "__main__":
    reverse_engineer()
