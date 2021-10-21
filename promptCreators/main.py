import json
import numpy as np

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
    DATASET_LENGTH = len(dataset['dataset']['text'])
    prompt_structure= dataset['prompt_structure']

    for i in range(nrOfPrompts):
        INDEX = selectRandomIndex()
        START = np.random.choice(list_structure['start'])
        MIDDLE = np.random.choice(list_structure['middle'])
    
         
        for j in range(nrOfExamples):   
            instruction = ''   
            RANDOM_ROW = np.random.randint(DATASET_LENGTH)
            SENTIMENT = dataset['dataset']['text'][RANDOM_ROW]
            SENTENCE = dataset['dataset']['label'][RANDOM_ROW]


            for part in prompt_structure:
                if (part == 'part2'):
                    instruction += np.random.choice(prompt_structure[part][SENTIMENT])
                else: 
                    instruction += np.random.choice(prompt_structure[part]) 

            print(INDEX[j] + START + instruction + MIDDLE  + SENTENCE +'\n')
                
        targetInstruction = ''   
        RANDOM_ROW_INSTRUCTION = np.random.randint(DATASET_LENGTH)
        INSTRUCTION_SENTIMENT = dataset['dataset']['text'][RANDOM_ROW_INSTRUCTION]

        for part in prompt_structure:
            if (part == 'part1' or part == 'part3'):
                targetInstruction += np.random.choice(prompt_structure[part]) 
            else: 
                targetInstruction += np.random.choice(prompt_structure[part][INSTRUCTION_SENTIMENT])

        print(INDEX[nrOfExamples+1] + START  + targetInstruction)
        print('\n------')


generatePrompts(nrOfExamples=4,nrOfPrompts=2,path='Datasets/sentimentdata.json')

