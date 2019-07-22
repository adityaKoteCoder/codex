#Program to find the reciprocal of factorial

num=int(input("enter a number:"))
if num>0:
    for i in range(1,num,1):
        fact=1
        for j in range(1,num,1):
            fact=fact*j
        sum+=1/fact
print(f"Result is {sum}")
