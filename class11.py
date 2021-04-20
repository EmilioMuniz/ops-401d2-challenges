#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class11.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  4/19/2021    
# Purpose:                  Network Security Tool with Scapy Part 1.

# Import libraries:
import sys
from scapy.all import ICMP, IP, sr1, TCP

# Declaration of variables:
host = "scanme.nmap.org"
port_range = 22
src_port = 22
dst_port = 22

response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)

# Declaration of functions:

# Main
print(response)

# End

# References:
