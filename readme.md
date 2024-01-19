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
- selectionsort_list(itemlist, key)
- example: [{"name":"baba"}, {"name":"blake"},{"name":"aaple"}, {"name":"candy"}]
    - [{"name":"aaple"}, {"name":"baba"},{"name":"blake"}, {"name":"candy"}]
### question 11 lengthOfLongestSubstring(word);
Given string s, find the length of the longest substring without repeating characters
 - lengthOfLongestSubstring(word);
 - EXAMPLE:
    - input: "abcabcbb"; output: 3; explanation: "abc" 
    - input: "bbbbb"; output: 1; explanation: "b" 
    - input: "pwwkew"; output: 3; explanation: "wke" 
    - input: "tmmzuxt"; output: 5; explanation: "mzuxt"
    - input: ""; output: 0; explanation: its empty 
### question 12 longestSubstring(word);
Following from question 12, Given string s, find the longest substring without repeating characters
 -  longestSubstring(word);
### question 13 shortestSubstring(word)
Shortest Distance Between Repeated Characters
- shortestSubstring(word)
- INPUT:
    - A string s of length n (1 ≤ n ≤ 10^5), consisting of lowercase English letters.
- OUTPUT:
    - A substring of s which is derived from the shortest distance between two repeated characters.
- Examples:
    - shortestSubstring("blob") should return "blob". Explanation: The shortest distance is between the two 'b' characters which encompass the entire string.
    - shortestSubstring("hannah") should return "nn". Explanation: The shortest distance is between the two 'n' characters in the middle.
    - shortestSubstring("badabas") should return either "ada" or "aba". Explanation: Both "ada" and "aba" have the same shortest distance between two repeated characters.
    - shortestSubstring("clique") should return "clique". Explanation: There are no repeated characters.
### q14. parse a sentence
Given a sentence, parse out a word(s).
- parsestring(sentence)
- Input: "Method=GET Path=/sample?param1=value1"
- Output: Path=/sample?param1=value1

    
### q15. parse a blob of http request
Given a blob of "http request", parse out: "Method, Path, Host, User-Agent, Accept, X-Service-Time, and     X-Request-Id". 
 - parsepair(blob)
 - Create a key value data structure to group the entities parsed.
 - All string input will have each key values in the same position. The value of the each key varies.

 An example is given:
 - INPUT: 
  "Method=GET Path=/sample?param1=value1&param2=value2 HTTP/1.1 Host: www.example.com User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Accept: application/json X-Service-Time: 100ms X-Request-Id: abc123"
 - OUTPUT:
  {
      "Method": "GET",
      "Path": "/sample?param1=value1&param2=value2",
      "Host": "www.example.com",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
      "Accept": "application/json",
      "X-Service-Time": "100ms",
      "X-Request-Id": "abc123"
  }