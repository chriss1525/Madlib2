#!/usr/bin/python3
from wonderwords import RandomWord
import random

rw = RandomWord()

articles = ['the', 'a', 'an']
adjectives = ['red', 'happy', 'large', 'bumpy', 'silly', 'fancy']
adverbs = ['quickly', 'happily', 'loudly', 'slowly', 'gently', 'eagerly']

print("Welcome to the Random Phrase Generator Game!\n")

while True:
    print("Enter 'q' to quit the game or any key to continue:")
    response = input()
    if response == 'q':
        break

    # Generate subject
    print("Do you want a random noun for the subject?")
    response = input("Enter 'y' or 'n': ")
    if response == 'y':
        subject = rw.word(include_parts_of_speech=["nouns"])
        print("{}".format(subject))
    elif response == 'n':
        subject = input("Enter a noun for the subject: ")
        print("{}".format(subject))
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue

    # Generate verb
    print("Do you want a random verb for the predicate?")
    response = input("Enter 'y' or 'n': ")
    if response == 'y':
        verb = rw.word(include_parts_of_speech=["verbs"])
        print("{}".format(verb))
    elif response == 'n':
        verb = input("Enter a verb for the predicate: ")
        print("{}".format(verb))
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue

    # Generate object
    print("Do you want a random noun for the object?")
    response = input("Enter 'y' or 'n': ")
    if response == 'y':
        obj = rw.word(include_parts_of_speech=["nouns"])
        print("{}".format(object))
    elif response == 'n':
        obj = input("Enter a noun for the object: ")
        print("{}".format(object))
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue

    # Generate article, adjective, and adverb
    article = random.choice(articles)
    adjective = random.choice(adjectives)
    adverb = random.choice(adverbs)

    # Construct phrase, clause, or sentence based on user choice
    print("Do you want a phrase, clause, or sentence?")
    response = input("Enter 'p', 'c', or 's': ")
    if response == 'p':
        phrase = "{} {} {}".format(article, adjective, subject)
        print("{}".format(phrase))
    elif response == 'c':
        clause = "{} {} {} {}".format(adverb, subject, verb, obj)
        print("{}".format(clause))
    elif response == 's':
        sentence = "{} {} {} {} {} {}".format(
            article, adjective, subject, verb, article, obj)
        print("{}".format(sentence))
    else:
        print("Invalid input. Please enter 'p', 'c', or 's'.")
        continue
