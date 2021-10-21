import json
import numpy as np
from questprompt import qnaprompt


def loadDataset(path): 
    with open(path, 'r') as f:
        return json.load(f)

list_structure = {
    "index": [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], 
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], 
        ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    ],
    "start": (". ", ".\n", ": ", ":\n"),
    "middle": ("\n", )
}

def selectRandomIndex():
    l = len(list_structure['index'])
    return list_structure['index'][np.random.randint(l)]

def generatePrompts(nrOfExamples, nrOfPrompts, path): 
    '''
    nrOfExamples: Number of examples per prompt
    nrOfPrompts: Number of generated prompts
    path: Dataset path
    '''

    dataset = loadDataset(path)
   

    if 'prompt_structure' not in dataset.keys():
        DATASET_LENGTH = len(dataset['text'])

        INDEX = selectRandomIndex()
        START = np.random.choice(list_structure['start'])
        MIDDLE = np.random.choice(list_structure['middle'])
    
        for i in range(nrOfPrompts):
            qnaprompts = qnaprompt(nrOfExamples, dataset)
            print(qnaprompts)

    else: 
        prompt_structure = dataset['prompt_structure']
        DATASET_LENGTH = len(dataset['dataset']['text'])

        for i in range(nrOfPrompts):
            INDEX = selectRandomIndex()
            START = np.random.choice(list_structure['start'])
            MIDDLE = np.random.choice(list_structure['middle'])
        
            
            for j in range(nrOfExamples):   
                instruction = ''   
                RANDOM_ROW = np.random.randint(DATASET_LENGTH)
                SENTIMENT = dataset['dataset']['text'][RANDOM_ROW]
                SENTENCE = dataset['dataset']['label'][RANDOM_ROW]

                if type(SENTENCE) == list:
                    RANDOM_SIMP = np.random.randint(len(SENTENCE))
                    SENTENCE = SENTENCE[RANDOM_SIMP].replace('\n', '')


                for part in prompt_structure:
                    if (part == 'part2'):
                        if prompt_structure[part] == 'USE_LABEL':
                            instruction += SENTIMENT
                        else: 
                            instruction += np.random.choice(prompt_structure[part][SENTIMENT])
                    else: 
                        instruction += np.random.choice(prompt_structure[part]) 

                print(INDEX[j] + START + instruction + MIDDLE  + SENTENCE +'\n')
                    
            targetInstruction = ''   
            RANDOM_ROW_INSTRUCTION = np.random.randint(DATASET_LENGTH)
            INSTRUCTION_SENTIMENT = dataset['dataset']['text'][RANDOM_ROW_INSTRUCTION]

            for part in prompt_structure:
                if part == 'part2':
                    
                    if prompt_structure[part] == 'USE_LABEL':
                            targetInstruction += SENTIMENT
                    else: 
                        targetInstruction += np.random.choice(prompt_structure[part][INSTRUCTION_SENTIMENT])
                else: 
                    targetInstruction += np.random.choice(prompt_structure[part]) 
                    

            print(INDEX[nrOfExamples+1] + START  + targetInstruction)
            print('\n------')


generatePrompts(nrOfExamples=1,nrOfPrompts=1,path='Datasets/GigawordDataset4.json')
# generatePrompts(nrOfExamples=1,nrOfPrompts=1,path='Datasets/summarizedataset.json')
# generatePrompts(nrOfExamples=1,nrOfPrompts=1,path='Datasets/quest.json')

