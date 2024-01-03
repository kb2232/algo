# algorithm practice in javascript and python

## question 1
```
given a string s, return how many times a character c appears, -1 if it does not appear
- charcount(word, character)
```
## question 2
```
given a string s, find the first non repeating character
- firstnonrepeat(word)
1. create an object of the word
2. loop through word
    - check each character in obj
    - return as soon as the value of the key is ONE
```
## question 3
```
given a string, s, find the character c or characters, that repeats the most
- repeatsmost(word)
EXAMPLE: 
    INPUT: s = "aabbbccc"
    OUTPUT: ['b', 'c']
```
## question 4
```
Given a dictionay of companies and how much each owe, return the company/companies that owes the most
- owe_most_amount(compdict)
EXAMPLE: 
    INPUT: {"compA": 30, "compB": 56, "compC": 12, "compD": 33, "compE": 56}
    OUTPUT: ["compB", "compE"]
```