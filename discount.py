amount=int(input("enter the amount"))
if amount>=10000 :
   discount=amount*0.2
else:
   discount=amount*0.5

net_amount=amount-discount
print(f"Bill amount;{amount},Discount;{discount},Net Amount : {net_amount}")