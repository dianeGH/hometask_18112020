# grading calculator

print("Hi there, welcome to the exam grade translation service")
def script():
    user_name = input("So what should we call you today?\n")
    print("Glad to meet you " + user_name)
    exam_type = input("What exam did you just sit?\n")
    print("Wow I bet that your " + exam_type + " exam was really hard!")
    grade_mark= int(input("And what mark did you get?\n"))

    if grade_mark >= 90:
        print("Your mark in " + exam_type + " is equivalent to an A*!")
    elif grade_mark >=80:
        print("Your mark in " + exam_type + " is equivalent to an A!")
    elif grade_mark >=70:
        print("Your mark in " + exam_type + " is equivalent to a B!")
    elif grade_mark >=60:
        print("Your mark in " + exam_type + " is equivalent to a C!")
    else:
        print("Your mark in " + exam_type + " is equivalent to an F!")

script()