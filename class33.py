#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class33.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  5/19/2021    
# Purpose:                  Signature-based Malware Detection Part 3 of 3.

# Import libraries:
import hashlib, os, time, datetime, time
from sys import platform

# Define variables:
md5_hash = hashlib.md5()
apikey = os.getenv('API_KEY_VIRUSTOTAL')
query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + hash

# Define functions:
def create_timestamp():
    now = datetime.datetime.now()
    timestamp = now.strftime('%m-%d-%Y %H:%M:%S:%f')
    return str(timestamp)

def linuxsearch():
    thefile = input("Enter the file you are searching for:")
    thedirectory = input("Enter the directory to search:")
    os.system("ls " + str(thedirectory) + " | echo \"Searched $(wc -l) files.\"")
    os.system("find " + str(thedirectory) + ' -wholename ' + str(thefile) + " -print | echo \"Found $(grep -c /) files that mathced:\"")
    print("")
    os.system("find " + str(thedirectory) + ' -wholename ' + str(thefile))
    print("")


def thehash(thefile):
    md5_hash = hashlib.md5()
    with open(thefile,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        return md5_hash.hexdigest()

def dircontents_hash():
    dir_count = 0
    file_count = 0
    start_path = input("Enter path of directory to search:")

# Main

if platform == "linux" or platform == "linux2":
    print("Searching Linux Machine.")
    linuxsearch()

for (path,dirs,files) in os.walk(start_path):
    print('Directory: {"s}'.format(path))
    print("")
    dir_count += 1

    for file in files:
        fstat = os.stat(os.path.join(path, file))

print('Summary: hashed {} file in {} directories'.format(file_count,dir_count))
dir_count = 0
file_count = 0

