units=int(input("enter the units"))

if units>=1 and units<=500:
	rate=6
elif units>=501 and units<=1000:
	rate=8
elif units>1000:
	rate=12
amount=units*rate

if amount<50:
	amount=50
print(f"The amount is{amount}")
