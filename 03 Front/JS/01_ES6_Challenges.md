# var and let Keywords  
* var keyword is that you can overwrite variable declarations without an error.
```js
var camper = 'James';
var camper = 'David';
console.log(camper);
// logs 'David'
```
* If you were to replace var with let in the variable declarations of the code above, the result would be an error.  
```js
let camper = 'James';
let camper = 'David'; // throws an error
```
* When you declare a variable with the var keyword, it is declared globally, or locally if declared inside a function.
* The let keyword behaves similarly, but with some extra features. When you declare a variable with the let keyword inside a block, statement, or expression, its scope is limited to that block, statement, or expression.
```js
var printNumTwo;
for (var i = 0; i < 3; i++) {
  if (i === 2) {
    printNumTwo = function() {
      return i;
    };
  }
}
console.log(printNumTwo());
// returns 3
```
```js
'use strict';
let printNumTwo;
for (let i = 0; i < 3; i++) {
  if (i === 2) {
    printNumTwo = function() {
      return i;
    };
  }
}
console.log(printNumTwo());
// returns 2
console.log(i);
// returns "i is not defined"
```
```js
function checkScope() {
  'use strict';
  let i = 'function scope';
  if (true) {
    let i = 'block scope';
    console.log('Block scope i is: ', i);//"block scope"
  }
  console.log('Function scope i is: ', i);//"function scope"
  return i;
}

```
# use strict
"use strict". This enables Strict Mode, which catches common coding mistakes and "unsafe" actions. For instance:
```js
"use strict";
x = 3.14; // throws an error because x is not declared
```


# const 
const has all the awesome features that let has, with the added bonus that variables declared using const are read-only. They are a constant value, which means that once a variable is assigned with const, it cannot be reassigned.
```js
"use strict";
const FAV_PET = "Cats";
FAV_PET = "Dogs"; // returns error
```

# Mutate an Array Declared with const
However, it is important to understand that objects (including arrays and functions) assigned to a variable using const are still mutable. Using the const declaration only prevents reassignment of the variable identifier.
```js
"use strict";
const s = [5, 6, 7];
s = [1, 2, 3]; // throws error, trying to assign a const
s[2] = 45; // works just as it would with an array declared with var or let
console.log(s); // returns [5, 6, 45]
```

# Prevent Object Mutation
JavaScript provides a function Object.freeze to prevent data mutation. Once the object is frozen, you can no longer add, update, or delete properties from it. Any attempt at changing the object will be rejected without an error.  
```js
let obj = {
  name:"FreeCodeCamp",
  review:"Awesome"
};
Object.freeze(obj);
obj.review = "bad"; // will be ignored. Mutation not allowed
obj.newProp = "Test"; // will be ignored. Mutation not allowed
console.log(obj); 
// { name: "FreeCodeCamp", review:"Awesome"}
```
# Use Arrow Functions to Write Concise Anonymous Functions
```js
const myFunc = function() {
  const myVar = "value";
  return myVar;
}
```
```js
const myFunc = () => {
  const myVar = "value";
  return myVar;
}
```
```js
const myFunc = () => "value";
```
# Write Arrow Functions with Parameters
```js
const doubler = (item) => item * 2;
```
```js
const doubler = item => item * 2;
```
```js
const multiplier = (item, multi) => item * multi;
```
# Set Default Parameters for Your Functions
```js
function greeting(name = "Anonymous") {
  return "Hello " + name;
}
console.log(greeting("John")); // Hello John
console.log(greeting()); // Hello Anonymous
```
# Use the Rest Parameter with Function Parameters
The rest parameter eliminates the need to check the args array and allows us to apply map(), filter() and reduce() on the parameters array.
```js
function howMany(...args) {
  return "You have passed " + args.length + " arguments.";
}
console.log(howMany(0, 1, 2)); // You have passed 3 arguments.
console.log(howMany("string", null, [1, 2, 3], { })); // You have passed 4 arguments.
```

# Use the Spread Operator to Evaluate Arrays In-Place
ES6 introduces the spread operator, which allows us to expand arrays and other expressions in places where multiple parameters or elements are expected.

The ES5 code below uses apply() to compute the maximum value in an array:
```js
var arr = [6, 89, 3, 45];
var maximus = Math.max.apply(null, arr); // returns 89
```
We had to use Math.max.apply(null, arr) because Math.max(arr) returns NaN. Math.max() expects comma-separated arguments, but not an array. The spread operator makes this syntax much better to read and maintain.
```js
const arr = [6, 89, 3, 45];
const maximus = Math.max(...arr); // returns 89
```
...arr returns an unpacked array. In other words, it spreads the array. However, the spread operator only works in-place, like in an argument to a function or in an array literal. The following code will not work:
```js
const spreaded = ...arr; // will throw a syntax error
```
```js
const arr1 = ['JAN', 'FEB', 'MAR', 'APR', 'MAY'];
let arr2;
arr2 = [...arr1];//Copy all contents of arr1 into another array arr2
```

