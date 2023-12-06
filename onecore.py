import hashlib
import time
import itertools

lowerCase = ['a','b','c','d','e','f','g','h']
upperCase = ['G','H','I','J','K','L']
numbers = ['0','1','2','3']
special = ['!','@','#','$']
allCharacters = lowerCase + upperCase + numbers + special

DIR = 'C:\\'

SALT = "&45Bvx9"
PW_LOW = 2
PW_HIGH = 6


startTime = time.time()

pwList = []
for r in range(PW_LOW, PW_HIGH):
    for s in itertools.product(allCharacters, repeat=r):
        pwList.append(''.join(s))

try:
    fp = open(DIR+'all','w')
    for pw in pwList:
        sha256Hash = hashlib.sha256()
        sha256Hash.update(SALT + pw)
        sha256Digest = sha256Hash.hexdigest()
        fp.write(sha256Digest + ' ' + pw + '\n')
        del sha256Hash
except:
    print("File Processing Error")
fp.close() #check placement of this
    
