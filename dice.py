import random
num=random.randint(1,6)
count=0
while True:
    guess = int(input("enter the values b/w 1-6:"))
    if  guess == num:
        count += 1
        print(f"you guessed number in {count} attempts")
        break
    elif guess<num:
        print("Guessed number is less than the actual numner")
        count+=1
    else:
        print("Guessed number is more than the actaual number")
        count += 1
    if count==3:
        print("Better luck next time")
        break