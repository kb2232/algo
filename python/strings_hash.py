from collections import Counter
import sys
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
    
"""
Given a string, s, sort it in increasing order using selection sort
- selectionsort(word)
- example "kunle" -> eunlk enulk elunk ekunl elnuk elkun  => "elknu"
"""
def selectionsort(word):
    charlist = list(word)
    for i in range(0, len(charlist)-1):
        for j in range(i+1, len(charlist)):
            if charlist[j] < charlist[i]:
                charlist[j], charlist[i] = charlist[i], charlist[j]
    return ''.join(charlist)
"""
Given a list of dictionary, sort them by a given key using selection sort
- selectionsort_list(itemlist, key)
- example: [{"name":"baba"}, {"name":"blake"},{"name":"aaple"}, {"name":"candy"}]
    - [{"name":"aaple"}, {"name":"baba"},{"name":"blake"}, {"name":"candy"}]
"""
def selectionsort_list(itemlist, key):
    n = len(itemlist)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if itemlist[j].get(key) < itemlist[i].get(key):
                itemlist[j],itemlist[i] = itemlist[i],itemlist[j]
    return itemlist

"""
Given string s, find the length of the longest substring without repeating characters
 - int lengthOfLongestSubstring(word);
Loop through each character,
    - if its not in frequency map(freq), 
    - freq[c] = i; then create key value with the value being the index of the character
    - at that point, thats the longest: longest = max(longest, i+1-first)
    - if it is in the map already, update the first = max(first, freq[c]+1)
"""
def lengthOfLongestSubstring(word):
    freqmap = {}
    first = 0
    longest = 0
    for i in range(0, len(word)-1):
        c = word[i]
        if c in freqmap:
            first = max(first, freqmap.get(c)+1)
        freqmap[c] = i
        longest = max(longest, i-first+1)
    return longest
def lengthOfLongestSubstring2(word):
    freqmap = {}; first=0; longest=0;
    for i in range(0, len(word)-1):
        c = word[i]
        if c in freqmap:
            first = max(first,freqmap.get(c))
        freqmap[c] = i
        longest = max(longest, i - first)
    return longest
"""
Following from question 12, Given string s, find the longest substring without repeating characters
 -  longestSubstring(word);
"""
def longestSubstring(word): #this was looked up
    freqmap = {}
    start = 0 
    maxLength = 0  # Track the length of the longest substring
    longestStart = 0  # Start index of the longest substring found
    for i, c in enumerate(word):  # Correct the range to include the last character
        if c in freqmap and freqmap[c] >= start:
            start = freqmap[c] + 1
        freqmap[c] = i
        if i - start + 1 > maxLength:  # Update maxLength and longestStart if a longer substring is found
            maxLength = i - start + 1
            longestStart = start
    return word[longestStart:longestStart+maxLength]  # Return the longest substring


# Shortest Distance Between Repeated Characters
def shortestSubstring(word):
    firstindex=-1
    secindex=-1
    shortdis=sys.maxsize
    freq = {}
    for i in range(len(word)-1):
        c = word[i]
        if c in freq:
            if i-freq.get(c) < shortdis:
                shortdis = i-freq.get(c)
                firstindex = freq.get(c)
                secindex = i
        else:
            freq[c] = i
    return word[firstindex:secindex+1] if firstindex!=-1 or secindex!=-1 else word
"""
Given a blob, parse out then create a dictionary.
- parsestring(blob)
- Input: "Method=GET Path=/sample?param1=value1"
- Output: {'Method': 'GET', 'Path': '/sample?param1=value1'}
"""
def parsestring(blob):
    # split the blob by space
    arrblob = blob.split(" ") #['Method=GET', 'Path=/sample?param1=value1']
    # for each item in list, split by first and make a dictionary with each
    arrdic = {}
    for item in arrblob:
        arritem = item.split("=", 1) #['Method', 'GET'], ['Path', '/sample?param1=value1']
        arrdic[arritem[0]] = arritem[1]
    return arrdic

"""
Given a blob of "http request", parse out: 
    "Method, Path, Host, User-Agent, Accept, X-Service-Time, and X-Request-Id". 
 - parsepair(blob)
 - Create a key value data structure to group the entities parsed.
 - All string input will have each key values in the same position. The value of the each key varies.
 input: "Method=GET Path=/sample?param1=value1&param2=value2 HTTP/1.1 Host: www.example.com User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Accept: application/json X-Service-Time: 100ms X-Request-Id: abc123"
"""
def parsepair(blob):
    blobarr = blob.split(" ")
    return blobarr