# Destructuring Assignment
* Use Destructuring Assignment to Extract Values from Objects
```js
const user = { name: 'John Doe', age: 34 };
const name = user.name; // name = 'John Doe'
const age = user.age; // age = 34
//or
const { name, age } = user;
// name = 'John Doe', age = 34
```
* Use Destructuring Assignment to Assign Variables from Objects
```js
const { name: userName, age: userAge } = user;
// userName = 'John Doe', userAge = 34
```
* Use Destructuring Assignment to Assign Variables from Nested Objects
```js
const user = {
  johnDoe: { 
    age: 34,
    email: 'johnDoe@freeCodeCamp.com'
  }
};
const { johnDoe: { age, email }} = user;
const { johnDoe: { age: userAge, email: userEmail }} = user;
```
* Use Destructuring Assignment to Assign Variables from Arrays
```js
const [a, b] = [1, 2, 3, 4, 5, 6];
console.log(a, b); // 1, 2
const [a, b,,, c] = [1, 2, 3, 4, 5, 6];
console.log(a, b, c); // 1, 2, 5
let a = 8, b = 6;
// swap a b
[a,b]=[b,a];
```
* Use Destructuring Assignment with the Rest Parameter to Reassign Array Elements
```js
const [a, b, ...arr] = [1, 2, 3, 4, 5, 7];
console.log(a, b); // 1, 2
console.log(arr); // [3, 4, 5, 7]
```
* Use Destructuring Assignment to Pass an Object as a Function's Parameters
```js
const profileUpdate = (profileData) => {
  const { name, age, nationality, location } = profileData;
  // do something with these variables
}
```
```js
const profileUpdate = ({ name, age, nationality, location }) => {
  /* do something with these fields */
}
```
```js
const stats = {
  max: 56.78,
  min: -0.75,
};
const half=({max,min})=>(max + min)/2.0;
console.log(stats); // should be object
console.log(half(stats)); // should be 28.015

```

