import json

wordCounter = dict()
with open("task2/book.txt") as f:
    allWords = (f.read()).split(" ")
    for word in allWords:
        wordLength = len(word)
        try:
            wordCounter[wordLength].append(word)
        except Exception:
            wordCounter[wordLength] = []
            wordCounter[wordLength].append(word)

with open("task2/result.json", "w") as f:
    json.dump(wordCounter, f)
