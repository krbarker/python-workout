#!/usr/bin/env python3
"""Solution to chapter 2, exercise 7: ubbi_dubbi"""


def ubbi_dubbi():
    """Ask the user to enter a word, and print the word's translation into Ubbi Dubbi."""
    word = input("Enter a word: ")

    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)

    print(''.join(output))
