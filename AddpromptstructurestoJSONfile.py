import json

filename = "Datasets\imdbdataset.json"
# python object(dictionary) to be dumped
prompt_structure:dict = {
        "part1": ("Write ", "Make ", "This is ", "Create ", "Show me ", "Display ", "Print ", "Reveal ", "Reaveal to me ", "Get me ", "May I a have ", "Could i have ", "Can you give to me ", "Please show me "),
        "part2": {
            "Positive": ('a glad ', 'an happy ', 'a positive ', 'a fantastic', 'an awesome', 'a contment', 'a satisfied', 'a pleased'),
            "Negative": ('an annoying ', 'an irritating ', 'an infuriating ', 'a tiresome', 'a terrible', 'a horrible', 'a negative', 'a bad'),
        },
        "part3": (' movie review', ' review of the movie', ' movie analysis', ' analysis of the movie', ' citation of the movie', 'movie judgement', 'judgement of the movie')
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
