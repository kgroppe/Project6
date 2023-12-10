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
            sha256Hash.update((SALT + pw).encode())
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

    for i in range(PW_LOW, PW_HIGH):
        try:
            fp = open(DIR+str(i), 'r')
            for line in fp:
                pairs = line.split()
                pwDict.update({pairs[0]: pairs[1]})
            fp.close()
        except:
            print("File Handling Error")
            fp.close()

    elapsedTime = time.time() - startTime
    print("Elapsed TIme: ", elapsedTime)
    print("Passwords Generated: ", len(pwDict))
    print()

    cnt = 0
    for key, value in (pwDict.items()):
        print(key, value)
        cnt += 1
        if cnt > 10:
            break
        print()

    pw = pwDict.get('1dbdfd6de15b28f247ec7e1ec571b9f49098b82a6be400baa0fe0e44aedc4e1c')
    print("Hash Value Tested = 1dbdfd6de15b28f247ec7e1ec571b9f49098b82a6be400baa0fe0e44aedc4e1c")
    print("Associated Password = ", pw)
