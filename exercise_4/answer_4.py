"""
4- (Coin Tossing) Write a program that simulates coin tossing. For each toss of the coin the
program should print Heads or Tails. Let the program toss the coin 100 times, and count the number
of times each side of the coin appears. Print the results. The program should call a separate function
flip that takes no arguments and returns 0 for tails and 1 for heads. [Note: If the program
realistically simulates the coin tossing, then each side of the coin should appear approximately half
the time for a total of approximately 50 heads and 50 tails.]
"""
import random

def flip()->bool:
    # Tails
    if(random.randrange(0,101) < 50):
        return False
    # Heads
    return True

if(__name__ == "__main__"):
    tailsCount = 0
    headsCount = 0
    i = 0
    while(i < 100):
        if(flip()):
            headsCount += 1
        else:
            tailsCount += 1
        
        i+=1

    print("Heads:", headsCount)
    print("Tails:", tailsCount)