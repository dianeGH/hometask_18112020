#Write a program that allows user to enter their favourite starter, main course, dessert and drink. Concatenate these and output a message which says – “Your favourite meal is .........with a glass of....”

def function_1():
user_name = input("Hi there, what's your name? \n")
#print ("Nice to meet you " + user_name + ". Let's find out some more about you.\n")
starter = input("I'd like to take you out for dinner. \nLet's go to your favourite restaurant! \nWhat is your favourite starter?\n")
main_meal = input("That's awesome, I love " + starter + " too!\nWhat is your favourite main meal?\n")
dessert = input("Cool, well " + main_meal+ " isn't my favourite, but I still like it!, What would your favourite dessert be? \n")
drink = input("Now a drink, I like a good Merlot, but I'm pretty easy going. What is your favourite drink?\n")

print("Well, I think we're going to have a great time! You'll have " + starter + " to start, followed by " + main_meal + " and " + dessert + " to finish, with a glass or two of " + drink + ". Shall we say Friday night? \n Great I'll book the table!!" )


