level = int(input("LEVEL: "))

"""
Develop a program that will determine the gross pay for an employee. The company pays “straight
time” for the first 40 hours worked by each employee and pays “time-and-a-half” for all hours worked
in excess of 40 hours. You’re given the number of hours each employee worked last week and the
hourly rate of that employee. Your program should input this information for an employee and should
determine and display the employee's gross pay. 

Enter # of hours worked : 39
Enter hourly rate of the worker ($00.00): 10.00
Salary is $390.00

Enter # of hours worked : 41
Enter hourly rate of the worker ($00.00): 10.00
Salary is $415.00
"""


if(level==1):
    hours = int(input("Please enter hours worked: "))
    rate = float(input("Please enter hourly rate of the worker: "))
    
    salary = hours * rate
    if(hours > 40):
        salary += (hours-40) * rate / 2
    
    print("Salary is $", salary, sep='')
"""

2-A palindrome is a number or a text phrase that reads the same backward as forward. 
For example,each of the following five-digit integers is a palindrome: 
12321, 55555, 45554 and 11611. 
Write a program that reads in a five-digit integer and determines whether or not it’s a palindrome. 
[Hint: Use the division and remainder operators to separate the number into its individual digits.]
"""

if(level==2):
    n = int(input("Please enter digit count: "))
    number = int(input("Please enter a number: "))

    n//=2

    answer = "It's not a palindrome number."
    if ((number//10**(n+1) - number % 10**n) % 9) == 0:
        answer = "It's a palindrome number!"
    
    print(answer)

"""

3- The explosive growth of Internet communications and data storage on Internet-connected
computers has greatly increased privacy concerns. The field of cryptography is concerned with
coding data to make it difficult (and hopefully—with the most advanced schemes—impossible) for
unauthorized users to read. In this exercise you’ll investigate a simple scheme for encrypting and
decrypting data. 
A company that wants to send data over the Internet has asked you to write a
program that will encrypt it so that it may be transmitted more securely. 
All the data is transmitted as four-digit integers. Your application should read a four-digit 
integer entered by the user and encrypt it as follows: 
Replace each digit with the result of adding 7 to the digit and getting the remainder after
dividing the new value by 10. Then swap the first digit with the third, 
and swap the second digit with the fourth. Then print the encrypted integer. 
Write a separate application that inputs an encrypted four-digit integer and decrypts it 
(by reversing the encryption scheme) to form the original number. 
"""

if(level==3):
    four_digits = int(input("Please enter your password: "))    #123456
    n = len(str(four_digits))   #6
    encrypted_digits = ""

    # Shifting
    shift = four_digits % 100   #56
    four_digits += shift * (10 ** n - 1)    #56123400
    four_digits //= 10 ** 2     #561234

    # Encrypting
    for i in range(n-1, -1, -1):
        encrypted_digits += str((four_digits // 10**i + 7) % 10)    #238901
        four_digits %= 10 ** i

    print("Password saved to database: ", encrypted_digits)