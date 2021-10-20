import nltk
from nltk.corpus import wordnet as wn
nltk.download('wordnet')
import datasets
from datasets import Dataset
import numpy as np
import random
import json

# The subject variable rebresents what kind of texts are in the dataset. This variable and synonyms will be included in the prompts
# Beware that the synonyms of the subject word might not always mean what you intend the subject to mean. For example using sentence will
# give a lot of synonyms from the legal system. Recomended subject is text
# The datafile variable includes the path to the dataset used
subject = 'text'
datafile = 'data.json'

#Load dataset
with open('data.json','r') as f:
    d = json.load(f)
dataset = Dataset.from_dict(d)

#Input word and output synonyms based on wordnet database
def Synonym(word):
  synonyms = []
  for syn in wn.synsets(word):
    for lm in syn.lemmas():
             synonyms.append(lm.name())#adding into synonyms
  synonyms = np.unique(synonyms, return_index=False, return_inverse=False, return_counts=False, axis=None)
  if len(synonyms.tolist()) == 0:
    synonyms = np.append(synonyms, word)
  
  return synonyms

#Add A or An based on starting letter of word
def A_Or_An(word):
  vowels = ['a','e','i','o','u']
  if word.lower()[0] in vowels:
    word = 'an '+ word
  else:
    word = 'a ' + word
  return word

#Generate prompts based on labels and subject
def GenerateSentence(grade, subject):
  word_list1= [
              'Write ', 'Make ', 'This is ', 'Create ', 'Show me ', 'Display ', 'Print ',
               'Reveal ', 'Get me ', 'May I a have ', 'Could i have ',
               'Can you give me ', 'Please show me '
  ]
  grade_list = Synonym(grade)
  subject_list = Synonym(subject)
  generated_sentences = []
  w = word_list1[random.randint(0,(len(word_list1)-1))]
  g = grade_list[random.randint(0,(len(grade_list)-1))]
  sentenceg = A_Or_An(g)
  s = subject_list[random.randint(0,(len(subject_list)-1))]
  sentence = w + sentenceg + ' ' + s
  sentence = sentence.replace('_', ' ')
  return sentence

#use Generate sentance to create prompts based on the labels in the dataset
def PromptsFromDataset(dataset, text_type):
  prompts_list = []
  for label in dataset['text']:
    prompts = GenerateSentence(label,text_type)
    prompts_list.append(prompts)
  
  return prompts_list, dataset['label']

def ShowExamples(numofex, dataset, subject):
  x = 1
  prompts, answers = PromptsFromDataset(dataset, subject)
  for i in range(numofex):
    randomplace = random.randint(0,len(prompts))
    print(str(i+1) + '. <'+ prompts[randomplace] + '>\n' + answers[randomplace] + '\n')
    x +=1
  print(str(x) + '. <'+ prompts[random.randint(0,len(prompts))] + '>')


#Run ShowExamples to get a list of prompts with answers and a last prompt without an answer. Insert nuber of prompts with answers,
#which dataset to use and which kind of media the answer is. The subject could for example be text or review.
ShowExamples(3, dataset, subject)


