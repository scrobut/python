import random
def playGameAdvin():

    print("***** on the game *****")
    numberAcert = random.randrange(1, 101)
    point = 1000
    print("difficulty level", numberAcert)
    print("(1) Easy - (2) Medium - (3) Hard")
    levelStr = input("Level: ")
    level = int(levelStr)

    if (level == 1):
        maxTries = 10
    else:
        if (level == 2):
            maxTries = 6
        elif (level == 3):
            maxTries = 3

    for round in range(1, maxTries + 1):
        print("try {:2d} of the {:2d}".format(round, maxTries))
        shootStr = input("Digit a number:")
        numberSecret = int(shootStr)
        print("your number", shootStr)

        if (numberSecret < 1):
            print("please, number 0 is invalid")
            continue
        done = numberSecret == numberAcert
        big = numberSecret > numberAcert
        small = numberSecret < numberAcert

        if (done):
            print("acert, points: {}".format(point))
            break
        else:
            if (big):
                print("big")
            elif (small):
                print("small")
        print("please try again", end="!\n")
        pointLoss = abs(numberAcert - numberSecret)
        point = point - pointLoss

if(__name__ == "__main__"):
    playGameAdvin()

