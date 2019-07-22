#accept a number from the uder and display if it is a palindome or not

def reverse_num(num):
    num=int(input("enter the number"))
    rev=0
    while num!=0:
        rev=rev*10+num%10
        num=num/10
print(f"{num} is a palindrome")
        
