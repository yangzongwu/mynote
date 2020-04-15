# Comment
```js
// This is an in-line comment.
/* This is a
multi-line comment */
```

# Number
### Declare Variables
* Declare  
Variable names can be made up of numbers, letters, and $ or _, but may not contain spaces or start with a number.
```js
var myName;
```
* assigns  
This assigns the Number value 5 to myVariable.
```js
myVariable = 5;
```
* Initializing  myVariable    
When JavaScript variables are declared, they have an initial value of undefined. If you do a mathematical operation on an undefined variable your result will be NaN which means "Not a Number". If you concatenate a string with an undefined variable, you will get a literal string of "undefined".
```js
var myVar = 0;
```
* Case Sensitivity in Variables

### operator
* Add ,Subtract,Multiply,Divide 
```js
var myVar1 = 5 + 10; // assigned 15
var myVar2 = 12 - 6; // assigned 6
```
* Increment,Decrement   
You can easily increment or add one to a variable with the ++ operator.  
```js
i++; 
i--;
``` 
* Decimal 
```js
var myDecimal=1.7;
var product = 2.0 * 2.5;//5.0
```
* Remainder 
```js
var remainder;
remainder=11%3;
```
* Compound Assignment with Augmented Division
```js
myVar += 5;
myVar -= 5;
myVar *= 5;
myVar /= 5;
```

# string
* Declare 
```js
var myName = "your name";
```
* Escaping Literal Quotes in Strings  
In JavaScript, you can escape a quote from considering it as an end of string quote by placing a backslash (\) in front of the quote
```js
var sampleStr = "Alan said, \"Peter is learning JavaScript\".";
```
* Quoting Strings with Single Quotes  
```js
goodStr = 'Jake asks Finn, "Hey, let\'s go on an adventure?"'; 
badStr = 'Finn responds, "Let's go!"'; // Throws an error;
```
* Escape Sequences in Strings
    * \\'	single quote
    * \\"	double quote
    * \\\	backslash
    * \n	newline
    * \r	carriage return
    * \t	tab
    * \b	word boundary
    * \f	form feed
    
 * Concatenating Strings
 ```js
var newStr='My name is Alan,' + ' I concatenate.';
var ourStr = "I come first. ";
ourStr += "I come second.";
```
* Constructing Strings with Variables
```js
var myName;
var myStr;
myName="qqq";
myStr="My name is " +myName+ " and I am well!"
```
* Length
```js
"Alan Peter".length; // 10
```
* Bracket Notation
```js
var firstName = "Ada";
var firstLetterOfFirstName = firstName[0];
var thirdLetterOfFirstName = firstName[2];
var lastLetterOfFirstName = firstName[firstName.length-1];
```
* String Immutability
In JavaScript, String values are immutable, which means that they cannot be altered once created.  
cannot change the value of myStr to "Job",  
```js
var myStr = "Bob";
myStr[0] = "J";
```

# Array

```js
var sandwich = ["peanut butter", "jelly", "bread"];
var ourArray = ["John", 23];
```
* Multi-dimensional Array  
You can also nest arrays within other arrays  
```js
var myArray = [["the universe", 42], ["everything", 101010]];
```
* Array Indexes
```js
var array = [50,60,70];
array[0]; // equals 50
var data = array[1];
```
* Modify 
```js
var ourArray = [50,40,30];
ourArray[0] = 15; // equals [15,40,30]
```
* Access Multi-Dimensional
```js
var arr = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [[10,11,12], 13, 14]
];
arr[3]; // equals [[10,11,12], 13, 14]
arr[3][0]; // equals [10,11,12]
arr[3][0][1]; // equals 11
```
* push()
```js
var arr = [1,2,3];
arr.push(4);// arr is now [1,2,3,4]
```
* pop()
```js
var threeArr = [1, 4, 6];
var oneDown = threeArr.pop();
console.log(oneDown); // Returns 6
console.log(threeArr); // Returns [1, 4]
```
* shift()  
That's where .shift() comes in. It works just like .pop(), except it removes the first element instead of the last.
* unshift()  
.unshift() works exactly like .push(), but instead of adding the element at the end of the array, unshift() adds the element at the beginning of the array.

