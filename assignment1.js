// 1.4 Palindrome Permutation

function permPalindrome(phrase) {
    //use const instead of var, bc the val doesnt change
    const countMap = buildCharFrequencyTable(phrase);
    return checkMaxOneOdd(countMap);
}

function checkMaxOneOdd(countMap) {
    var oddCount = 0;
    for (i of countMap.values())
        if (i % 2){
            oddCount += 1;
        }
        if (oddCount > 1){
            return false;
        }
    return true;
}

// JS NOTES
// map, hashmap, dictionary
// data structure: key value
//   -unique key
//   -value
//   {"a": 1, "b": 2, "c": 3}
// Map is ordered, dict is unordered
// Map key can be anything not just char or string

// Create map, 
//  iterate through each char in phrase, 
//  if its alredy in the map, increment the value
// Builds map w count of each unique char
//      key = char
//      value = count
function buildCharFrequencyTable(phrase) {
    var map = new Map();
    //for each char in string
    for (c in phrase){
        //check if c already in map
        //if yes, increment, if no, set to initial value
        if (map.get(phrase[c]) >= 0) {
            map.set(phrase[c], map.get(phrase[c])+1);
        }
        else{
            map.set(phrase[c], 1);
        }
    }
    return map;
}

console.log(permPalindrome("tacocat"));
console.log(permPalindrome("hello"));


//2.6 Linked List palindrome
class LinkedList{
    constructor(next, data) {
        this.next = next;
        this.data = data;
    }

    append(data) {
        //let vs var
        //let does not allow you to access the var outside of the method
        let tail = new LinkedList(null, data);
        let current = this;
        //while not at end
        while (current.next !== null) {
            current = current.next;
        }
        current.next = tail;
    }
}

function palindrome(head) {
    let current = head;
    let stack = [];
    //builds up stack represenation of linked list
    //stores linked list order in reverse
    while (current !== null) {
        stack.push(current.data);
        current = current.next;
    }
    current = head;
    //comparing each val in the linked list to each val in the reversed stack we just made
    //if are not same on either side, not a palindrome
    for (i = 0; i < stack.length; i++) {
        if (current.data !== stack.pop()) {
            return false;
        }
        current = current.next;
    }
    return true;
}

let notPalindrome = new LinkedList(null, "a");
notPalindrome.append("b");
notPalindrome.append("c");

console.log(palindrome(notPalindrome));

let isPalindrome = new LinkedList(null, "a");
isPalindrome.append("b");
isPalindrome.append("a");

console.log(palindrome(isPalindrome));