def cast_vote(age):
    assert age >= 18 , f"Age shouldnt be < 18,it was :{age}"
    print(thank you for voting..)

try:
    age = int(input("ente rthe age"))
    cast_vote(age)

except AssertionError as a:
    print(a)
    else
