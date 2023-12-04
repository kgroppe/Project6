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
print("Password Caracter Set: ", chars)
print("Password Lengths: ", str(PW_LOW), " - ", str(PW_HIGH))
