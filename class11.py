#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class11.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  4/20/2021    
# Purpose:                  Network Security Tool with Scapy Part 1.

# Import libraries:
import random
from scapy.all import ICMP,IP,sr1,TCP

# Declaration of variables:
host = "10.0.0.129"
port_range = [22, 23, 80, 443, 3389]



# Declaration of functions:

# Main Run With Sudo
for dst_port in port_range:
    src_port = random.randint(1025,65534)
    response = sr1(
        IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,
        verbose=0
    )

    if response is None:
        print(f"{host}:{dst_port} is filtered (silently dropped).")

    elif(response.haslayer(TCP)):
        if(response.getlayer(TCP).flags == 0x12):
            send_rst = sr(
                IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),
                timeout=1,
                verbose=0,
            )
            print(f"{host}:{dst_port} is open.")

        elif(response.getlayer(TCP).flags == 0x14):
            print(f"{host}:{dst_port} is closed.")

    elif(response.haslayer(ICMP)):
        if(
            int(response.getlayer(ICMP).type) == 3 and
            int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]
        ):
            print(f"{host}:{dst_port} is filtered (silently dropped).")


# End

# References:
