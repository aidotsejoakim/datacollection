import json, random

class prompt_generator():
  def __init__(self, dataset, words):
    with open(dataset) as f:
        self.data = json.loads(f.readlines()[0])

    self.first_words = words["first_words"]
    self.middle_words = words["middle_words"]
    self.plural_words = words["plural_words"]
    self.last_words = words["last_words"]
    self.final_signs = words["final_signs"]

  def generate_prompt(self, examples_per_prompt=3):
    prompt = ""
    selected_num = []

    for _ in range(0, examples_per_prompt):  
      all_num = list(range(len(self.data["dataset"]["text"])))
      allowed_num = [x for x in all_num if x not in selected_num]
      num = random.choice(allowed_num)
      selected_num.append(num)

      sentence = self.generate_words()

      prompt += sentence + self.data["dataset"]["text"][num] + "\n"
      prompt += self.data["dataset"]["label"][num] + "\n\n"

    num = random.choice(allowed_num)

    sentence = self.generate_words()

    prompt += sentence + self.data["dataset"]["text"][num]

    return prompt

  def generate_words(self):
    first_word = self.first_words[random.randint(0, len(self.first_words) - 1)]
    
    capital_bool = random.randint(0, 1)
    if capital_bool == 1:
      first_word = first_word.title()

    plural_bool = random.randint(0, 1)
    if plural_bool == 0:
      middle_word = self.middle_words[random.randint(0, len(self.middle_words) - 1)]
    else:
      middle_word = self.plural_words[random.randint(0, len(self.plural_words) - 1)]
    last_word = self.last_words[random.randint(0, len(self.last_words) - 1)]
    
    if plural_bool == 1:
      last_word += "s"

    delimeter = self.final_signs[random.randint(0, len(self.final_signs) - 1)]

    sentence = first_word + middle_word + last_word + delimeter

    return sentence

words = {
  "first_words": [
    "continue ", "complete ", "finish ", "end "
  ],

  "middle_words": [
    "the ", "this ", "that ", ""
  ],

  "plural_words": [
    "these ", "those ", ""
  ],

  "last_words": [
    "sentence", "prompt", "string", "statement", "text"
  ],

  "final_signs": [
    ": ", "-> ", ", ", ". ", "> ", " "
  ]
}

generator = prompt_generator("Datasets/swag.json", words)

print(generator.generate_prompt())