"""
3- Let a user to enter as many number as they wants. User should enter -1 if does not want to enter
numbers any more. Find the minimum of those numbers.
"""
print("Enter \'-1\' to break")

minimum = int(input("Please enter a number: "))
while(True):
    temp = int(input("Please enter a number: "))
    if(temp == -1):
        break
    if(temp < minimum):
        minimum = temp

print("Minimum number: ", minimum)