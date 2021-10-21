import json

filename = "Datasets\summarizedataset.json"
# python object(dictionary) to be dumped
prompt_structure:dict = {
        "part1": ('Summarize ', 'Compress ', 'Condense ', 'summarize ', 'compress ', 'condense ')
        # "part2": {
        #     "sadness": ('a sad', 'an unhappy', 'a depressed', 'a sorrowful', 'a', 'a not so happy', 'an unglad', 'a not glad', 'melancholic'),
        #     "joy": ('a happy', 'a joyful', 'a glad', 'a delightful', 'a', 'a gleefull'),
        #     "love": ('a', ),
        #     "anger": ('a sad', 'an unhappy', 'a depressed', 'a sorrowful', 'a', 'a not so happy', 'an unglad', 'a not glad', 'melancholic'),
        #     "fear": ('a scarred', 'a fearful', 'a'),
        #     "surprise": ('a surpised', 'unexpected', 'a'),
        # },
        # "part3": (' sentence', ' statement', ' piece of text', ' quote', ' citation')
    }

# the json file where the output must be stored
with open(filename, "r") as file:
    data = json.load(file)

_dataset = {
    'prompt_structure': prompt_structure,
    'dataset': data
}

with open(filename, "w") as file:
    json.dump(_dataset, file)

file.close()
