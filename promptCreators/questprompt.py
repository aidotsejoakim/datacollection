from numpy import random

def prompt(count, dictionary):
  string = ''
  for i in range(count):
    index = random.randint(len(dictionary['label']))
    string += str(i+1) + ". <"
    string += dictionary['text'][index+i] + ">\n"
    string += dictionary['label'][index+i] + "\n"
  index = random.randint(len(dictionary['label']))
  string += str(count+1) + ". <"
  string += dictionary['text'][index+i] + ">\n" 

  return string
