"""
Count happy and sad words using the NLTK Opinion Lexicon.
Dataset: https://www.nltk.org/api/nltk.corpus.reader.opinion_lexicon.html
"""

import re

from nltk.corpus import opinion_lexicon


# Separate positive and negative word lists from the public dataset.
HAPPY_WORDS = set(opinion_lexicon.positive())
SAD_WORDS = set(opinion_lexicon.negative())


def read_sentence(prompt):
    """Keep asking until the user enters a nonempty sentence."""
    while True:
        sentence = input(prompt).strip()
        if sentence:
            return sentence
        print("Please enter a sentence.")


def words_in(sentence):
    """Extract lowercase words while allowing internal hyphens/apostrophes."""
    return re.findall(r"[a-z0-9]+(?:[-'][a-z0-9]+)*", sentence.lower())


def number_happy(sentence):
    """Count every occurrence of a word in the positive word list."""
    return sum(1 for word in words_in(sentence) if word in HAPPY_WORDS)


def number_sad(sentence):
    """Count every occurrence of a word in the negative word list."""
    return sum(1 for word in words_in(sentence) if word in SAD_WORDS)


def challenge():
    """Compare happy and sad word counts to determine the sentence's tone."""
    print("\nHAPPY AND SAD WORD COUNTER")
    sentence = read_sentence("Enter a sentence: ")
    happy = number_happy(sentence)
    sad = number_sad(sentence)

    if happy > sad:
        analysis = "Positive (happy)"
    elif sad > happy:
        analysis = "Negative (sad)"
    else:
        analysis = "Neutral"

    print(f"\nHappy words: {happy}")
    print(f"Sad words: {sad}")
    print(f"Analysis: {analysis}")


if __name__ == "__main__":
    challenge()