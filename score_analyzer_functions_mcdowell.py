def gradeAnalyzer(numGrade):
    #grade logic
    if numGrade >= 90:
        return "A"
    elif numGrade >= 80:
        return "B"
    elif numGrade >= 70:
        return "C"
    else:
        return "F"

def studentRecordBuilder(name,numgrade,lettergrade):
    studentRecord = [name,numgrade,lettergrade]
    return studentRecord