import hashlib
import time
import itertools
import multiprocessing

lowerCase = ['a','b','c','d','e','f','g','h']
upperCase = ['G','H','I','J','K','L']
numbers = ['0','1','2','3']
special = ['!','@','#','$']
allCharacters = lowerCase + upperCase + numbers + special

DIR = 'pw\\'

SALT = "&45Bvx9"
PW_LOW = 2
PW_HIGH = 6

def pwGenerator(size):
    pwList = []
    for r in range(size, size + 1):
        for s in itertools.product(allCharacters, repeat=r):
            pwList.append(''.join(s))

    try:
        fp = open(DIR+str(size),'w')
        for pw in pwList:
            sha256Hash = hashlib.sha256()
            sha256Hash.update(SALT + pw)
            sha256Digest = sha256Hash.hexdigest()
            fp.write(sha256Digest + ' ' + pw + '\n')
            del sha256Hash
    except IOError:
        print("File Processing Error")
    finally:
        fp.close()

if __name__ == "__main__":
    startTime = time.time()

    corePool = multiprocessing.Pool(processes=4)

    results = corePool.map(pwGenerator, (2, 3, 4, 5))

    pwDict = {}

    
