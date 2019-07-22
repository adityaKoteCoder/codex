#Program to find the biggest of two numbers

num1=int(input("enter the number 1:"))
num2=int(input("enter the number 2:"))
num3=int(input("enter the number 3:"))

if num1>num2 and num1>num3:
	big=num1
elif num2>num3:
	big=num2
else:
	big=num3
print(f"Between {num1} and {num2} and {num3} is {big}")