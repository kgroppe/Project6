import hashlib
import time
import itertools

lowerCase = ['a','b','c','d','e','f','g','h']
upperCase = ['G','H','I','J','K','L']
numbers = ['0','1','2','3']
special = ['!','@','#','$']
allCharacters = lowerCase + upperCase + numbers + special

#DIR = 'C:\\'

SALT = "&45Bvx9"
PW_LOW = 2
PW_HIGH = 6


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

fp.close()

elapsedTime = time.time() - startTime
print("Single Core Rainbow Complete")
print("Elapsed time:",elapsedTime)
print("Passwords Generated:", pwCount)
print()