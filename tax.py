#Program to calculate the tax

income=float(input("Enter Income: "))

if income<=500000:
	Tax=0
elif income<=10000:
	temp=income-500000
	Tax=temp*0.10
elif income>=100000:
	temp=income-500000
	temp1=temp-500000
	tax1=500000*0.1
	tax2=temp1*0.3
	Tax=tax1+tax2
print(f"income{income} with tax of {Tax}")