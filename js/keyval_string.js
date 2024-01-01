function charfreq(word) {
    const obj = {};
    for(let c of word) {
        !obj[c] ? obj[c]=1 : obj[c]++;
    }
    return obj;
}
//given a string s, return how many times a character c appears, -1 if it does not appear
const charcount = (word, char) => {
    const obj = charfreq(word);
    return (obj[char] == 0 || !obj[char]) ? -1 : obj[char];
}
//given a string s, find the first non repeating character
const firstnonrepeat = (word) => {
    const obj = charfreq(word);
    for(let c of word) {
        if(obj[c] == 1) return c;
    }
    return '\0';
}
// given a string s, find all characters that repeats the most
const repeatsmost = word => {
    if(word.length == 0) {
        return false;
    }
    //get all values in char freq
    const obj = charfreq(word);
    const allvals = Object.values(obj);
    //get max
    const maxval = Math.max(...allvals);
    //all key-val with val equal to maxval, add to list to return
    const res = [];
    for(let c of word) {
        if(obj[c] == maxval) res.push([c, maxval]);
    }
    return res;
}
// given a string s, find the FIRST characters that repeats the most
const firstchar_mostrepeat = word => {
    if(word.length == 0 || !word) {
        return false;
    }
    //get key value
    const obj = charfreq(word);
    //get all value and max value
    const maxval = Math.max(...Object.values(obj));
    //whichever one of the character first equals max value, return it
    for (const c of word) {
        if(obj[c] == maxval) return c;
    }
    return '\0'
}
/**
 * {"compA": 30, "compB": 56, "compC": 12, "compD": 33, "compE": 56}
 * Given a dictionay of companies and how much each owe, 
 * return the company/companies that owes the most
 */
const owes_most = comp_dict => {
    if(typeof comp_dict == "object") {
        const res = [];
        //all the values
        const allvals = Object.values(comp_dict);
        //get the max
        const maxval = Math.max(...allvals);
        //put in a list the ones with max
        for (const char in comp_dict) {
            if(comp_dict[char] == maxval) {
                res.push(char);
            }
        }   
        return res;
    } else {
        throw new Error("Wrong type !!");
    }
}
/**
 * Given a string s, return true if its palindrome.
 * A palindrome is a string that reads same forward and backwards
 * Example: "hanah" => true
 */
const isPalidrome = word => {
    if(typeof word == "string") {
        if(word.length == 0) return false;
        if(word.length == 1) return true;
        const revstr = word.split("").reverse().join("");
        return word.toLowerCase() == revstr.toLowerCase();
    }else {
        throw new Error("must be a string");
    }
}
/**
 * Given a string s, return true if its Pangram. 
 * A pangram is a sentence or string that contains every letter of the alphabet at least once. 
 * Example: "The quick brown fox jumps over a lazy dog" => true
 */
function isPangram(word) {
    //create array of 26 false
    const alphacheck = Array(26).fill(false);
    word = word.toLowerCase();
    for(let w of word) {
        //check if alpha
        if(/^[a-z]$/.test(w)) {
            //get the numerical
            const index = w.charCodeAt(0) - 'a'.charCodeAt(0);
            //update the alphacheck
            alphacheck[index] = true;
        }
    }
    return alphacheck.every(e => e)
}
console.log(isPangram("abcdefghijklmnopqrstuvw xyz"))
