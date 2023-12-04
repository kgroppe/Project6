import hashlib
import time
import sys
import os
import itertools

chars = ['a','b','c','d','e','f','g','h']

SALT = "&45Bvx9"
PW_LOW = 4
PW_HIGH = 8

print("Processing Single Core")
print(os.getcwd())
print("Password Caracter Set:", chars)
print("Password Lengths:", str(PW_LOW), "-", str(PW_HIGH))

startTime = time.time()

try:
    fp = open('PW-ALL', 'w')
except:
    print("File Processing Error")
    sys.exit(0)

pwCount = 0

for r in range(PW_LOW, PW_HIGH + 1):
    for s in itertools.product(chars, repeat = r):
        pw=''.join(s)
        try:
            sha256Hash = hashlib.sha256()
            sha256Hash.update(SALT + pw)
            sha256Digest = sha256Hash.hexdigest()
            fp.write(sha256Digest+' '+pw+'\n')
            pwCount += 1
            del sha256Hash
        except:
            print("File Processing Error")

