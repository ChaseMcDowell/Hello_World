#function for creating the grade
def gradescale():
    #asking for the grade and saving it as an int
    grade = int(input("Please enter a number grade: "))
    #grade logic
    if grade >= 90:
        print("Your grade of " + str(grade) + " is an A!!!")
    elif grade >= 80:
        print("Your grade of " + str(grade) + " is a B!")
    elif grade >= 70:
        print("Your grade of " + str(grade) + " is a C.")
    else:
        print("Your grade of " + str(grade) + " is an F. =(")