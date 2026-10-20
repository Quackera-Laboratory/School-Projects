import json

PATH = "practice.json."

scores = {"x":0,"o":0}
def save_scores(path, score):
    with open(path, mode = "w") as file:
        json.dump(scores, file)
def load_scores(path,):
    with open(path, mode = "r") as file:
        scores = json.load(file)
        return scores

save_scores(PATH, scores)
score = load_scores(PATH)
print(scores)
scores["x"] += 1
scores["o"] += 2
print(scores)

save_scores(PATH,scores)

save_scores('new/practice.json', scores)

def reset_scores(scores):
    scores["x"] = 0
    scores["0"] = 0
    save_scores(PATH, scores)

with open(PATH, mode = "w") as file:
    json.dump(scores, file)