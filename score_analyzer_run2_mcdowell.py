import score_analyzer_functions_mcdowell

students = int(input("How many students are in your class? "))

for i in range(students):
    name = input("What is the student's name? ")
    numgrade = int(input("What is their grade? "))
    score_analyzer_functions_mcdowell.gradeAnalyzer(numgrade)
    lettergrade = score_analyzer_functions_mcdowell.gradeAnalyzer(numgrade)
    score_analyzer_functions_mcdowell.studentRecordBuilder(name,numgrade,lettergrade)
    print(score_analyzer_functions_mcdowell.studentRecordBuilder(name,numgrade,lettergrade))