'''
Created on Oct 23, 2015

@author: Trinity
'''

import binascii
import base64

def hexTobase64(s):
    decoded = binascii.unhexlify(s)
    return base64.b64encode(decoded).decode('ascii')

if __name__ == "__main__":
    x = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    answer = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    y = hexTobase64(x)
    print y
    print answer
    if y != answer:
        raise Exception(y + '!=' + answer)
