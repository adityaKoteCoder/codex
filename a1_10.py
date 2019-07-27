n = int(input("enter the number")) 
for x in range(1,n+1):
    print(((10**x - 1)//9)**2)