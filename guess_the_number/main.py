#write a program that:
#a. Stores a random number (1-10 or range decided by you) in a variable
#b. Asks a user for their name and stores this in a variable
#c. Asks a user to guess the number between 1 and 10 (or range decided by you)
#d. Tells the user whether they have guessed too high, too low or correctly
#e Gives the use a maximum of 6 goes

import random # script containing random number generator

print("Hi there, welcome to my number guessing game!\n"
      "I am thinking of a number between 1 and 50, can you guess what it is?\n"
      "I will give you 6 guesses")
username = input("So, lets get started, what's your name?\n")

def script(): #enclosing the whole program from this point in a function to allow a loop
    sysNum = random.randint(1, 50)
    #print(sysNum) #too test the code is working
    userGuess = int(input("Great, " + username + " What's your first guess?"))

    guessCount = 1
    guessMax = 5
    secondTry = (0) #a flag to indicate whether the user guesses on the first or subsequent attempts
    while guessCount <= guessMax:
        if sysNum == userGuess:
            if secondTry !=1:
                print("Wow that's amazing! You got it straight away!")
                restart = input("Do you want to have another go? (yes or no)")
                if restart == ("yes"):
                    script() #restarts the function
                else:
                    print("Ok, see you soon!")
                    break #stops the while loop
            else:
                print("Well done, you got there in the end!")
                restart = input("Do you want to have another go? (yes or no)")
                if restart == ("yes"):
                    script()
                else:
                    print("Ok, see you soon!")
                    break
        else:
            print("You have ", guessMax - guessCount+1, " guesses left")
            if sysNum>userGuess:
                print("Your guess was too low")
            else:
                print("Your guess was too high")
            userGuess= int(input("Take another turn! "))
            secondTry = (1)
        guessCount+=1
    while guessCount == 6:
        print("Oh well, better luck next time!")
        restart = input("Do you want to have another go? (yes or no)")
        if restart == ("yes"):
            script()
        else:
            print("Ok, see you soon!")
            break
script()

