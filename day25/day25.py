def calculateLoopSize(target):
    count = 0
    subjectNum = 7
    initNum = 1
    while True:
        initNum *= subjectNum
        initNum %= 20201227
        count += 1
        if initNum == target:
            return count
    return None

def getEncrypKey(card, door):
    cardLoopSize = calculateLoopSize(card)
    # doorLoopSize = calculateLoopSize(door)
    
    initNum = 1
    subjectNum = door

    for i in range(cardLoopSize):
        initNum *= door
        initNum %= 20201227

    return initNum

if __name__== "__main__":
    encry = getEncrypKey(12320657,9659666)
    print(encry)
