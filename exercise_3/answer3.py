"""
Let user to enter a number and decide whether that number is a 
prime number or not. Try to write a function while solwing this one.
"""
# Algo
def isPrime(num:int)->bool:
    for i in range(2, num//2):
        if not (num % i):
            mark = i
            return False
        
    return True

if __name__ == "__main__":
    # Input
    x = int(input("Please enter a number: "))

    # Output
    print(isPrime(x))