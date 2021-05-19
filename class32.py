#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class31.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  5/18/2021    
# Purpose:                  Signature-based Malware Detection Part 2 of 3.

# Import libraries:
import hashlib, os, time
from sys import platform

# Define variables:
filename = input("Enter the file name: ")
md5_hash = hashlib.md5()

# Define functions:
def linuxsearch():
    thefile = input("Enter the file you are searching for:")
    thedirectory = input("Enter the directory to search:")
    os.system("ls " + str(thedirectory) + " | echo \"Searched $(wc -l) files.\"")
    os.system("find " + str(thedirectory) + ' -wholename ' + str(thefile) + " -print | echo \"Found $(grep -c /) files that mathced:\"")
    print("")
    os.system("find " + str(thedirectory) + ' -wholename ' + str(thefile))
    print("")

if platform == "linux" or platform == "linux2":
    print("Searching Linux Machine.")
    linuxsearch()

with open(filename,"rb") as f:
    for byte_block in iter(lambda: f.read(4096),b""):
        md5_hash.update(byte_block)
    print(md5_hash.hexdigest())



# End
