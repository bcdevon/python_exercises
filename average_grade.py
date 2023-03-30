negative_score = False
total_score = 0
course_total = 0
while negative_score == False:
    score = input("Enter Test Score: ")
    score = int(score)
    if score >= 0:
        total_score += score
        course_total += 1
    elif score < 0:
        print(total_score/course_total)
        negative_score = True
