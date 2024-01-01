from collections import Counter
"""
given a string s, return how many times a character c appears, -1 if it does not appear
"""
def charcount(word, character):
    amount = word.count(character)
    return amount if amount != 0 else -1
def charcount_counter(word, character):
    if not isinstance(word, str) or len(character) != 1:
        raise TypeError("Arg 0 must be string and Arg 1 must be character !!")
    charfreq = Counter(word)
    amount = charfreq.get(character)
    return amount if amount != 0 else -1
"""
given a string s, find the first non repeating character
"""
def firstnonrepeat(word):
    if not isinstance(word, str):
        raise TypeError("Must be string !!")
    charfreq = Counter(word)
    for c in word:
        if charfreq.get(c) == 1:
            return c
    return None