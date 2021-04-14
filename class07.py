#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class07.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  4/13/2021    
# Purpose:                  File Encryption Script Part 2.

# Declaration of variables:
y_n = "y"

# Import Libraries
from cryptography.fernet import Fernet


# Declaration of functions:
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        print("Key is "+str(key.decode('utf-8')))

def load_key():
    return open("key.key", "rb").read()

def encrypt_message():
    user_message = input("Enter message to encrypt: ")
    message_e = user_message.encode()
    f = Fernet(key)
    encrypted = f.encrypt(message_e)
    print("Encrypted message: ")
    print(encrypted)

def decrypt_message():
    user_message = input("Enter message to decrypt: ")
    message_d = str.encode()
    f = Fernet(key)
    decrypted = f.decrypt(message_d)
    print("Decrypted message: ")
    print(str(decrypted.decode('utf-8')))

def encrypt_file():
    f = Fernet(key)
    filename = input("Enter file path for file to encrypt: ")
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_file = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_file)

def decrypt_file():
    f = Fernet(key)
    filename = input("Enter file path for file to decrypt: ")
    with open(filename, "rb") as file:
        encrypted_doc = file.read()
    decrypted_info = f.decrypt(encrypted_doc)
    with open(filename, "wb") as file:
        file.write(decrypted_info)

def ask_user():
    mode = input("\nSelect a mode: \nMode 1: Encrypt a File \nMode 2: Decrypt a File \nMode 3: Encrypt a Message \nMode 4: Decrypt a Message\n")
    if (mode== "1"):
        encrypt_file()
        print("File encrypted.")
    elif (mode== "2"):
        decrypt_file()
        print("File decrypted.")
    elif (mode== "3"):
        encrypt_message()
    elif (mode== "4"):
        decrypt_message()
    elif ((mode != "1") and (mode != "2") and (mode != "3") and (mode != "4")):
        print("Invalid input.")

# Main
#write_key()

# load the previously generated key
key = load_key()

while True:
    ask_user()
    y_n = input("Try again? y/n\n")
    if y_n == "n":
        print("See ya later!")
        break

#End
