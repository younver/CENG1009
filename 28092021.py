while 1:
    try:
        ex = eval(input("Expression: "))
        answer = eval(input("Answer: "))
        if answer == ex:
            ex = "TRUE"
        print(ex, "\n")
    except:
        break

"""
Expression: 5**2
Answer: 25
TRUE        

Expression: 9*5
Answer: 45
TRUE        

Expression: 15/12
Answer: 1.25
TRUE        

Expression: 12/15
Answer: 0.8
TRUE        

Expression: 15//12
Answer: 1
TRUE 

Expression: 12//15
Answer: 0
TRUE 

Expression: 5%2
Answer: 1
TRUE 

Expression: 9%5
Answer: 4
TRUE 

Expression: 15%12
Answer: 3
TRUE 

Expression: 12%15
Answer: 12
TRUE 

Expression: 6%6
Answer: 0
TRUE 

Expression: 0%7
Answer: 7
TRUE
"""
