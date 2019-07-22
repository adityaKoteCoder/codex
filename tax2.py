#Program to calculate the tax

income=float(input("Enter Income: "))
basic=500000
if income<=basic:
	tax=0
elif income<=basic and income< 1000000:
	temp=income-500000
	tax=temp*0.10
else:
	tax=(income-1000000)*0.3+basic*0.1
print(f"income={income}, tax= {tax}")