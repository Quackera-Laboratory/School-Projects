student_scores = {}

student_scores["Luna"] = 97
student_scores["Jack"] = 80
student_scores["CiCi"] = 85
student_scores["CiCi"] += 5
for names in student_scores.keys():
    print(names)
for score in student_scores.values():
    print(score)
for name, score in student_scores.items():
    print(f"{name}'s score is {score}.")