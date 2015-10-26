'''
Created on Oct 26, 2015

@author: Trinity
'''

import base64
from Crypto.Cipher import AES

def AESdecrypt(x, key):
    cipher = AES.new(key, AES.MODE_ECB)
    y = cipher.decrypt(x)
    print (y.decode('ascii'))

if __name__ == "__main__":
    x = base64.b64decode(open('extra/7.txt', 'r').read())
    key = b'YELLOW SUBMARINE'
    AESdecrypt(x, key)
