import random
scores = []
def getGrade(value):
    if value > 89:
        return "A"
    elif value <= 89 & value > 79:
        return "B"
    elif value <= 79 & value > 69:
        return "C"
    elif value <= 69 & value > 59:
        return "D"
    elif value < 60:
        return "F"
    return value

# Randomly, geGrade fails the comparison, and was returning none
# So, I set it to return value if it fails.
# I am not sure why
print "Scores and Grades"
for x in range(0, 10):
    scores.append(random.randint(60, 100))
    grade = getGrade(scores[x])
    print "Score:", scores[x], "Your grade is", grade
print "End of the program. Bye!"