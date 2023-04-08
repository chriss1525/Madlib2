#!/usr/bin/python3
import requests
import random

url = "https://api.datamuse.com/words?sp=*n*&max=1000"
word = requests.get(url,)

subject = input("type any noun:\n")
verb = input("type any verb:\n")

print("{}".format(subject), end=" ")
print("{}".format(verb), end=" ")
if word.status_code != 200:
    print("Error: API returned status code {}".format(word.status_code))
    print(word.text)
else:
    data = word.json()
    nouns = [d['word'] for d in data]  # Extract all the nouns
    chosen_noun = random.choice(nouns)  # Pick a random noun
    print("{}".format(chosen_noun))
