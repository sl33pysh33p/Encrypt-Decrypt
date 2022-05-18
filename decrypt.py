import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "theKey.key" or file == "decrypt.py":
        continue

    if os.path.isfile(file):
        files.append(file)


with open("theKey.key", "rb") as key:
    secretkey = key.read()

for file in files:
    with open(file, "rb") as theFile:
        contents = theFile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as theFile:
        theFile.write(contents_decrypted)
