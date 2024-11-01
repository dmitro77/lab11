import csv
import random

with open("task1/quest.csv", "r") as f:
    reader = csv.reader(f)
    questionList = []
    for row in reader:
        questionList.append(row[2])
    random.shuffle(questionList)
    for q in questionList:
        print(q)
