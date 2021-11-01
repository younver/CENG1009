"""
1-Let a computer generate a random number between 1 and 100, but do not show this number to the
user. Then, let user to try to guess this number. If the number that user entered is greater or lesser than
this random number give an appropriate message and let user to enter another number. This process
should continue until a user guess it right. Congragulate the user and print the number of tries.
"""
import random

randomNumber = random.randrange(1,100)
print("Ada | I have a number in my mind. Can you guess it? :3", randomNumber)

limit = 1
while(limit < 6):
    guessNumber = int(input("You | I guess it issss: "))
    if(guessNumber==randomNumber):
        print("Ada | No wayy! You made it in just", limit, "tries.")
        break
    print("Ada | Nope, it isn't.")
    limit+=1

print(f"Ada | It was {randomNumber}.")