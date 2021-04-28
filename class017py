#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class17.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  4/27/2021    
# Purpose:                  Automated Brute Force Wordlist Attack Tool Part 2 of 3.

# Import Libraries
from pexpect import pxssh
import getpass

# Declare variables:
s = pxssh.pxssh()
host = "10.0.0.215"
username = "lisav"
pwd = getpass.getpass("Password:")


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
