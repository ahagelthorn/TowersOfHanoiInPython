def moveCheck(n):
    print('You made',n, 'moves, the optimal solution requires 7 moves')
def countMoves(n):
    b = n + 1
    while n != b:
        n+=1
    return n
def ringCheck(firstTower,secondTower,thirdTower):  
    try:
        firstTower1 = iter(firstTower)
        for item in firstTower1:
            a = item
            b = next(firstTower1)
            if a > b:
                return 0
    except StopIteration:
        pass
    try:
        secondTower1 = iter(secondTower)
        for item in secondTower1:
            a = item
            b = next(secondTower1)
            if a > b:
                return 0
    except StopIteration:
        pass
    try:
        thirdTower1 = iter(thirdTower)
        for item in thirdTower1:
            a = item
            b = next(thirdTower1)
            if a > b:
                return 0
    except StopIteration:
        pass
    passList = [1,2,3,4]
    if thirdTower == passList or secondTower == passList:
        return 2
    return 1
def ringMove(loc, des,firstTower,secondTower,thirdTower):
    if loc == 1:
        if des == 1:
            firstTower = firstTower[len(firstTower)::-1]
            firstTower.append(firstTower[0])
            firstTower = firstTower[len(firstTower)::-1]
        if des == 2:
            secondTower = secondTower[len(secondTower)::-1]
            secondTower.append(firstTower[0])
            secondTower = secondTower[len(secondTower)::-1]
        if des == 3:
            thirdTower = thirdTower[len(thirdTower)::-1]
            thirdTower.append(firstTower[0])
            thirdTower = thirdTower[len(thirdTower)::-1]
        firstTower = firstTower[len(firstTower)::-1]
        firstTower.pop()
        firstTower = firstTower[len(firstTower)::-1]
        print(firstTower,secondTower,thirdTower)
    if loc == 2:
        if des == 1:
            firstTower = firstTower[len(firstTower)::-1]
            firstTower.append(secondTower[0])
            firstTower = firstTower[len(firstTower)::-1]
        if des == 2:
            secondTower = secondTower[len(secondTower)::-1]
            secondTower.append(secondTower[0])
            secondTower = secondTower[len(secondTower)::-1]
        if des == 3:
            thirdTower = thirdTower[len(thirdTower)::-1]
            thirdTower.append(secondTower[0])
            thirdTower = thirdTower[len(thirdTower)::-1]
        secondTower = secondTower[len(secondTower)::-1]
        secondTower.pop()
        secondTower = secondTower[len(secondTower)::-1]
        firstTower,secondTower,thirdTower
        print(firstTower,secondTower,thirdTower)
    if loc == 3:
        if des == 1:
            firstTower = firstTower[len(firstTower)::-1]
            firstTower.append(thirdTower[0])
            firstTower = firstTower[len(firstTower)::-1]
        if des == 2:
            secondTower = secondTower[len(secondTower)::-1]
            secondTower.append(thirdTower[0])
            secondTower = secondTower[len(secondTower)::-1]
        if des == 3:
            thirdTower = thirdTower[len(thirdTower)::-1]
            thirdTower.append(thirdTower[0])
            thirdTower = thirdTower[len(thirdTower)::-1]
        thirdTower = thirdTower[len(thirdTower)::-1]
        thirdTower.pop()
        thirdTower = thirdTower[len(thirdTower)::-1]
        print(firstTower,secondTower,thirdTower)
    return firstTower, secondTower, thirdTower
def ringAsk():
    firstTower = [i for i in range(1,5)]
    secondTower = []
    thirdTower = []
    userMoves = 0
    while ringCheck(firstTower,secondTower,thirdTower) == 1:
        userMoves = countMoves(userMoves)
        firstTower, secondTower, thirdTower = ringMove(int(input('Please input which tower you would like to take a ring from: ')), int(input('Please input which tower you would like to move the ring to: ')),firstTower,secondTower,thirdTower)
    if ringCheck(firstTower,secondTower,thirdTower) == 2:
        print('You win!', firstTower,secondTower,thirdTower)
        moveCheck(userMoves)
    if ringCheck(firstTower,secondTower,thirdTower) == 0:
        print('You lose!',firstTower,secondTower,thirdTower)
print('\nThe Towers of Hanoi is a mathematical game invented by Edourd Lucas in 1883.\nThe goal of the game is to move the tower of disks from the first tower to another.\nA larger disk cannot be placed on a smaller one.\n\nTry and see if you can solve this puzzle!\n')
ringAsk()
