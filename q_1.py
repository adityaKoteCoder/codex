import math

num = int(input("enter the number"))
is_prime = True
if num < 2:
	is_prime = False
    
else:
	for i in range(2,num//2 + 1):
		if num%2==0:
			is_prime = False
			break

if is_prime:
	print(f"{num} is a prime number")
else:
	print(f"{num} is a prime number")	