#!/usr/bin/python3
from wonderwords import RandomWord
import random

rw = RandomWord()

articles = ['the', 'a', 'an']
adjectives = ['red', 'happy', 'large', 'bumpy', 'silly', 'fancy', 'good', 'new', 'fast', 'last', 'long']
adverbs = ['quickly', 'happily', 'loudly', 'slowly', 'gently', 'eagerly', 'often', 'just', 'really']

print("Welcome to the Random Phrase Generator Game!\n")

while True:
    print("Enter 'q' to quit the game or any key to continue:")
    response = input()
    if response == 'q':
        break

    # Generate subject
    print("Do you want a random noun for the subject?\n")
    response = input("Enter 'y' or 'n': ")
    if response == 'y':
        subject = rw.word(include_parts_of_speech=["nouns"])
        print("{}\n".format(subject))
    elif response == 'n':
        subject = input("Enter a noun for the subject: \n")
    else:
        print("Invalid input. Please enter 'y' or 'n'.\n")
        continue

    # Generate verb
    print("Do you want a random verb for the predicate?\n")
    response = input("Enter 'y' or 'n': ")
    if response == 'y':
        verb = rw.word(include_parts_of_speech=["verbs"])
        print("{}\n".format(verb))
    elif response == 'n':
        verb = input("Enter a verb for the predicate: ")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue

    # Generate object
    print("Do you want a random noun for the object?\n")
    response = input("Enter 'y' or 'n': ")
    if response == 'y':
        object = rw.word(include_parts_of_speech=["nouns"])
        print("{}\n".format(object))
    elif response == 'n':
        object = input("Enter a noun for the subject: \n")
    else:
        print("Invalid input. Please enter 'y' or 'n'.\n")
        continue

    # Generate article, adjective, and adverb
    article1 = random.choice(articles)
    article2 = random.choice(articles)
    adjective = random.choice(adjectives)
    adverb = random.choice(adverbs)

    # Construct phrase, clause, or sentence based on user choice
    print("Do you want a phrase, clause, or sentence?\n")
    response = input("Enter 'p', 'c', or 's': ")
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
