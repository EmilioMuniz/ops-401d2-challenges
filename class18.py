#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class18.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  4/28/2021    
# Purpose:                  Automated Brute Force Wordlist Attack Tool Part 3 of 3.

# Import Libraries
import time, paramiko, sys, socket
from zipfile import ZipFile


# Define functions
def menu():
    print("Which mode would you like to enter?")
    print("   1. Offensive; SSH Hacker")
    print("   2. Offensive; ZIP Hacker")
    print("   3. Defensive; Password Recognizer")
    print("   4. Quit")
    choice = input("\n(1/2/3) >>> ")
    return choice

    zip_file = "./protectme2.zip"
password = "sunday"

with ZipFile(zip_file) as zf:
  zf.extractall(pwd=bytes(password,'utf-8'))
try:
    s.login(host, username, pwd)
    s.sendline("uptime")
    s.prompt()
    print(s.before)
    s.sendline("ls -l")
    s.prompt()
    print(s.before)
    s.sendline("df")
    s.prompt()
    print(s.before)
    s.logout()

except pxssh.ExceptionPxssh as e:
    print("Pxssh failed to login.")
    print(e)
