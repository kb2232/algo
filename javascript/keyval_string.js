
const freqmap = word => {
    const obj = {};
    for(let c of word) {
        !obj[c] ? obj[c]=1 : obj[c]++
    }
    return obj;
}
/**
 * given a string s, return how many times a character c appears, -1 if it does not appear
 */
function charcount(word, character) {
    if (typeof word != "string") {
        throw new TypeError("must be a string")
    }else {
        if(!word.includes(character)) {
            return -1;
        }
        myobj = freqmap(word);
        return myobj[character];
    }
}

/**
 * given a string s, find the first non repeating character
 */
function firstnonrepeat(word) {
    const myobj = freqmap(word);
    for(let c of word) {
        if(myobj[c] == 1) {
            return c;
        }
    }
    return "None";
}
/**
 * given a string, s, find the character c or characters, that repeats the most
- repeatsmost(word)
 */
const repeatsmost = word => {
    if(typeof word !== "string"){
        throw new TypeError("must be string!!1")
    }
    if(word.length == 1) return [word];
    const myobj = freqmap(word);
    const allvalues = Object.values(myobj);
    const maxval = Math.max(...allvalues);
    const myset = new Set()
    for(let c of word) {
        if(myobj[c] === maxval) myset.add(c)
    }
    return myset;
}
/**
 *  Given a dictionary of companies and how much each owe, return the company/companies that owes the most.
1. get all the values and find the max
2. loop through each item
    - if the value equals the max then store the key
 */
function owe_most_amount(compdict) {
    if(typeof compdict != "object") throw new TypeError("Must be Object!!");
    const maxval = Math.max(...Object.values(compdict));
    const myset = new Set();
    for(const item in compdict){
        const key = item;
        const value = compdict[item];
        if(value == maxval) {
           myset.add(key)
        }
    }
    return myset;
}
// Give a string s, return true if its palindrome.
const ispalindrome = word => {
    if(typeof word != "string") {
        throw new TypeError("must be string")
    }
    return word == word.split("").reverse().join("")
}
/**
 * Given a string s, return true if its Pangram.
A pangram is a sentence or string that contains every letter of the alphabet at least once. 
- make list of 26 and fill with false
- make lower case
- loop through and see if every character is /^[a-z]&/.test()
    - get index value of it and turn it to true
- return false if any of the array values are false
 */
function ispanagram(word) {
    if(typeof word == "string") {
        const alphacheck = Array(26).fill(false);
        word = word.toLowerCase();
        for(let w of word) {
            if(/^[a-z]$/.test(w)) {
                const index = w.charCodeAt(0) - 'a'.charCodeAt(0);
                alphacheck[index] = true;
            }
        }
        return alphacheck.every(e=>e);
    }else {
        throw new TypeError("must be string")
    }
}
/**
 * Given two string inputs, determine if both are anagrams.
 * An anagram is a word or phrase formed by rearranging the letters of a different word or phrase 
- return false if there of diff lengths
- create a frequency map of each
- loop through s1, and check if each key and value equals in s2
    - return false if you encounter one that does not match
- return true
 */
const isanagram = (s1, s2) => {
    if(s1.length != s2.length) return false;
    const s1map = freqmap(s1);
    const s2map = freqmap(s2);
    for(const item in s1map) {
        if(s2map[item] != s1map[item]) {
            return false;
        }
    }
    return true;
}

/**
 * You need to write a function, "removeOutsideWhitespaces", 
 * that will remove the leading and trailing white spaces from a given string. 
 * The function will leave the white spaces that are in the middle of the string untouched. 
 * If the input string consists only of white spaces, the function should return an empty string.
- removeOutsideWhitespaces(word)

MY APPROACH
- find indexof first non whitespace character
- find indexof last non whitespace character
- make a new string from those indices
 */
const firstnonwhitespace_char_index = word => {
    for(let i = 0; i<word.length; i++) 
        if(!/^\s$/.test(word[i])) return i;
    return -1;
}
const lastnonwhitespace_char_index = word => {
    for(let i = word.length-1; i >= 0; i--) 
        if(!/^\s$/.test(word[i])) return i;
    return -1;
}
function removeOutsideWhitespaces(word) {
    const start = firstnonwhitespace_char_index(word);
    const stop = lastnonwhitespace_char_index(word);
    return start ===-1 || stop === -1 ? '' : word.slice(start, stop+1);
}
/**
 * Given a string, s, sort it in increasing order using selection sort
- selectionsort(word)
- example "kunle" -> eunlk enulk elunk ekunl elnuk elkun  => "elknu"
 */
function selectionsort(word) {
    const listword = word.split("");
    const n = listword.length;
    for(let i=0; i<n; i++) {
        for(let j=i+1; j<=n; j++) {
            if(listword[j] < listword[i]) {
                const temp = listword[i];
                listword[i] = listword[j];
                listword[j] = temp;
            }
        }
    }
    return listword.join("");
}
/**
 * Given a list of dictionary, sort them by a given key using selection sort
- selectionsort_list(itemlist, key)
- example: [{"name":"baba"}, {"name":"blake"},{"name":"aaple"}, {"name":"candy"}]
    - [{"name":"aaple"}, {"name":"baba"},{"name":"blake"}, {"name":"candy"}]
 */
function selectionsort_list(itemlist, uni_key) {
    const listword = itemlist;
    const n = listword.length;
    for(let i=0; i<n; i++) {
        for(let j=i+1; j<=n; j++) {
            if(listword[j][uni_key] < listword[i][uni_key]) {
                const temp = listword[i];
                listword[i] = listword[j];
                listword[j] = temp;
            }
        }
    }
    return listword;
}
/**
 * Given string s, find the length of the longest substring without repeating characters
 - int lengthOfLongestSubstring(word);
Loop through each character,
    - if its not in frequency map(freq), 
    - freq[c] = i; then create key value with the value being the index of the character
    - at that point, thats the longest: longest = max(longest, i+1-first)
    - if it is in the map already, update the first = max(first, freq[c]+1)
*/
const lengthOfLongestSubstring = word => {
    const obj = {}; let first=0,longest=0;
    for(let i=0; i<word.length; i++) {
        const c = word[i];
        if(obj[c]) {
            first = Math.max(first, obj[c]+1);
        }
        obj[c] = i;
        longest = Math.max(longest, i-first+1);
    }
    return longest;
}
/*
Following from question 12, Given string s, find the longest substring without repeating characters
 -  longestSubstring(word);
*/
//this was looked up
const longestSubstring = (str) => {
    const map = {};
    let start = 0; // Start of the sliding window
    let longest = 0;
    let longestStart = 0; // Starting index of the longest substring found

    for (let i = 0; i < str.length; i++) {
        const c = str[i];
        if (map[c] >= start) { // Character seen and is within the current window
            start = map[c] + 1; // Move the start of the window
        }
        map[c] = i; // Update the last index of the character

        // If the current window is larger than the previously recorded longest
        if (i - start + 1 > longest) {
            longest = i - start + 1;
            longestStart = start; // Update the start of the longest substring
        }
    }
    return str.substring(longestStart, longestStart + longest); // Extract the longest substring
};