# Functions
```js
function functionName() {
  console.log("Hello World");
}
functionName()
```
* Arguments
```js
function testFun(param1, param2) {
  console.log(param1, param2);
}
```
* Global vs Local 
```js
var myGlobal=10;//global 
function fun1() {
  oopsGlobal=5;//global 
  var oopsLocal=5;
}
function fun2() {
  var output = "";
  if (typeof myGlobal != "undefined") {
    output += "myGlobal: " + myGlobal;
  }
  if (typeof oopsGlobal != "undefined") {
    output += " oopsGlobal: " + oopsGlobal;
  }
}
```
```js
var someVar = "Hat";
function myFun() {
    someVar = "Head";//ex wrong,Do not change the value of the global outerWear
    var someVar = "Head";
    return someVar;
}
```
* return  
```js
function plusThree(num) {
  return num + 3;
}
var answer = plusThree(5); // 8
```
* Undefined Value returned
```js
var sum = 0;
function addSum(num) {
  sum = sum + num;
}
addSum(3); // sum will be modified but returned value is undefined
```
* array to queue
```js
function nextInLine(arr, item) {
  arr.push(item);
  var item=arr.shift();
  return item;
}
```


# Operator
* Equality Operator
```js
1   ==  1   // true
1   ==  2   // false
1   == '1'  // true
"3" ==  3   // true
```
* Strict Equality
```js
3 ===  3   // true
3 === '3'  // false
```
```js
typeof 3   // returns 'number'
typeof '3' // returns 'string'
```
* Inequality Operator
```js
1 !=  2     // true
1 != "1"    // false
1 != '1'    // false
1 != true   // false
0 != false  // false
```
* Strict Inequality
```js
3 !==  3   // false
3 !== '3'  // true
4 !==  3   // true
```
* Greater & Less 
```js
5   >  3   // true
7   > '3'  // true
2   >  3   // false
'1' >  9   // false
```
* Greater Than Or Equal To  & Less Than Or Equal To
```js
6   >=  6   // true
7   >= '3'  // true
2   >=  3   // false
'7' >=  9   // false
```
* And 
```js
if (num > 5 && num < 10) {}
```
* or
```js
if (num > 10 || num < 5){}
```
# If
 ```js
if (condition is true) {
  statement is executed
}
```
* Else Statements
```js
if (num > 10) {
  return "Bigger than 10";
} else {
  return "10 or Less";
}
```
* Else If Statements
```js
if (num > 15) {
  return "Bigger than 15";
} else if (num < 5) {
  return "Smaller than 5";
} else {
  return "Between 5 and 15";
}
```

# Switch
```js
switch(num) {
  case value1:
    statement1;
    break;
  case value2:
    statement2;
    break;
...
  case valueN:
    statementN;
    break;
}
```
* default 
```js
switch (num) {
  case value1:
    statement1;
    break;
  case value2:
    statement2;
    break;
...
  default:
    defaultStatement;
    break;
}
```
* Multiple Identical Options
```js
switch(val) {
  case 1:
  case 2:
  case 3:
    result = "1, 2, or 3";
    break;
  case 4:
    result = "4 alone";
}
```
* Replacing If Else Chains with Switch
```js
if (val === 1) {
  answer = "a";
} else if (val === 2) {
  answer = "b";
} else {
  answer = "c";
}
```
```js
switch(val) {
  case 1:
    answer = "a";
    break;
  case 2:
    answer = "b";
    break;
  default:
    answer = "c";
}
```

