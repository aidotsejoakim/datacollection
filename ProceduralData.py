# Imports
import json
import copy
import random

class DatasetLoader():
    ''' Handels download and convertion of huggingface dataset to type(dict) '''
    def __init__(self, convert_label_index_to_string:bool = True):        
        self.convert_label_index_to_string:bool = convert_label_index_to_string

    def LoadDatasetFromHuggingface(self, dataset_name:str):
        ''' Returns self.dataset_name dataset from huggingface '''
        from datasets import load_dataset
        return load_dataset(dataset_name)

    def CreateDictionaryFromDataset(self, dataset_name:str, labels:tuple, prompt_structure:dict, list_structure:dict) -> dict:
        ''' Returns dictionary representation of currently loaded dataset '''
        dataset = self.LoadDatasetFromHuggingface(dataset_name)

        self.dataset_dictionary:dict = {
            "datasets": {},
            "labels": labels,
            "prompt_structure": prompt_structure,
            "list_structure": list_structure,
        }
        data_structure:dict = {
            "text" : [],
            "label" : []
        }

        for key, value in dataset.items():
            self.dataset_dictionary["datasets"][key] = copy.deepcopy(data_structure)
            for data_point in value:
                if (self.convert_label_index_to_string):
                    label:str = labels[data_point["label"]]
                    self.dataset_dictionary["datasets"][key]["text"].append(label)
                else:
                    label:int = data_point["label"]
                    self.dataset_dictionary["datasets"][key]["text"].append(label)
                self.dataset_dictionary["datasets"][key]["label"].append(data_point["text"])
            
        return self.dataset_dictionary

    def LoadDatasetFromJSON(self, file_directory:str) -> dict:
        with open(file_directory) as json_file:
            data = json.load(json_file)
            self.dataset_dictionary:dict = data
            return data

    def SortDictionary(self, dataset_dictionary:dict, reprocess:bool = False) -> dict:
        ''' Returns sorted dictionary of currently loaded dataset '''
        cached_bool:bool = self.convert_label_index_to_string
        self.convert_label_index_to_string = True
        
        self.dataset_dictionary_split = copy.deepcopy(dataset_dictionary)
        for key in self.dataset_dictionary_split["datasets"].keys():
            combined:dict = {}
            
            for label in dataset_dictionary["labels"]:
                combined[str(label)] = []

            for text, label in zip(self.dataset_dictionary_split["datasets"][key]["text"], self.dataset_dictionary_split["datasets"][key]["label"]):
                combined[text].append(label)

            self.dataset_dictionary_split["datasets"][key] = combined

        self.convert_label_index_to_string = cached_bool
        return self.dataset_dictionary_split

    @staticmethod
    def SaveDataset(dataset_dictionary:dict, save_directory:str = "/content/", file_name:str = "dataset"):
        ''' Saves dataset as file_name to save_directory in JSON format '''
        json_content:str = json.dumps(dataset_dictionary)
        
        full_path:str = f"{save_directory}{file_name}.json"
        with open(full_path, "w+") as json_file:
            json_file.write(json_content)
            json_file.close()

    @staticmethod
    def PrintDataset(dataset_dictionary:dict, indent:int = 4, example_amount:int = 3):
        ''' Prints concatinated dataset '''
        iteration_index:int = -1
        
        def Recursive(dictionary:dict, iteration_index:int):
            iteration_index += 1
            for key, value in dictionary.items():
                indent_str:str = " " * indent * iteration_index
                print(f"{indent_str}{key}:")
                value_type:type = type(value)
                if value_type is dict:
                    Recursive(value, iteration_index)
                else:
                    indent_str:str = " " * indent * (iteration_index + 1)
                    print(f"{indent_str}{value_type.__name__}: {value[0:example_amount]} +{len(value)-example_amount} items")

        Recursive(dataset_dictionary, iteration_index)

class PromptCreator():
    ''' Itteratable object that returns procedurally generated prompts given category and prompt_structure '''
    def __init__(self, prompt_structure:dict, labels:tuple, iteration_amount:int = -1, convert_label_to_index:bool = False):
        self.prompt_structure:dict = copy.deepcopy(prompt_structure)
        self.labels:tuple = labels
        self.iteration_amount:int = iteration_amount
        self.convert_label_to_index:bool = convert_label_to_index
        self.iteration_index:int = 0

    def __iter__(self):
        ''' Iterator protocol that returns an iterator '''
        self.iteration_index = 0
        return self
    
    def __call__(self, iteration_amount:int):
        ''' Allows the assignment of self.iteration_amount by call '''
        self.iteration_amount = iteration_amount
        self.iteration_index = 0
        return self

    def __next__(self) -> tuple:
        ''' Iterator protocol that returns the next item '''
        if self.iteration_index >= self.iteration_amount and self.iteration_amount >= 0:
            self.iteration_index = 0
            raise StopIteration

        self.iteration_index += 1

        chosen_category:str = ""
        prompt:str = ""
        for prompt_part in self.prompt_structure.values():
            if type(prompt_part) is dict:
                random_category:str = random.choice(list(prompt_part))
                prompt += random.choice(prompt_part[random_category])
                if random_category in self.labels:
                    chosen_category = random_category
            else:
                prompt += random.choice(prompt_part)

        return (prompt, chosen_category if not self.convert_label_to_index else self.labels.index(chosen_category))

