import hashlib
import time
import itertools

lowerCase = ['a','b','c','d','e','f','g','h']
upperCase = ['G','H','I','J','K','L']
numbers = ['0','1','2','3']
special = ['!','@','#','$']
allCharacters = lowerCase + upperCase + numbers + special

DIR = 'pw\\'

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
        sha256Hash.update((SALT + pw).encode())
        sha256Digest = sha256Hash.hexdigest()
        fp.write(sha256Digest + ' ' + pw + '\n')
        del sha256Hash
    fp.close()
except IOError:
    print("File Processing Error")
    fp.close()
finally:
    fp.close()

pwDict = {}

try:
    fp = open(DIR +'all', 'r')
    for line in fp:
        pairs = line.split()
        pwDict.update({pairs[0]: pairs[1]})
    fp.close()
except IOError:
    print("File Handling Error")
    fp.close()

elapsedTime = time.time() - startTime
print("Elapsed TIme: ", elapsedTime)
print("Passwords Generated: ", len(pwDict))
print()

cnt = 0
for key,value in (pwDict.items()):
    print(key,value)
    cnt += 1
    if cnt > 10:
        break
print()

pw = pwDict.get('1dbdfd6de15b28f247ec7e1ec571b9f49098b82a6be400baa0fe0e44aedc4e1c')
print("Hash Value Tested = 1dbdfd6de15b28f247ec7e1ec571b9f49098b82a6be400baa0fe0e44aedc4e1c")
print("Associated Password = ", pw)