# Objects
```js
var cat = {
  "name": "Whiskers",
  "legs": 4,
  "tails": 1,
  "enemies": ["Water", "Dogs"]
};
```
* Accessing Object Properties with Dot Notation
```js
var myObj = {
  prop1: "val1",
  prop2: "val2"
};
var prop1val = myObj.prop1; // val1
var prop2val = myObj.prop2; // val2
```
* Accessing Object Properties with Bracket Notation
```js
var myObj = {
  "Space Name": "Kirk",
  "More Space": "Spock",
  "NoSpace": "USS Enterprise"
};
myObj["Space Name"]; // Kirk
myObj['More Space']; // Spock
myObj["NoSpace"];    // USS Enterprise
```
* Accessing Object Properties with Variables
```js
var dogs = {
  Fido: "Mutt",  Hunter: "Doberman",  Snoopie: "Beagle"
};
var myDog = "Hunter";
var myBreed = dogs[myDog];
console.log(myBreed); // "Doberman"
```
* Updating Object
```js
ourDog.name = "Happy Camper";
ourDog["name"] = "Happy Camper";
```
* Add New Properties
```js
ourDog.bark = "bow-wow";
ourDog["bark"] = "bow-wow";
```
* Delete Properties
```js
delete ourDog.bark;
```
* Testing Objects for Properties
```js
var myObj = {
  top: "hat",
  bottom: "pants"
};
myObj.hasOwnProperty("top");    // true
myObj.hasOwnProperty("middle"); // false
```

# while
```js
var ourArray = [];
var i = 0;
while(i < 5) {
  ourArray.push(i);
  i++;
}
```
# For Loops
for ([initialization]; [condition]; [final-expression])
```js
var ourArray = [];
for (var i = 0; i < 5; i++) {
  ourArray.push(i);
}
```
```js
var ourArray = [];
for (var i=10; i > 0; i-=2) {
  ourArray.push(i);
}
```
```js
var arr = [10,9,8,7,6];
for (var i = 0; i < arr.length; i++) {
   console.log(arr[i]);
}
```
# Do...While Loops
```js
var ourArray = [];
var i = 0;
do {
  ourArray.push(i);
  i++;
} while (i < 5);
```

# Recursion
```js
function multiply(arr, n) {
    var product = arr[0];
    for (var i = 1; i <= n; i++) {
        product *= arr[i];
    }
    return product;
  }
```
```js
function multiply(arr, n) {
    if (n <= 0) {
      return arr[0];
    } else {
      return multiply(arr, n - 1) * arr[n];
    }
  }
```

# Random Fractions
Math.random() function that generates a random decimal number between 0 (inclusive) and not quite up to 1 (exclusive). Thus Math.random() can return a 0 but never quite return a 1
### Random Whole Numbers
* Use Math.random() to generate a random decimal.
* Multiply that random decimal by 20.
* Use another function, Math.floor() to round the number down to its nearest whole number.
```js
Math.floor(Math.random() * 20);
```
### Random Whole Numbers within a Range
```js
Math.floor(Math.random() * (max - min + 1)) + min
```
```js
function ourRandomRange(ourMin, ourMax) {
  return Math.floor(Math.random() * (ourMax - ourMin + 1)) + ourMin;
}
ourRandomRange(1, 9);
```

# parseInt 
The parseInt() function parses a string and returns an integer. Here's an example:
```js
var a = parseInt("007");
```
The above function converts the string "007" to an integer 7. If the first character in the string can't be converted into a number, then it returns NaN.
### parseInt Function with a Radix  
The parseInt() function parses a string and returns an integer. It takes a second argument for the radix, which specifies the base of the number in the string. The radix can be an integer between 2 and 36.  
The function call looks like:  
```js
parseInt(string, radix);
```
And here's an example:
```js
var a = parseInt("11", 2);
```
The radix variable says that "11" is in the binary system, or base 2. This example converts the string "11" to an integer 3.

# Conditional 
```js
condition ? statement-if-true : statement-if-false;
```
```js
function findGreater(a, b) {
  if(a > b) {
    return "a is greater";
  }
  else {
    return "b is greater";
  }
}
```
```js
function findGreater(a, b) {
  return a > b ? "a is greater" : "b is greater";
}
```
### Multiple Conditional
```js
function findGreaterOrEqual(a, b) {
  return (a === b) ? "a and b are equal" : (a > b) ? "a is greater" : "b is greater";
}
```


