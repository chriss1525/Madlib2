#!/usr/bin/python3
import requests
import random

nouns = "https://api.datamuse.com/words?sp=*n*"
verbs = "https://api.datamuse.com/words?sp=*v*"
# Adjectives = "https://api.datamuse.com/words?sp=*adj*&max=1000"
# Adverbs = "https://api.datamuse.com/words?sp=*adv*&max=1000"
noun = requests.get(nouns,)
verb = requests.get(verbs,)

print("pick random noun?")
yes = input("y/n\n")
if yes == 'y':
        data = noun.json()
        word = [d['word'] for d in data]  # Extract all the words
        subject = random.choice(word)  # Pick a random word
        print("{}".format(subject))
elif yes == 'n':
    subject = input("type any noun:\n")
else:
    raise TypeError("Please pick Y or N")
print("pick random verb?")
yes = input("y/n\n")
if yes == 'y':
        data = verb.json()
        word = [d['word'] for d in data]  # Extract all the words
        verb = random.choice(word)  # Pick a random word
        print("{}".format(verb))
elif yes == 'n':
    verb = input("type any verb:\n")
else:
    raise TypeError("Please pick Y or N")
print("pick a random noun?")
yes = input("y/n\n")
if yes == 'y':
        data = noun.json()
        word = [d['word'] for d in data]  # Extract all the words
        object = random.choice(word)  # Pick a random word
        print("{}".format(object))

print("{}".format(subject), end=" ")
print("{}".format(verb), end=" ")
print("{}".format(object))
