import hashlib
import time
import os
import itertools
import multiprocessing

chars = ['a','b','c','d','e','f','g','h']

SALT = "&45Bvx9"
PW_LOW = 4
PW_HIGH = 8

def pwGenerator(size):
    pwCount = 0
    try:
        fp = open('PW-'+str(size), 'w')
        for r in range(size, size + 1):
            for s in itertools.product(chars, repeat = r):
                pw = ''.join(s)
                sha256Hash = hashlib.sha256()
                sha256Hash.update(SALT + pw)
                sha256Digest = sha256Hash.hexdigest()
                fp.write(sha256Digest + ' ' + pw + '\n')
                pwCount += 1
                del sha256Hash

