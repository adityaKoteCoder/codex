num=int(input("enter a number:"))
sum=0
for num>0:
    for i in range(1,num,1):
        sum+=1/num
        break
print(f"Result is {sum}")