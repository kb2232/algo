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
"""
given a string, s, find the character c or characters, that repeats the most
- repeatsmost(word)
"""
def repeatsmost(word):
    freq = Counter(word)
    allvalues = freq.values()
    maxval = max(allvalues)
    return [char for char,val in freq.items() if val == maxval]
"""
Given a dictionay of companies and how much each owe, return the company/companies that owes the most.
1. get all the values and find the max
2. loop through each item
    - if the value equals the max then store the key
"""
def owe_most_amount(compdict):
    if isinstance(compdict, dict):
        maxval = max(compdict.values())
        return [key for key,val in compdict.items() if val == maxval]
    return None
# Give a string s, return true if its palindrome.
def ispalindrome(word):
    if not isinstance(word, str):
        raise TypeError("Must be string")
    return word == word[::-1] #object[start:stop:step]
"""
Given a string s, return true if its Pangram.
A pangram is a sentence or string that contains every letter of the alphabet at least once. 
- make list of 26 and fill with false
- make lower case
- loop through and see if every character is /^[a-z]&/.test()
    - get index value of it and turn it to true
- return false if any of the array values are false
"""
def panagram(word):
    if isinstance(word, str):
        assesspanagram = [False]*26
        word = word.lower()
        for w in word:
            if w.isalpha():
                index = ord(w) - ord('a')
                assesspanagram[index] = True
        return all(assesspanagram)
    else:
        raise TypeError("Must be string!!!")
"""
Given two string inputs, determine if both are anagrams.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase 
- return false if there of diff lengths
- create a frequency map of each
- loop through s1, and check if each key and value equals in s2
    - return false if you encounter one that does not match
- return true
"""   
def isanagram(s1, s2):
    if len(s1) != len(s2):
        return False
    freqs1 = Counter(s1)
    freqs2 = Counter(s2)
    for key,val in freqs1.items():
        if freqs2.get(key) != val:
            return False
    return True
"""
You need to write a function, "removeOutsideWhitespaces", 
that will remove the leading and trailing white spaces from a given string. 
The function will leave the white spaces that are in the middle of the string untouched. 
If the input string consists only of white spaces, the function should return an empty string.
- removeOutsideWhitespaces(word)

MY APPROACH
- find indexof first non whitespace character
- find indexof last non whitespace character
- make a new string from those indices
"""
def firstnonwhitespace_char_index(word):
    for i in range(0, len(word), 1):
        if not word[i].isspace():
            return i
    return -1
def lastnonwhitespace_char_index(word):
    for i in range(len(word)-1, -1, -1):
        if not word[i].isspace():
            return i
    return -1

def removeOutsideWhitespaces(word):
    start = firstnonwhitespace_char_index(word)
    stop = lastnonwhitespace_char_index(word)
    return '' if start == -1 or stop == -1 else word[start:stop+1]
    
