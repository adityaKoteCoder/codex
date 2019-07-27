try:
    num1 = int(input("enter the num1:"))
    num2 = int(input("enter the num2:"))
    print(num1**num2)
    print(num1//num2)
    print ("Sum is:"+num1+num2)

except ZeroDivisionError:
    print("")

except Exception as e:
print(f "{e}")

