# Use the JavaScript Console to Check the Value of a VariablePassed
```js
console.log('Hello world!');
```
```js
let a = 5;
let b = 1;
a++;
// Add your code below this line
let sumAB = a + b;
console.log(sumAB);
```

# Use typeof to Check the Type of a Variable
```js
console.log(typeof ""); // outputs "string"
console.log(typeof 0); // outputs "number"
console.log(typeof []); // outputs "object"
console.log(typeof {}); // outputs "object"
```


# Debugging
* Catch Misspelled Variable and Function Names
* Catch Unclosed Parentheses, Brackets, Braces and Quotes
* Catch Mixed Usage of Single and Double Quotes
* Catch Use of Assignment Operator Instead of Equality Operator
* Catch Missing Open and Closing Parenthesis After a Function Call
```js
function myFunction() {
  return "You rock!";
}
let varOne = myFunction; // set to equal a function
let varTwo = myFunction(); // set to equal the string "You rock!"
```
* Catch Arguments Passed in the Wrong Order When Calling a Function
* Catch Off By One Errors When Using Indexing
* Use Caution When Reinitializing Variables Inside a Loop
* Prevent Infinite Loops with a Valid Terminal Condition
