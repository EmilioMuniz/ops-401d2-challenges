#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class12.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  4/20/2021    
# Purpose:                  Network Security Tool with Scapy Part 2.

# Import libraries:
import ipaddress
import random
from scapy.all import ICMP,IP,sr1,TCP

# Declaration of variables:
host = "10.0.0.129"
port_range = [22, 23, 80, 443, 3389]
network = "10.0.0.0/24"
ip_list = ipaddress.ip_network(network)
hosts_count = 0



# Declaration of functions:

def range_scanner():
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

def network_address():
    address = input("\nEnter Network Address:\n")

def ping_sweep():
    for host in ip_list:
        network_address()
        print("Pinging ",host,", please wait...")
        response = sr1(
            IP(dst=str(host))/ICMP(),
            timeout=2,
            verbose=0
        )
    
        if response is None:
            print(f"{host}:{dst_port} is unresponsive.")
    
        elif(response.haslayer(ICMP)):
            if(
                int(response.getlayer(ICMP).type) == 3 and
                int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]
            ):
                print(f"{host}:{dst_port} is actively blocking ICMP).")

def ask_user():
    mode = input("\nSelect a Mode: \nMode 1: TCP Port Range Scanner \nMode2: ICMP Ping Sweep\n")
    if (mode == 1):
        range_scanner
    elif(mode == 2):
        ping_sweep


# End

# References:
