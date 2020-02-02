#!usr/bin/python3



choise = input('CLI/gui mode?; Type C to use cli or type g to use gui')

if choise == 'c' or 'C':
    import cli.py

if choise == 'g' or 'G':
    pass

else:
    print('sorry, please type right letter')
