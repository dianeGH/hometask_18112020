# password checking programme
# to pass the input must be >7 characters,  and contain at
# least 1 of number, upper, lower and spec characters.

# user input
def script():
    print("Your password must be 7 characters in length, have one number, one\n"
          "special character, one uppercase and one lowercase letter")
    password = input("Please enter your password here\n")
    check_password = input("Please re - enter your password here\n")
    if password == check_password:
        print("you have chosen " + password + " as your password\n")
    else:
        print("Your passwords don't match, try again")
        script()

    # Variables - case types
    uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                 "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special = ["!", "@", "£", "%", "^", "&", "*", "~"]

    # counts
    u_case = 0
    l_case = 0
    n_case = 0
    s_case = 0

    for letter in password:
        if letter in uppercase:
            u_case +=1
        if letter in lowercase:
            l_case +=1
        if letter in numbers:
            n_case +=1
        if letter in special:
            s_case +=1

    if len(password)>7:
        if u_case >=1 and l_case >=1 and n_case >=1 and s_case >=1:
            print("Your password meets our requirements")
        elif u_case >=1 and l_case >=1 and n_case >=1 and s_case <1:
            print("Your password is missing a special character, please try again\n"
                  "Your password must be 7 characters in length, have one number, one\n"
                  "special character, one uppercase and one lowercase letter\n")
            script()
        elif u_case >= 1 and l_case >= 1 and n_case <1 and s_case >= 1:
            print("Your password is missing a number, please try again.\n"
                  "Your password must be 7 characters in length, have one number, one\n"
                  "special character, one uppercase and one lowercase letter\n")
            script()
        elif u_case >= 1 and l_case <1 and n_case >= 1 and s_case >=1:
            print("Your password is missing a lower case letter, please try again\n"
                  "Your password must be 7 characters in length, have one number, one\n"
                  "special character, one uppercase and one lowercase letter\n")
            script()
        else:
            print("Your password is missing an upper case letter, please try again\n"
                  "Your password must be 7 characters in length, have one number, one\n"
                  "special character, one uppercase and one lowercase letter\n")
            script()
    else:
        print("Your password is too short please try again\n"
              "Your password must be 7 characters in length, have one number, one\n"
              "special character, one uppercase and one lowercase letter\n")
        script()

    if len(password)>9 and u_case >=3 and l_case >=3 and n_case >=3 and s_case>=3:
        print("You have picked a strong password!!")
    elif len(password)>8 and u_case >=2 and l_case >=2 and n_case >=2 and s_case>=2:
        print("You have picked a medium strength password!")
    else:
        print("You have picked a weak password.")

script()
