"""
5- (Greatest Common Divisor) The greatest common divisor (GCD) of two integers is the largest
integer that evenly divides each of the two numbers. Write function gcd that returns the greatest
common divisor of two integers.
"""
def findGCD(num1:int, num2:int)->int:
    # Optimization
    if(num1 < num2):
        i = num1
    else:
        i = num2

    while(i > 0):
        if not (num1%i or num2%i):
            return i
        i -= 1

x = int(input("Please enter an integer: "))
y = int(input("Please enter another integer: "))
print(findGCD(x, y))