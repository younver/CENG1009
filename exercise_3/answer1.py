"""
Write a program that prints the following patterns separately. Write a function for each of the
patterns. All of the asterisk(*) should be printed separately like print(“*”). (hint: last two patterns
require that each line begins with an appropriate number of blanks.)
"""
# Normal Algo
def leftBottomLedder(size:int)->str:
    output = ""
    for i in range(size):
        for j in range(i+1):
            output += '*'
        output += '\n'

    return output

def leftTopLedder(size:int)->str:
    output = ""
    for i in range(size, 0, -1):
        for j in range(i):
            output += '*'
        output += '\n'
    
    return output

def rightTopLedder(size:int)->str:
    output = ""
    for i in range(size):
        for j in range(i):
            output += ' '

        for j in range(size-i):
            output += '*'
        output += '\n'

    return output

def rightBottomLedder(size:int)->str:
    output = ""
    for i in range(size-1, -1, -1):
        for j in range(i):
            output += ' '
        
        for j in range(size-i):
            output += '*'
        output += '\n'
    
    return output

# Fast Algo
def fastLeftBottomLedder(size:int)->str:
    output = ""
    for i in range(1, size+1):
        output += i * '*' + '\n'

    return output

def fastLeftTopLedder(size:int)->str:
    output = ""
    for i in range(size, 0, -1):
        output += i * '*' + '\n'
    
    return output

def fastRightTopLedder(size:int)->str:
    output = ""
    for i in range(size):
        output += i * ' ' + (size-i) * '*' + '\n'

    return output

def fastRightBottomLedder(size:int)->str:
    output = ""
    for i in range(size-1, -1, -1):
        output += i * ' ' + (size-i) * '*' + '\n'
    
    return output


if __name__ == "__main__":
    # Input
    n = int(input())

    # Output
    print(fastRightBottomLedder(n))