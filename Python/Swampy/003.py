__author__ = 'TIW'


def find_1(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return 'Shit + 1'

def find(word,letter):
    for the_one in word:
