import os
from cryptography.fernet import Fernet
import time
files = []
print("Instrucitons:")
print("1.Create a new Folder")
print("2.Put the files you want to encrypt in that Folder")
print("3.Put this program in the same Folder")
print("4.Run this program")
time.sleep(3)
print("Finding files.....")
time.sleep(3)
for file in os.listdir():
    files.append(file)
    if file == "file_encryptor.py":
        continue
print("Done")
time.sleep(2)
print("Generating key.....")
key = Fernet.generate_key()
time.sleep(2)
print("Done")
time.sleep(1)
print("Saving the key....")
time.sleep(2)
with open("thekey.key", "wb") as thekey:
    thekey.write(key)
print("Done")
time.sleep(1)
print("Encrypting files....")
time.sleep(2)

    
print("Done")
time.sleep(1)
print("Replacing data.....")
time.sleep(2)
for file in files:
    with open(file, "wb"):
        data = file.write()
        encrypted_files = Fernet(key).encrypt(data)

    with open(file, "wb") as thefile:
        thefile.write(encrypted_files)
print("Done")
print("The key is" + key.decode())





