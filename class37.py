#!/usr/bin/env python3

# Script:                   ops-401d2-challenge-class37.py                       
# Author:                   Emilio Muniz                       
# Date of latest revision:  5/25/2021    
# Purpose:                  Cookie Capture.

# Import libraries:
import requests

# Declare variables:
targetsite = "http://www.whatarecookies.com/cookietest.asp"
response = requests.get(targetsite)
cookie = response.cookies
print("Target site is " + targetsite)
print("Response cookie: " + str(cookie))


response = requests.get(targetsite, cookies=cookie)
cookie2 = response.cookies
print("Target site is " + targetsite)
print("Response cookie: " + str(cookie))
print(response.text, file = open("./class-37.html", "a"))
print("Response saved as response.html")

# End
