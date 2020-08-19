import random
import json
import torch
import numpy


from src.model import NeuralNet
from src.nltk_utils import tokenize ,bag_of_words 

# loading json file 
INPUT_FILE = 'intents.json'
with open(f'./input/{INPUT_FILE}', 'r') as f:
    intents = json.load(f)

# loading trained model, state dict 
MODEL = 'model_chat.pth'
data = torch.load(f'./models/{MODEL}')

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

bot_name = 'pytorch_chatbot'
print("Let's us chat ! type 'q' to exit")

while True:
    # sentence = "do you use credit cards?"
    sentence = input("You: ")
    if sentence == "q":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: I do not understand...")

