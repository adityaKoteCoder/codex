import random as rn
lst = []
for i in range(1,101):
    lst.append(rn.randit(1,101))

if i % 3 == 0 and i % 6 == 0 and i % 9 != 0:
    print(f" {i} number is divisible")
else:
     print(f" {i} number is not divisible")