import json
import numpy as np

with open("data.json",'r') as f:
    d = json.load(f)



FINAL_SIGNS = ['\n', '.\n', ':\n']
SUB_SENTENCES = {
  'part1': ['Write ', 'Make ', 'This is ', 'Create ', 'Show me ', 'Display ', 'Print ', 'Reveal ', 'Reaveal to me ', 'Get me ', 'May I a have ', 'Could i have ', 'Can you give to me ', 'Please show me '],
  'sadness': ['a sad', 'an unhappy', 'a depressed', 'a sorrowful', 'a not so happy', 'an unglad', 'a not glad', 'melancholic'],
  'joy': ['a happy', 'a joyful', 'a glad', 'a delightful', 'a gleefull'],
  'love': [ 'heartful'],
  'anger': ['a sad', 'an unhappy', 'a depressed', 'a sorrowful', 'a not so happy', 'an unglad', 'a not glad', 'melancholic'],
  'fear': ['a scarred', 'a fearful'],
  'surprise':['a surpised', 'unexpected'],
  'part3': ['sentence', ' statement', ' piece of text', ' quote', ' citation'],
}



NR_OF_PROMPTS = 20
NR_OF_EXAMPLES= 4

DATASET_LENGTH = len(d['text'])



def generateRandomPrompt():

    RANDOM_ROW = np.random.randint(DATASET_LENGTH)
    SENTIMENT = d['text'][RANDOM_ROW]
    SENTENCE = d['label'][RANDOM_ROW]

    INSTRUCTION = np.random.choice(SUB_SENTENCES['part1']) \
            + np.random.choice(SUB_SENTENCES[SENTIMENT]) \
            + np.random.choice(SUB_SENTENCES['part3']) \
            + np.random.choice(FINAL_SIGNS)

    return INSTRUCTION, SENTENCE
    


for j in range(NR_OF_PROMPTS):
    for i in range(NR_OF_EXAMPLES):
        
        SOURCE_SENTENCE, SIMPLIFICATION = generateRandomPrompt()

        print(str(i+1) + '.', SOURCE_SENTENCE  + SIMPLIFICATION + '\n')
    
    SENTIMENT = generateRandomPrompt()
    print(str(NR_OF_EXAMPLES+1) + '.', SENTIMENT[0])
    print('\n------\n')


