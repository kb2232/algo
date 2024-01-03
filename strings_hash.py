from collections import Counter

"""
{"compA": 30, "compB": 56, "compC": 12, "compD": 33, "compE": 56}
Given a dictionay of companies and how much each owe, return the company/companies that owes the most
"""
def owe_most_amount(compdict):
    if isinstance(compdict, dict):
        max_owe = max(compdict.values())
        comp_most_owe = [comp for comp,owe in compdict.items() if owe == max_owe]
        return comp_most_owe
    raise TypeError("Expected a dictionary")
"""
Give a string s, return true if its palindrome.
A palindrome is a string that reads same forward and backwards
Example: "hanah" => true
"""
def ispalindrome(word):
    if not isinstance(word, str):
        return False
    if len(word) == 0:
        return False
    return word == word[::-1] #object[start:stop:step]
"""
Given a string s, return true if its Pangram.
A pangram is a sentence or string that contains every letter of the alphabet at least once. 
Example: "The quick brown fox jumps over a lazy dog" => true
"""
def panagram(word):
    if isinstance(word, str):
        # create list of 26 false
        alphabet_presence = [False]*26
        word = word.lower()
        # find the numerical val and update the list to true
        for w in word:
            #make sure not space and is character
            if w.isalpha():
                index = ord(w) - ord('a')
                alphabet_presence[index] = True
        # go over list and if any false then not a panagram
        return all(alphabet_presence)
    else:
        raise TypeError("Not a string")
"""
Given a string, determine if its a anagram.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase 
INPUT:  "listen" and "silent"
OUTPUT: true
"""

"""
 * You need to write a function, "removeWhitespace", 
 * that will remove the leading and trailing white spaces from a given string. 
 * The function will leave the white spaces that are in the middle of the string untouched. 
 * If the input string consists only of white spaces, the function should return an empty string.
"""

"""
Given a string, s, sort it in increasing order
"""

"""
Given a list of dictionary, sort them by a given key
"""