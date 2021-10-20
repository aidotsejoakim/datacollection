
import numpy as np
import json

DATASET_PATH ='Datasets\summarizedataset.json'

with open(DATASET_PATH,'r') as f:
    d = json.load(f)


NR_OF_PROMPTS = 3
NR_OF_EXAMPLES= 20

DATASET_LENGTH = len(d['text'])


def generateRandomPrompt(): 
    RANDOM_ROW = np.random.randint(DATASET_LENGTH)
    SOURCE_SENTENCE = d['text'][RANDOM_ROW].replace('\n', '')

    ROW_SIMPLIFICATIONS = d['label'][RANDOM_ROW]

    RANDOM_SIMP = np.random.randint(len(ROW_SIMPLIFICATIONS))

    ROW_SIMPLIFICATION = ROW_SIMPLIFICATIONS[RANDOM_SIMP].replace('\n', '')
    return SOURCE_SENTENCE, ROW_SIMPLIFICATION

for j in range(NR_OF_PROMPTS):
    for i in range(NR_OF_EXAMPLES):
        
        SOURCE_SENTENCE, SIMPLIFICATION = generateRandomPrompt()

        print(str(i+1) + '. Summarize:', SOURCE_SENTENCE + '\n' + SIMPLIFICATION + '\n')
    
    SOURCE_SENTENCE = generateRandomPrompt()
    print(str(NR_OF_EXAMPLES+1) + '. Summarize:',SOURCE_SENTENCE[0])
    print('\n------\n')


