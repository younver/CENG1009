"""
2- Let a user to enter as many number as they wants. User should enter -1 if does not want to enter
numbers any more. Find the sum of those numbers
"""
print("Enter \'-1\' to break")

sum = 0
while(True):
    temp = int(input("Please enter a number: "))

    if(temp == -1):
        break

    sum += temp

print("Sum of numbers: ", sum)