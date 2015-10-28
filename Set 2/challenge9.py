'''
Created on Oct 28, 2015

@author: Trinity
'''

from binascii import unhexlify

def PKCS7_padding(text, block_size):
    text_length = len(text)
    amount_to_pad = block_size - (text_length%block_size)
    if (amount_to_pad == 0):
        amount_to_pad = block_size
    pad = unhexlify('%02d' % amount_to_pad)
    return (text + pad*amount_to_pad)

if __name__ == "__main__":
    X = b'YELLOW SUBMARINE'
    ExpectedY = b'YELLOW SUBMARINE\x04\x04\x04\x04'
    Y = PKCS7_padding(X, 20)
    if Y != ExpectedY:
        raise Exception("Incorrect Answer")
    else:
        print (Y)