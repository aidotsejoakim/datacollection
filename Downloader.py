if __name__ == "__main__":
    from ProceduralData import *

    def Save():
        dataset_loader = DatasetLoader()
        dataset_dictionary:dict = dataset_loader.CreateDictionaryFromDataset(dataset_name=dataset_name, labels=labels, prompt_structure=prompt_structure, list_structure=list_structure)
        dataset_loader.SaveDataset(dataset_dictionary=dataset_dictionary, save_directory="./Datasets/Downloaded_datasets/", file_name=dataset_name + "_dataset")

    # Name of huggingface dataset
    dataset_name:str = "emotion"
    # Labels for our dataset
    labels:tuple = ("sad", "joy", "love", "anger", "fear", "surprise")
    # Holds structure for prompts
    prompt_structure:dict = {
        "part1": ('Write ', 'Make ', 'This is ', 'Create ', 'Show me ', 'Display ', 'Print ', 'Reveal ', 'Reaveal to me ', 'Get me ', 'May I a have ', 'Could i have ', 'Can you give to me ', 'Please show me '),
        "part2": {
            "sad": ('a sad', 'an unhappy', 'a depressed', 'a sorrowful', 'a', 'a not so happy', 'an unglad', 'a not glad', 'melancholic'),
            "joy": ('a happy', 'a joyful', 'a glad', 'a delightful', 'a', 'a gleefull'),
            "love": ('a', 'a romantic', 'a love filled'),
            "anger": ('a sad', 'an unhappy', 'a depressed', 'a sorrowful', 'a', 'a not so happy', 'an unglad', 'a not glad', 'melancholic'),
            "fear": ('a scarred', 'a fearful', 'a'),
            "surprise": ('a surpised', 'unexpected', 'a')
        },
        "part3": (' sentence', ' statement', ' piece of text', ' quote', ' citation')
    }
    # Holds structure for how prompts should be listed
    list_structure:dict = {
        "index": (("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"), ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j"), ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")),
        "start": (". ", ".\n", "\n", ": ", ":\n"),
        "middle": ("\n", ),
        "end": ("\n", "\n\n")
    }
    Save()

    # Name of huggingface dataset
    dataset_name:str = "ag_news"
    # Labels for our dataset
    labels:tuple = ("World", "Sports", "Business", "Sci/Tech")
    # Holds structure for prompts
    prompt_structure:dict = {
        "part1": ('Write ', 'Make ', 'This is ', 'Create ', 'Show me ', 'Display ', 'Print ', 'Reveal ', 'Reaveal to me ', 'Get me ', 'May I a have ', 'Could i have ', 'Can you give to me ', 'Please show me '),
        "part2": ('a article ', 'a news article '),
        "part3": ('regarding ', 'containing ', 'about '),
        "part4": {
            "World": ('the world', 'anything', 'something'),
            "Sports": ('sports', 'sport', 'anything', 'something'),
            "Business": ('business', 'anything', 'something'),
            "Sci/Tech": ('sci/tech', 'sci', 'tech', 'technology', 'scify', 'anything', 'something')
        }
    }
    Save()

    # Name of huggingface dataset
    dataset_name:str = "yelp_polarity"
    # Labels for our dataset
    labels:tuple = ("Negative", "Positive")
    # Holds structure for prompts
    prompt_structure:dict = {
        "part1": ('Write ', 'Make ', 'This is ', 'Create ', 'Show me ', 'Display ', 'Print ', 'Reveal ', 'Reaveal to me ', 'Get me ', 'May I a have ', 'Could i have ', 'Can you give to me ', 'Please show me '),
        "part2": {
            "Negative": ('a negative', 'a hurtfull', 'a destructive'),
            "Positive": ('a positive', 'a progressive', 'an affirmative', 'a constructive', 'a practical'),
        },
        "part3": (' review', ),
    }
    Save()

    # Name of huggingface dataset
    dataset_name:str = "kan_hope"
    # Labels for our dataset
    labels:tuple = ("NoneHope", "Hope")
    # Holds structure for prompts
    prompt_structure:dict = {
        "part1": ('Write ', 'Make ', 'This is ', 'Create ', 'Show me ', 'Display ', 'Print ', 'Reveal ', 'Reaveal to me ', 'Get me ', 'May I a have ', 'Could i have ', 'Can you give to me ', 'Please show me '),
        "part2": {
            "NoneHope": ('a hopeless', 'a helpless', 'a pointless', 'a tragic'),
            "Hope": ('a hopeful', 'a cheerful', 'an enthusiastic', 'a upbeat'),
        },
        "part3": (' speech', ' conversation', ' discussion', ' dialogue'),
    }
    Save()