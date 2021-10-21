if __name__ == "__main__":
    from PromptDataset import *     

    labels:tuple = ("sad", "joy", "love", "anger", "fear", "surprise")
    prompt_structure:dict = {
        "part1": ('Write ', 'Make ', 'This is ', 'Create ', 'Show me ', 'Display ', 'Print ', 'Reveal ', 'Reaveal to me ', 'Get me ', 'May I a have ', 'Could i have ', 'Can you give to me ', 'Please show me '),
        "part2": {
            "sad": ('a sad', 'an unhappy', 'a depressed', 'a sorrowful', 'a', 'a not so happy', 'an unglad', 'a not glad', 'melancholic'),
            "joy": ('a happy', 'a joyful', 'a glad', 'a delightful', 'a', 'a gleefull'),
            "love": ('a', ),
            "anger": ('a sad', 'an unhappy', 'a depressed', 'a sorrowful', 'a', 'a not so happy', 'an unglad', 'a not glad', 'melancholic'),
            "fear": ('a scarred', 'a fearful', 'a'),
            "surprise": ('a surpised', 'unexpected', 'a')
        },
        "part3": (' sentence', ' statement', ' piece of text', ' quote', ' citation')
    }
    list_structure:dict = {
        "index": (("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"), ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j"), ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")),
        "start": (". ", ".\n", "\n", ": ", ":\n"),
        "middle": ("\n", ),
        "end": ("\n", "\n\n")
    }

    dataset = DatasetLoader(dataset_name="emotion", labels=labels)
    # # Get dataset from huggingface
    # dataset.LoadDatasetFromHuggingface()
    # DatasetLoader.SaveDataset(dataset_dictionary=dataset.CreateDictionaryFromDataset(), save_directory="./Datasets/", file_name="emotion_dataset")
    # Load in dataset from file
    dataset = DatasetLoader(dataset_name="emotion", labels=labels)
    dataset.dataset_dictionary = DatasetLoader.LoadDatasetFromJSON("./Datasets/emotion_dataset.json")
    my_complete_dataset_object = DatasetsGenerator(dataset=dataset, labels=labels, prompt_structure=prompt_structure, list_structure=list_structure, few_shot_range=(0,3), dataset_training_size=10_000, dataset_other_size=1_000)
    my_complete_dataset:dict = my_complete_dataset_object.Create()
    
    DatasetLoader.PrintDataset(my_complete_dataset)
    DatasetLoader.SaveDataset(dataset_dictionary=my_complete_dataset, save_directory="./Datasets/", file_name="my_emotion_dataset")