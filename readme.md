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
1. create a freq map of word
2. from all the values, find max
3. loop over word, return a list of one or all the characters with value of max
```