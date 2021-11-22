from random import randint


def findMax(anyList:list):
    """ Returns maximum value in a list """
    max = anyList[0]
    for element in anyList:
        if element > max:
            max = element

    return max

def dropCoin(moveCount:int)->int:
    """ Returns chamber index that coin just dropped """
    chamber = 0
    for _ in range(moveCount):
        if(randint(0,1)):
            chamber += 1
    
    return chamber

def setChambers(coinCount:int, chamberCount:int, moveCount:int)->list:
    """ Returns a list whiches elements represents coin amount in chamber and indexes represent chambers respectively """
    chambers = [0] * chamberCount
    for i in range(coinCount):
        chambers[dropCoin(moveCount)] += 1 
        
    return chambers

def produceOutput(chamberList:list, maxChamber:int):
    """ Returns an output in given format """
    maxCoinCount = findMax(chamberList)
    output = ""
    output2 = len(str(maxCoinCount)) * ' ' + '|'

    space = (len(str(maxChamber)) // 2) * 2 + 1
    
    # Iterate through rows till tail
    for row in range(maxCoinCount):
        currentCoinCount = maxCoinCount - row
        output += (len(str(maxCoinCount)) - len(str(currentCoinCount)))*' ' + str(currentCoinCount) + "|"
        
        for i in range(maxChamber):
            output += space//2*' '
            output += ('X' if (chamberList[i] >= currentCoinCount) else ' ') 
            output += space//2*' ' + '|'
        output += '\n'


    output += len(str(maxCoinCount)) * '-' + '+'


    # Iterate through chambers till maxChamber
    for chamber in range(1, maxChamber+1):
        output += space*'-' + '+'
        # If 
        temp = (space - len(str(chamber)))
        output2 += ((temp > 0) * ' ') + str(chamber) + ((temp > 1) * ' ')
        output2 += ' '


    # The End
    output2 += '|'
    return output + '\n' + output2


if(__name__ == "__main__"):
    coinNumber = int(input("Please enter the number of coins to drop: "))
    chamberNumber = int(input("Please enter the number of chambers: "))
    moves = chamberNumber - 1

    chambers = setChambers(coinNumber, chamberNumber, moves)
    print(produceOutput(chambers, chamberNumber))
    print(chambers)
