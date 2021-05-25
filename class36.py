#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class36.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  5/24/2021    
# Purpose:                  Fingerprinting Part 1 of 3.

# Import libraries:
import os, sys, socket

# Declare variables:

# Define functions:
def netcat_grab():
    ip=input("Enter ip address:")
    port=input("Enter port number:")
    os.system("nc" + str(ip) + str(port))

def telnet_grab():
    ip=input("Enter ip address:")
    port=input("Enter port number:")
    os.system("telnet" + str(ip) + str(port))

def nmap_grab():
    ip=input("Enter ip address:")
    port=input("Enter port number:")
    os.system("nmap" + str(ip) + str(port))

# Main
netcat_grab()
telnet_grab()
nmap_grab()

# End
