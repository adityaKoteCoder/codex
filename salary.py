salary=float(input("enter the salary: "))
if salary<0:
	salary =- (salary)
salary = salary+(salary*0.1)
print(f"salary = {salary}")
input('')