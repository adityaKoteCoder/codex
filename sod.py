n = int(input("enter the number"))
sum = 0
while n>0:
    rem=n%10
    sum = sum + rem
    n = n//10
print(f"the total number is:{sum}")