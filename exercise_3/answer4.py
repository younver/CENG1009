"""
Write a function that take an integer as a parameter and returns the factorial of it
"""
# Algo
def factorial(num:int)->int:
    for i in range(1,num):
        num *= i
    
    return num

if __name__ == "__main__":
    # Input
    x = int(input("Please enter an integer: "))

    # Output
    print(factorial(x))