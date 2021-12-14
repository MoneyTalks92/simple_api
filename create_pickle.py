import json
import pickle

f = open("projects.json")

data = json.load(f)

with open("projects.pickle", "wb") as file:
  pickle.dump(data, file)

f.close()