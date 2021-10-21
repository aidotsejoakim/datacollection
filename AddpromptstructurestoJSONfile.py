import json

filename = "Datasets\goEmotionsDataset.json"
# python object(dictionary) to be dumped
prompt_structure:dict = {
        "part1": ("Write ", "Make ", "This is ", "Create ", "Show me ", "Display ", "Print ", "Reveal ", "Reaveal to me ", "Get me ", "May I a have ", "Could i have ", "Can you give to me ", "Please show me "),
        "part2": {
            "neutral": ('a neutral', 'an unbiased', 'an objective', 'an impartial', 'a'),
            "annoyance": ('a annoying', 'a irritating', 'an infuriating', 'a tiresome'),
            "gratitude": ('an appriciative', 'a recognizing'),
            "anger": ('a sad', 'an unhappy', 'a depressed', 'a sorrowful', 'a', 'a not so happy', 'an unglad', 'a not glad', 'melancholic'),
            "fear": ('a scarred', 'a fearful', 'a'),
            "surprise": ('a surpised', 'unexpected'),
            "desire": ('a desiring', 'a longing', 'a craving'),
            "admiration": ('an admiring', 'a praising', 'a applauding'),
            "confusion": ('a confusing', 'a wierd'),
            "amusement": ('a amusing', 'a gleeful', 'a delighting'),
            "caring": ('a caring', 'a kind', 'a tender'),
            "embarrassment": ('an emparrasing', 'a humiliating', 'a shamefull'),
            "grief": ('a grieving', 'a sad', 'a melancholic'),
            "joy": ("a happy", "a joyful", "a glad", "a delightful", "a", "a gleefull"),
            "curiosity": ("a curious", "an interesting"),
            "disapproval": ("a disapproving", "an objecting"),
            "optimism": ("an optimistic", "a positive"),
            "excitement": ("an exciting", "an enthusiastic"),
            "love": ("a loving", "an intimate"),
            "relief": ("a relieving", "a comforting"),
            "sadness": ("a sad", "an unhappy", "a depressed", "a sorrowful", "a", "a not so happy", "an unglad", "a not glad", "melancholic")
        },
        "part3": (' sentence', ' statement', ' piece of text', ' quote', ' citation')
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
