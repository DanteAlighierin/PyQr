#!/usr/bin/python3


from pyqrcode import create #import libs



print("please,type url:")#hello
url = create(input(''))#take value from your input




url.svg('code.svg', scale=8) #good naming; image scaling
print(url.terminal(quiet_zone=2)) #border
