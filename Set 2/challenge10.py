import base64
from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor

BLOCKSIZE = 16

def getBlocks(s):
    return [s[i:i+BLOCKSIZE] for i in range(0, len(s), BLOCKSIZE)]

def encrypt(plaintext, ECB, IV):
    plaintextblocks = getBlocks(plaintext)
    ciphertext = b''
    previousblock = IV
    for i in range(len(plaintextblocks)):
        plainblock = plaintextblocks[i]
        cipherblock = ECB.encrypt(strxor(plainblock, previousblock))
        ciphertext = ciphertext + cipherblock
        previousblock = cipherblock
    return ciphertext

def decrypt(ciphertext, ECB, IV):
    encryptedblocks = getBlocks(ciphertext)
    plaintext = b''
    previousblock = IV
    for i in range(len(encryptedblocks)):
        cipherblock = encryptedblocks[i]
        plainblock = strxor(ECB.decrypt(cipherblock), previousblock)
        plaintext = plaintext + plainblock
        previousblock = cipherblock
    return plaintext

if __name__ == '__main__':
    x = base64.b64decode (open('extra/10.txt', 'r').read())
    key = b'YELLOW SUBMARINE'
    y = decrypt(x, AES.new(key, AES.MODE_ECB), bytes([0]*16))
    print (b'y: ' + y)
    z = encrypt(y, AES.new(key, AES.MODE_ECB), bytes([0]*16))
    print (b'z: '+ z)
    if (x != z):
        raise Exception("Incorrect Execution")

