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

different_scores = {}

different_scores["olympics"] = 160
different_scores["PEPS"] = 40
different_scores["evo"] = 9

for Medal_count in different_scores.values():
    if Medal_count >= 40:
        print(Medal_count)
for Medal_count in different_scores.values():
    if Medal_count <= 159:
        print(different_scores)
        
for Medal_count in different_scores.keys():
    different_scores[Medal_count] *=10
print(different_scores)

Player_scores = {}

Player_scores["Billy Mitchel"] = 1
Player_scores["Dream"] = 1
Player_scores["ZeR0"] = 0
Player_scores["Spyro&Cynder"] = 0

for disgraces in Player_scores.keys():
    print(disgraces)
for cheater_values in Player_scores.values():
    if cheater_values == 1:
        print("Cheater")
