import numpy as np
import json

DATASET_PATH ='Datasets/contradictions.json'

with open(DATASET_PATH,'r') as f:
    s = json.load(f)
    d = s['dataset']


NR_OF_PROMPTS = 3
NR_OF_EXAMPLES= 20

DATASET_LENGTH = len(d['text'])

def generate_type(type, index):
    RANDOM_START = s["prompt_structure"]["part1"][len(s["prompt_structure"]["part1"])-1]
    if np.random.choice([0,1]) == 1 or type == 'neutral':
        RANDOM_MIDDLE = s["prompt_structure"]["part2"][type][1]
        RANDOM_END = s["prompt_structure"]["part3"][len(s["prompt_structure"]["part3"])-1]
        SENTENCE = RANDOM_START + RANDOM_MIDDLE +RANDOM_END
    else:
        RANDOM_MIDDLE = s["prompt_structure"]["part2"][type][0]
        SENTENCE = RANDOM_START + RANDOM_MIDDLE
    SENTENCE += s["prompt_structure"]["part4"][len(s["prompt_structure"]["part4"])-1]
    return SENTENCE
def generateRandomPrompt():
    RANDOM_ROW = np.random.randint(DATASET_LENGTH)
    RANDOM_PREMISE = d['premise'][RANDOM_ROW].replace('\n', '')
    RANDOM_TYPE = generate_type(d['text'][RANDOM_ROW],RANDOM_ROW)  
    RANDOM_HYPOTHESIS = d['label'][RANDOM_ROW]
    return RANDOM_PREMISE, RANDOM_TYPE, RANDOM_HYPOTHESIS

for j in range(NR_OF_PROMPTS):
    for i in range(NR_OF_EXAMPLES):
        
        SOURCE_SENTENCE, TYPE, HYPOTHESIS = generateRandomPrompt()

        print(str(i+1) + '.', SOURCE_SENTENCE + '\n' + TYPE + ':\n'+ HYPOTHESIS+ '\n')
    
    SOURCE_SENTENCE, TYPE, HYPOTHESIS = generateRandomPrompt()
    print(str(NR_OF_EXAMPLES+1) + '.',SOURCE_SENTENCE + '\n' + TYPE + ':\n')
    print('\n------\n')