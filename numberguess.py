import random

def checkIfNumber(user_guess):
    if(user_guess.isnumeric()):
        return True
    else:
        print("the number that you have entered is not a valid number.")
        return False

def checkIfInRange(user_guess):
    if( (1 <= user_guess) and (user_guess <= 100)):
        return True
    else:
        print("the number you have entered is not in the 1-100 range, please try again")
        return False


def getValidValue():
    while(True):
        UserGuess = input("please guess a number in range from 1 to 100:")
        if(checkIfNumber(UserGuess)):
            UserGuess = int(UserGuess)
            if(checkIfInRange(userGuess)):
                return UserGuess

def main():
    SavedNumber = random.randint(1,100)
    NumberofSteps = 0
    UserGuess = 0

    while(UserGuess !=SavedNumber):
        UserGuess = getValidValue()

        if(SavedNumber == UserGuess):
            print("you are the winner! After", NumberOfSteps, "steps")
        elif(SavedNUmber > UserGuess):
            print("The number is too small")
            NumberOfSteps = NumberOfSteps + 1
        else:
            print("the number is too big")
            NumberOfSteps = NumberOfSteps + 1
    print("Goodbye")
    
