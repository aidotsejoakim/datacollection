import json

import os

files = os.listdir()

json_files = [x for x in files if x[-5:] == '.json']

print(json_files)


for file in json_files:
    with open(file, 'r') as file:
        try:
            data = json.load(file)
            print(file.name + ":     " + str(len(data['label'])))
        except:
            print("Could not read: " + file.name)
