#imports the function
import score_analyzer_function_mcdowell

#asking for the amount of grades the user will enter
numberOfScores = int(input("How many grades would you like to enter: "))

# runs the loop the number of times the y senter a grade
for i in range(numberOfScores):
    score_analyzer_function_mcdowell.gradescale()