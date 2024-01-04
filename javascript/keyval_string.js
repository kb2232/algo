
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
