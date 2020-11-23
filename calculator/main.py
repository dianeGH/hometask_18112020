print ("Welcome to your handy calculator!\nSo tell me what type of calculation you want to complete today\n"
       "a for addition\n"
       "b for subtraction\n"
       "c for multiplication\n"
       "d for division\n"
       "e for a square root\n"
       "or\n"
        "f for the power of\n")
calc_type= input ("a,b,c,d,e,or f\n")
print ("Great, now lets get some numbers from you")
no_one = int(input ("Please enter your first number\n"))

if calc_type == "a":
    no_two = int(input("please enter your second number here\n"))
    print(no_one, "+",no_two, "=", no_one + no_two)
elif calc_type == "b":
    no_two = int(input("please enter your second number here\n"))
    print(no_one, "-",no_two, "=", no_one - no_two)
elif calc_type == "c":
    no_two = int(input("please enter your second number here\n"))
    print(no_one, "x",no_two, "=", no_one * no_two)
elif calc_type == "d":
    no_two = int(input("please enter your second number here\n"))
    print(no_one, "/",no_two, "=", no_one / no_two)
elif calc_type == "e":
    print(no_one, "squared =", no_one * no_one )
else:
    no_two = int(input("please enter your second number here\n"))
    print(no_one, "^",no_two, "=", no_one ** no_two)