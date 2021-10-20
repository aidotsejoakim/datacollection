
import numpy as np
import json

DATASET_PATH ='Datasets/simplificationdataset.json'

with open(DATASET_PATH,'r') as f:
    d = json.load(f)


NR_OF_PROMPTS = 3
NR_OF_EXAMPLES= 4

DATASET_LENGTH = len(d['text'])


def generateRandomPrompt(): 
    RANDOM_ROW = np.random.randint(DATASET_LENGTH)
    SOURCE_SENTENCE = d['text'][RANDOM_ROW]

    ROW_SIMPLIFICATIONS = d['label'][RANDOM_ROW]

    RANDOM_SIMP = np.random.randint(len(ROW_SIMPLIFICATIONS))

    ROW_SIMPLIFICATION = ROW_SIMPLIFICATIONS[RANDOM_SIMP]
    return SOURCE_SENTENCE, ROW_SIMPLIFICATION

for j in range(NR_OF_PROMPTS):
    for i in range(NR_OF_EXAMPLES):
        
        SOURCE_SENTENCE, SIMPLIFICATION = generateRandomPrompt()

        print(str(i+1) + '. Simplify:', SOURCE_SENTENCE + '\n' + SIMPLIFICATION + '\n')
    
    SOURCE_SENTENCE = generateRandomPrompt()
    print(str(NR_OF_EXAMPLES+1) + '. Simplify:',SOURCE_SENTENCE[0])
    print('\n------\n')





