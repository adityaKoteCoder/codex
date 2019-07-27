num = int(input("enter the number :"))
count = 0
while num>0:
    digit = num%10
    if digit == 2 or 3 or 5 or 7:
        count=count+1
    else:
        count=count+0
    num=num//10
print(count)