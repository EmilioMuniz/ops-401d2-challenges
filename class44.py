#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class42.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  6/04/2021    
# Purpose:                  Creat port scanner.

# Import libraries:
import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 1
sockmod.settimeout(timeout)

hostip = "10.0.0.217"
portno = int(22)

def portScanner(portno):
    if sockmod.gethostbyname((hostip, portno)): # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
        print("Port closed")
    else:
        print("Port open")

portScanner(portno)
