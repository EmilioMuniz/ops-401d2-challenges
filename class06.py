#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class06.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  4/12/2021    
# Purpose:                  File Encryption Script.

# Declaration of variables:

# Import Libraries
from cryptography.fernet import Fernet
import inquirer


# Declaration of functions:
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        print("Key is "+str(key.decode('utf-8')))

def load_key():
    return open("key.key", "rb").read()


# Main
write_key()

# load the previously generated key
key = load_key()

message = "Hello there!".encode()

# initialize the Fernet class
#f = Fernet(key)

# encrypt the message
#encrypted = f.encrypt(message)

# print how it looks
#print(encrypted)
questions = [
  inquirer.List('method',
                message="Select Mode:",
                choices=["Mode 1 Encrypt a File", "Mode 2 Decrypt a File", "Mode 3 Encrypt a Message", "Mode 4 Decrypt a Message"],
            ),
]
answers = inquirer.prompt(questions)
#print ("Performing:", answers['method'])
#choice = input("Would you like to proceed? y/n""\n")
#if answers == "Mode 1 Encrypt a File":
#    g = requests.get(webpage)
#    print(g.text)
#elif choice == "n":
#    print("Goodbye!")
