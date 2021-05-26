#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class36.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  5/24/2021    
# Purpose:                  Fingerprinting Part 1 of 3.

# Import libraries:
import requests

# Declare variables:
cookies = dict(name='ASPSESSIONIDCAAAQSTQ=DCPHAALCMALIHMCMPIFCIEIE')
targetsite = "http://www.whatarecookies.com/cookietest.asp"
response = requests.get(targetsite)
cookie = response.cookies
response = requests.get(targetsite, cookies=cookies)

# Define functions:
def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

# Main
bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)
 
# End
