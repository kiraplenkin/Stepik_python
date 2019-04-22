class BadPassword(Exception):
    pass

import simplecrypt

with open('passwords.txt', 'r') as inp:
    passwords = inp.read().strip().split()

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

try:
    text = simplecrypt.decrypt('RVrF2qdMpoq6Lib', encrypted)
    print(text)
except Exception:
    raise BadPassword
