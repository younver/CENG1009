from answer4 import factorial

"""
Write a function that takes an integer n as a parameter and calculates the e using the
formula below
e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
"""
# Algo
def formula(n:int):
    e = 1
    for i in range(1, n+1):
        e += 1 / factorial(i)

    return e

if __name__ == "__main__":
    # Input
    x = int(input("Please enter an integer: "))

    # Output
    print(formula(x))