def SynonymHelper(word:str) -> tuple:
    import numpy as np
    import nltk
    from nltk.corpus import wordnet as wn
    nltk.download('wordnet')
    def A_Or_An(word:str) -> str:
        vowels:tuple = ('a','e','i','o','u')
        if word.lower()[0] in vowels:
            word = 'an '+ word
        else:
            word = 'a ' + word
        return word

    synonyms:list = []
    for syn in wn.synsets(word):
        for lm in syn.lemmas():
            synonyms.append(A_Or_An(lm.name())) # adding into synonyms
    synonyms = np.unique(synonyms, return_index=False, return_inverse=False, return_counts=False, axis=None)
    if len(synonyms.tolist()) == 0:
        synonyms = np.append(synonyms, word)
    
    return tuple(synonyms.tolist())

class PromptDatasetPair():
    ''' Pairs procedurally generated prompts from prompt_creator with random text from dataset into tuples '''
    def __init__(self, dataset:dict, prompt_creator:PromptCreator, iteration_amount:int = 5):
        self.dataset:dict = dataset
        self.prompt_creator:PromptCreator = prompt_creator
        self.prompt_creator.iteration_amount = -1
        self.iteration_amount:int = iteration_amount
        self.iteration_index:int = 0
    
    def __iter__(self):
        ''' Iterator protocol that returns an iterator '''
        self.iteration_index = 0
        return self
    
    def __call__(self, iteration_amount:int):
        ''' Allows the assignment of self.iteration_amount by call '''
        self.iteration_amount = iteration_amount
        self.iteration_index = 0
        return self

    def __next__(self) -> tuple:
        ''' Iterator protocol that returns the next item '''
        if self.iteration_index >= self.iteration_amount and self.iteration_amount >= 0:
            self.iteration_index = 0
            raise StopIteration

        self.iteration_index += 1
        
        prompt, category = next(self.prompt_creator)
        text:str = random.choice(self.dataset[category])

        return (prompt, text)

class FewShotGenerator():
    def __init__(self, prompt_dataset_pair:PromptDatasetPair, list_structure:dict, iteration_amount:int = 5, few_shot_range:tuple=(0,3)):
        self.prompt_dataset_pair:PromptDatasetPair = prompt_dataset_pair
        self.prompt_dataset_pair.iteration_amount = -1
        self.list_structure:dict = list_structure
        self.few_shot_range:tuple = few_shot_range
        self.iteration_amount:int = iteration_amount
        self.iteration_index:int = 0
    
    def __iter__(self):
        ''' Iterator protocol that returns an iterator '''
        self.iteration_index = 0
        return self
    
    def __call__(self, iteration_amount:int):
        ''' Allows the assignment of self.iteration_amount by call '''
        self.iteration_amount = iteration_amount
        self.iteration_index = 0
        return self

    def __next__(self) -> tuple:
        ''' Iterator protocol that returns the next item '''
        if self.iteration_index >= self.iteration_amount and self.iteration_amount >= 0:
            self.iteration_index = 0
            raise StopIteration

        self.iteration_index += 1
        
        few_shot_amount:int = random.randint(self.few_shot_range[0], self.few_shot_range[1])
        indices:tuple = random.choice(self.list_structure["index"])
        start:str = random.choice(self.list_structure["start"])
        middle:str = random.choice(self.list_structure["middle"])
        end:str = random.choice(self.list_structure["end"])

        text:str = ""
        label:str = ""
        index:int = 0
        for single_prompt, single_text in self.prompt_dataset_pair(few_shot_amount + 1):
            text += indices[index] + start + single_prompt
            if index == few_shot_amount:
                label = single_text
            else:
                text += middle + single_text + end
            index += 1

        return (text, label)

class DatasetGenerator():
    ''' Uses PromptDatasetPair class to create a dataset '''
    def __init__(self, few_shot_generator:FewShotGenerator):
        self.few_shot_generator:FewShotGenerator = few_shot_generator
    
    def Create(self) -> dict:
        ''' Returns dictionary of created dataset '''
        created_dataset:dict = {
            "text": [],
            "label": []
        }
        for text, label in self.few_shot_generator:
            created_dataset["text"].append(text)
            created_dataset["label"].append(label)

        return created_dataset

class DatasetsGenerator():
    ''' Creates dataset with all parts of downloaded dataset '''
    def __init__(self, sorted_dataset:dict, few_shot_range:tuple=(0,3), dataset_training_size:int = 10_000, dataset_other_size:int = 1_000):
        self.sorted_dataset:dict = sorted_dataset
        self.prompt_creator:PromptCreator = PromptCreator(prompt_structure=sorted_dataset["prompt_structure"], labels=sorted_dataset["labels"], convert_label_to_index=False)
        self.dataset_creators:dict = {}
        self.list_structure = sorted_dataset["list_structure"]

        is_beginning:bool = True
        for key, item in self.sorted_dataset["datasets"].items():
            prompt_dataset_pair_object = PromptDatasetPair(dataset=item, prompt_creator=self.prompt_creator)
            few_shot_object = FewShotGenerator(prompt_dataset_pair=prompt_dataset_pair_object, list_structure=self.list_structure, few_shot_range=few_shot_range)
            dataset_creator_object = DatasetGenerator(few_shot_object(dataset_training_size if is_beginning else dataset_other_size))
            self.dataset_creators[key] = dataset_creator_object
            is_beginning = False

    def Create(self) -> dict:
        ''' Returns dictionary of created dataset '''
        datasets:dict = {}
        data_structure:dict = {
            "text" : [],
            "label" : []
        }

        for key, item in self.dataset_creators.items():
            datasets[key] = item.Create()

        return datasets