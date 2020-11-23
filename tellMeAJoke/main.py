#Write a program that asks a user for their favourite number between 1 and 100 and then tells them a joke based on the number. You should use a minimum of 3 jokes.
user_input = input("Hi there, What's your name?\n")
like_jokes = input("Well hello there "+ user_input+ ". Do you like jokes? (answer yes or no)\n")

if like_jokes == "yes":
    pick_number = int(input("That's great!! pick a number between 1 and 100\n"))
    print ("knock knock\n")
    input ()
    if pick_number <= 20:
        print ("idunnap")
        input ()
        print ("urgh go and change your pants!!")
    elif pick_number <= 40:
        print("orange")
        input()
        print("orange you glad I didn't say bananas")
    elif pick_number <= 60:
        print("doctor")
        input()
        print("wooo-oo-o woo-oo-o")
    elif pick_number <= 80:
        print("adore")
        input()
        print("adore is between us, please open up")
    else:
        print("hike")
        input()
        print("I didn't know you liked japanese poetry!")
else:
    print("oh well, this isn't the programme for you, see you later.")
