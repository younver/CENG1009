"""
Write a function that takes two integer paramaters and 
decides whether the fist one is divisible by the second.
"""
# Algo
def isDivisible(num1:int, num2:int)->bool:
    return not (num1 % num2)

if __name__ == "__main__":
    # Input
    x = int(input("Please enter first integer:"))
    y = int(input("Please enter second integer:"))

    # Output
    print(isDivisible(x, y))