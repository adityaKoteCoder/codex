lob = int(input("enter the number lower bound"))
upb= int(input("enter the number upper bound"))

for num in range (lob,upb+1):
    if num%9 ==0 and num%5 != 0:
        print(f"{num}")