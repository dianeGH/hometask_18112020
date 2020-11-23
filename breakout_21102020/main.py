def function_favmeal():
    name= input("Good evening, What is your name?\n")
    starter = input("Choose your favourite starter\n")
    main = input("Choose your favourite main dish\n")
    dessert = input ("and your favourite pudding\n")
    drink = input ("and what would you like to drink?\n")

    output = ("So "+ name + ", dinner will be \n" +starter+ " followed by " + main +
           " and " +dessert + " to follow, all with a nice glass of " +drink+ " or two?")
    return output

message = function_favmeal()
print(message)