# Create Strings using Template Literals
```js
const person = {
  name: "Zodiac Hasbro",
  age: 56
};

// Template literal with multi-line and string interpolation
const greeting = `Hello, my name is ${person.name}!
I am ${person.age} years old.`;

console.log(greeting); // prints
// Hello, my name is Zodiac Hasbro!
// I am 56 years old.
```
A lot of things happened there. Firstly, the example uses backticks (`), not quotes (' or "), to wrap the string. Secondly, notice that the string is multi-line, both in the code and the output. This saves inserting \n within strings. The ${variable} syntax used above is a placeholder. Basically, you won't have to use concatenation with the + operator anymore. To add variables to strings, you just drop the variable in a template string and wrap it with ${ and }. Similarly, you can include other expressions in your string literal, for example ${a + b}. This new way of creating strings gives you more flexibility to create robust strings.
```js
const result = {
  failure: ["no-var", "var-on-top", "linebreak"],
};
function makeList(arr) {
  "use strict";
  const resultDisplayArray =arr.map(x=>`<li class="text-warning">${x}</li>`)
  return resultDisplayArray;
}
/**
 * makeList(result.failure) should return:
 * [ `<li class="text-warning">no-var</li>`,
 *   `<li class="text-warning">var-on-top</li>`,
 *   `<li class="text-warning">linebreak</li>` ]
 **/
const resultDisplayArray = makeList(result.failure);
```

# Write Concise Declarative Functions with ES6
ES5
```js
const person = {
  name: "Taylor",
  sayHello: function() {
    return `Hello! My name is ${this.name}.`;
  }
};
```
ES6
```js
const person = {
  name: "Taylor",
  sayHello() {
    return `Hello! My name is ${this.name}.`;
  }
};
```

# Use class Syntax to Define a Constructor Function
In ES5, we usually define a constructor function, and use the new keyword to instantiate an object.
```js
var SpaceShuttle = function(targetPlanet){
  this.targetPlanet = targetPlanet;
}
var zeus = new SpaceShuttle('Jupiter');
```
The class syntax simply replaces the constructor function creation:
```js
class SpaceShuttle {
  constructor(targetPlanet) {
    this.targetPlanet = targetPlanet;
  }
}
const zeus = new SpaceShuttle('Jupiter');
```

# Use getters and setters to Control Access to an Object
You can obtain values from an object, and set a value of a property within an object.  

These are classically called getters and setters.  

Getter functions are meant to simply return (get) the value of an object's private variable to the user without the user directly accessing the private variable.  

Setter functions are meant to modify (set) the value of an object's private variable based on the value passed into the setter function. This change could involve calculations, or even overwriting the previous value completely.  
```js
class Book {
  constructor(author) {
    this._author = author;
  }
  // getter
  get writer() {
    return this._author;
  }
  // setter
  set writer(updatedAuthor) {
    this._author = updatedAuthor;
  }
}
const lol = new Book('anonymous');
console.log(lol.writer);  // anonymous
lol.writer = 'wut';
console.log(lol.writer);  // wut
```

# export & Import
### Create a Module Script
```html
<script type="module" src="filename.js"></script>
```

### Use export to Share a Code Block
Imagine a file called math_functions.js, it contains several functions related to mathematical operations. One of them is stored in a variable, add, that takes in two numbers and returns the sum of them. You want to use this function in several different JavaScript files. In order to share it with the files, you need to first export it.
```js
export const add = (x, y) => {
  return x + y;
}
```
The above is a common way to export a single function, but you can achieve the same thing like this:
```js
const add = (x, y) => {
  return x + y;
}

export { add };
```
After you export a variable or function, you can import it in another file to use without having to rewrite the code. You can export multiple things by repeating the first example for each thing you want to export, or by placing them all in the export statement of the second example like this:
```js
export { add, subtract };
```

### Reuse Javascript Code Using import
import allows you to choose which parts of a file or module to load. In the previous lesson, the examples exported add from the math_functions.js file. Here's how you can import it to use in another file:
```js
import { add } from './math_functions.js';
```
Here, import will find add in math_functions.js, import just that function for you to use, and ignore the rest. The ./ tells the import to look for the math_functions.js file in the same folder as the current file. The relative file path (./) and file extension (.js) are required when using import in this way.

You can import more than one item from the file by adding them in the import statement like this:
```js
import { add, subtract } from './math_functions.js';
```
### Use * to Import Everything from a File
```js
import * as myMathModule from "./math_functions.js";
myMathModule.add(2,3);
myMathModule.subtract(5,3);
```
### Create an Export Fallback with export default
In the export lesson, you learned about the syntax referred to as a named export. This allowed you to make multiple functions and variables available for use in other files.

There is another export syntax you need to know, known as export default. Usually you will use this syntax if only one value is being exported from a file. It is also used to create a fallback value for a file or module.
```js
// named function
export default function add(x, y) {
  return x + y;
}

// anonymous function
export default function(x, y) {
  return x + y;
}
```
### Import a Default Export
```html
import add from "./math_functions.js";
```
The syntax differs in one key place. The imported value, add, is not surrounded by curly braces ({}). add here is simply a variable name for whatever the default export of the math_functions.js file is. You can use any name here when importing a default.


# Promise
A promise in JavaScript is exactly what it sounds like - you use it to make a promise to do something, usually asynchronously. When the task completes, you either fulfill your promise or fail to do so. Promise is a constructor function, so you need to use the new keyword to create one. It takes a function, as its argument, with two parameters - resolve and reject. These are methods used to determine the outcome of the promise. The syntax looks like this:
```js
const myPromise = new Promise((resolve, reject) => {
});
```
A promise has three states: pending, fulfilled, and rejected. The promise you created in the last challenge is forever stuck in the pending state because you did not add a way to complete the promise. The resolve and reject parameters given to the promise argument are used to do this. resolve is used when you want your promise to succeed, and reject is used when you want it to fail. These are methods that take an argument, as seen below.
```js
const myPromise = new Promise((resolve, reject) => {
  if(condition_here) {
    resolve("Promise was fulfilled");
  } else {
    reject("Promise was rejected");
  }
}
```
The example above uses strings for the argument of these functions, but it can really be anything. Often, it might be an object, that you would use data from, to put on your website or elsewhere.

### Handle a Fulfilled Promise with then
Promises are most useful when you have a process that takes an unknown amount of time in your code (i.e. something asynchronous), often a server request. When you make a server request it takes some amount of time, and after it completes you usually want to do something with the response from the server. This can be achieved by using the then method. The then method is executed immediately after your promise is fulfilled with resolve. Here’s an example:
```js
myPromise.then(result => {
  // do something with the result.
});
```
result comes from the argument given to the resolve method.
```js
const makeServerRequest = new Promise((resolve, reject) => {
  // responseFromServer is set to true to represent a successful response from a server
  let responseFromServer = true;
    
  if(responseFromServer) {
    resolve("We got the data");
  } else {  
    reject("Data not received");
  }
});

makeServerRequest.then(result=>{
  console.log(result);
})
```

### Handle a Rejected Promise with catch
```js
myPromise.catch(error => {
  // do something with the error.
});
```
```js
const makeServerRequest = new Promise((resolve, reject) => {
  // responseFromServer is set to false to represent an unsuccessful response from a server
  let responseFromServer = false;
    
  if(responseFromServer) {
    resolve("We got the data");
  } else {  
    reject("Data not received");
  }
});

makeServerRequest.then(result => {
  console.log(result);
});

makeServerRequest.catch(error=>{
  console.log(error);
})
```
