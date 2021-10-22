import json

import os

files = os.listdir()

json_files = [x for x in files if x[-5:] == '.json']

print(json_files)


for file in json_files:
    with open(file, 'r') as file:
        
        data = json.load(file)
        try:
            print(file.name + ":     " + str(len(data['label'])))
        except: 
            pass
        try:
            print(file.name + ":     " + str(len(data['dataset']['label'])))
        except:
            pass
        try:
            print(file.name + ":     " + str(len(data['dataset']['train']['label'])) + len(data['dataset']['test']['label'] + len(data['dataset']['test']['label'])))
        except:
            pass
