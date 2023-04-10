#!/usr/bin/python3
from wonderwords import RandomWord
import random

rw = RandomWord()


adjectives = ['red', 'happy', 'large', 'bumpy', 'silly',
              'fancy', 'good', 'new', 'fast', 'last', 'long']
adverbs = ['quickly', 'happily', 'loudly', 'slowly',
           'gently', 'eagerly', 'often', 'just', 'really']

print("Welcome to the Random Phrase Generator Game!")

while True:
    print("Enter 'q' to quit the game or any key to continue:")
    response = input()
    if response == 'q':
        break

    # Generate subject
    print("Do you want a random noun for the subject?")
    response = input("Enter 'y' or 'n': \n")
    if response == 'y':
        subject = rw.word(include_parts_of_speech=["nouns"])
        print("{}".format(subject))
    elif response == 'n':
        subject = input("Enter a noun for the subject: \n")
    else:
        print("Invalid input. Please enter 'y' or 'n'.\n")
        continue

    # Generate verb
    print("Do you want a random verb for the predicate?")
    response = input("Enter 'y' or 'n': \n")
    if response == 'y':
        verb = rw.word(include_parts_of_speech=["verbs"])
        print("{}".format(verb))
    elif response == 'n':
        verb = input("Enter a verb for the predicate: \n")
    else:
        print("Invalid input. Please enter 'y' or 'n'.\n")
        continue

    # Generate object
    print("Do you want a random noun for the object?")
    response = input("Enter 'y' or 'n': \n")
    if response == 'y':
        object = rw.word(include_parts_of_speech=["nouns"])
        print("{}".format(object))
    elif response == 'n':
        object = input("Enter a noun for the subject: \n")
    else:
        print("Invalid input. Please enter 'y' or 'n'.\n")
        continue

    # Generate article, adjective, and adverb
    article1 = 'an' if subject[0].lower(
    ) in ['a', 'e', 'i', 'o', 'u'] else 'the' if subject[0].isupper() else 'a'
    article2 = 'an' if object[0].lower(
    ) in ['a', 'e', 'i', 'o', 'u'] else 'the' if object[0].isupper() else 'a'
    adjective = random.choice(adjectives)
    adverb = random.choice(adverbs)

    # Construct phrase, clause, or sentence based on user choice
    print("Do you want a phrase, clause, or sentence?")
    response = input("Enter 'p', 'c', or 's': \n")
    if response == 'p':
        phrase = "{} {} {}".format(article1, adjective, subject)
        print("{}".format(phrase))
    elif response == 'c':
        clause = "{} {} {} {}".format(adverb, subject, verb, object)
        print("{}".format(clause))
    elif response == 's':
        sentence = "{} {} {} {} {} {}".format(
            article1, adjective, subject, verb, article2, object)
        print("{}".format(sentence))
    else:
        print("Invalid input. Please enter 'p', 'c', or 's'.")
        continue
