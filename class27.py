#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class27.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  5/11/2021    
# Purpose:                  Create logging capabilities part 2.

# Import Libraries
import logging
import os


# Define variables
logger = logging.getLogger('my_logger')
handler = RotatingFileHandler('my_log.log', maxBytes=30, backupCount=1)
logger.addHandler(handler)


# Main
logging.basicConfig(filename="./sample.log", level=logging.ERROR, format="%(asctime)s:%(levelname)s:%(message)s")
print("Begin logging...")
logging.debug("Debug this...")
logging.info("Some info for you.")
logging.warning("This is your warning.")

try:
  verification() # Intentional error
except Exception as msg:
  print(msg)
  logging.exception(msg)
print("Logging finished.")

for i in range(10):
    logmsg = "Hello world!"
    logmsg += str(i)
    logger.warning(logmsg)
    print ("Logging Hello world! number", i)
    os.system("ls -al")
    time.sleep(1)
