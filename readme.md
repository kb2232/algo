# algorithm practice in javascript and python
## strings and hash (solutions are in javascript and python directories)
### question 1
given a string s, return how many times a character c appears, -1 if it does not appear
- charcount(word, character)
- EXAMPLE: 
    - INPUT: "abascas", "s"
    - OUTPUT: 2
- EXAMPLE: 
    - INPUT: "abascas", "t"
    - OUTPUT: -1   
### question 2
given a string s, find the first non repeating character
- firstnonrepeat(word)
- EXAMPLE: "babatunde" => "t"
### question 3
given a string, s, find the character c or characters, that repeats the most
- repeatsmost(word)
- EXAMPLE: 
    - INPUT: s = "aabbbccc"
    - OUTPUT: ['b', 'c']
### question 4
Given a dictionay of companies and how much each owe, return the company/companies that owes the most
- owe_most_amount(compdict)
- EXAMPLE: 
    - INPUT: {"compA": 30, "compB": 56, "compC": 12, "compD": 33, "compE": 56}
    - OUTPUT: ["compB", "compE"]
### question 5
Give a string s, return true if its palindrome.
A palindrome is a string that reads same forward and backwards
- ispalindrome(word)
- EXAMPLE: "hanah" => true
### question 6
Given a string s, return true if its Pangram.
A pangram is a sentence or string that contains every letter of the alphabet at least once. 
- panagram(word)
- Example: "The quick brown fox jumps over a lazy dog" => true
### question 7
Given two string inputs, determine if both are anagrams.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase 
- isanagram(s1, s2)
- INPUT:  "listen" and "silent" => OUTPUT: true
- "listen" and "silent" are anagrams.
- "triangle" and "integral" are anagrams.
- "hello" and "bye" are not anagrams.
### question 8
You need to write a function, "removeOutsideWhitespaces", 
that will remove the leading and trailing white spaces from a given string. 
The function will leave the white spaces that are in the middle of the string untouched. 
If the input string consists only of white spaces, the function should return an empty string.
- removeOutsideWhitespaces(word)
### question 9
Given a string, s, sort it in increasing order using selection sort.
Selection sort involved finding the smallest and moving it all the way to the begining.
- selectionsort(word)
- example "kunle" -> eunlk enulk elunk ekunl elnuk elkun  => "elknu"
### question 10
Given a list of dictionary, sort them by a given key using selection sort
- selectionsort_list(list)
- example: [{"name":"baba"}, {"name":"blake"},{"name":"aaple"}, {"name":"candy"}]
    - [{"name":"aaple"}, {"name":"baba"},{"name":"blake"}, {"name":"candy"}]


