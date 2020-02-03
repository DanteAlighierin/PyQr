#!usr/bin/python3


choise = input('CLI/gui mode?; Type C to use cli or type g to use gui:  ')

if choise == "c":
    import cli
if choise == "C":
    import cli
if choise == "g":
    import main
if choise == "G":
    import main
else:
    print("please, enter a valid letter")

