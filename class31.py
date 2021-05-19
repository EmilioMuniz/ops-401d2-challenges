#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class31.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  5/17/2021    
# Purpose:                  Signature-based Malware Detection Part 1 of 3.

# Import Libraries
import os, time
from sys import platform

# Define variables

# Define functions
def linuxsearch():
    thefile = input("Enter the file you are searching for:")
    thedirectory = input("Enter the directory to search:")
    os.system("ls " + str(thedirectory) + " | echo \"Searched $(wc -l) files.\"")
    os.system("find " + str(thedirectory) + ' -name ' + str(thefile) + " -print | echo \"Found $(grep -c /) files that mathced:\"")
    print("")
    os.system("find " + str(thedirectory) + ' -name ' + str(thefile))
    print("")

# Main
if platform == "linux" or platform == "linux2":
    print("Searching Linux Machine.")
    linuxsearch()

# End for now.
