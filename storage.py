#import json
#import os

# FILE_NAME = "tasks.json"

# def load_tasks():
  #  if not os.path.exists(FILE_NAME):
 #       return []
   # with open(FILE_NAME, "r") as file:
    #    return json.load(file)

#def save_tasks(tasks):
   # with open(FILE_NAME, "w") as file:
      #  json.dump(tasks, file, indent=4)



import json
import os

FILE_NAME = "tasks.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return {"tasks": [], "points": 0}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

        