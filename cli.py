#!/usr/bin/python3


from pyqrcode import create #import libs


url = create("https://vk.com")
url.svg('code.svg', scale=8) #good naming; image scaling
print(url.terminal(quiet_zone=2)) #border
