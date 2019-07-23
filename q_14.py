#Max and Min of Random numbers and dsisplay it
import random as rn
lst=[]
for i in range(1,21):
    lst.append(rn.randint(1,50))

print(lst)
res = [max(lst),min(lst)]
print(res)