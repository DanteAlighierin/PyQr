#!/usr/bin/python3

from pyqrcode import create


url = create("https://vk.com")
url.svg('faf.svg', scale =8)
print(url.terminal(quiet_zone=1))
