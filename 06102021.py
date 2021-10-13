level = int(input("LEVEL: "))

"""

1-Create an application that calculates your daily driving cost, 

so that you can estimate how much money could

be saved by car pooling, which also has other advantages such as 

reducing carbon emissions and reducing

traffic congestion. The application should input the following 

information and display the user’s cost per day of

driving to work:

a) Total miles driven per day.

b) Cost per gallon of gasoline.

c) Average miles per gallon.

d) Parking fees per day.

e) Tolls per day.
"""


if(level==1):

    # MPG => Miles Per Gallon

    milesPerDay = float(input("Please enter total miles driven per day: "))

    costPerGallon = float(input("Please enter cost per gallon of gasoline: "))

    avarageMPG = float(input("Please enter avarage miles per gallon: "))

    parkingFee = float(input("Please enter parking fees per day: "))

    tollsPerDay = float(input("Please enter tolls per day: "))


    dailyDrivingCost = milesPerDay / avarageMPG * costPerGallon + parkingFee + tollsPerDay


    print(dailyDrivingCost)
"""

2- Create a BMI calculator application that reads the user’s 

weight in kg and height in meters then calculates and

displays the user’s body mass index. Also, the application 

should display the following information from

the Department of Health and Human Services/National 

Institutes of Health so the user can evaluate his/her BMI:

BMI VALUES

Underweight: less than 18.5

Normal: between 18.5 and 24.9

Overweight: between 25 and 29.9

Obese: 30 or greater


The formula von Body Mass Index:

BMI = weight(kg)/height(m)*height(m)
"""

if(level==2):

    weight = float(input("Please enter weight in kg: "))

    height = float(input("Please enter height in m: "))


    bmi = weight/height**2

    detail = "Underweight" if bmi < 18.5 else "Normal" if bmi < 24.9 else "Overweight" if bmi < 29.9 else "Obese"


    print(f"Body Mass Index: {bmi}\n{detail}")

"""

3- Write a program that inputs one five-digit number, 

separates the number into its individual digits and prints

the digits separated from one another by three spaces each. 

[Hint: Use combinations of integer division and the

remainder operation.] For example, if the user types in 42139, 
the program should print

4 2 1 3 9
"""

if(level==3):

    # n + (n-1)*spaces - 1

    n = int(input("Please enter character count: "))
    spaces = int(input("Please enter the desired spaces between two characters: "))
    number = int(input("Please enter a number: "))


   
    # Algorithm 1
    """
    length = n + (n-1)*spaces - 1

    for i in range(length, -1, -(spaces+1)):
        print('\r', (i)*' ', number % 10, end='', sep='')
        number //= 10
    """
    # Algorithm 2
    for i in range(n-1,-1,-1):
        print(number // 10**i, spaces * ' ', sep='', end='')
        number %= 10**i
