#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class28.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  5/12/2021    
# Purpose:                  Create logging capabilities part 3.

# Import Libraries
import logging, time, os
from logging.handlers import RotatingFileHandler

# Define variables

# Define functions
def file_crawler(my_log):
    for (root, dirs, files) in os.walk("./" + my_log):
        print("==root==")
        print(root)
        print("==dirs==")
        print(dirs)
        print("==files==")
        print(files)


# Main
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')

logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('my_log', maxBytes=100, backupCount=1)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
print("Begin logging...")
logging.debug("Debug this...")
logging.info("Some info for you.")
logging.warning("This is your warning.")

for i in range(10):
    logmsg = "Hello world!"
    logmsg += str(i)
    logger.warning(logmsg)
    print ("Logging Hello world! number", i)
    os.system("ls -al")
    time.sleep(1)

try:
  verification() # Intentional error
except Exception as msg:
  print(msg)
  logging.exception(msg)
print("Logging finished.")

# End
# References: https://realpython.com/python-logging/#using-handlers
