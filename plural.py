str=input("enter the string:")
if str.endswith('y'):
    str = str.replace('y','') + 'ies'
else:
    str=str+'s'
print(str)