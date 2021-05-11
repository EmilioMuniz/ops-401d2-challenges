#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class26.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  5/10/2021    
# Purpose:                  Create logging capabilities.

# Import Libraries
import logging
import os


# Define functions


# Main
logging.basicConfig(filename="./example2.log", level=logging.ERROR, format="%(asctime)s:%(levelname)s:%(message)s")
print("Begin logging...")
try:
  verification() # Intentional error
except Exception as msg:
  print(msg)
  logging.exception(msg)
print("Logging finished.")
