# Array 
###  Access an Array's Contents Using Bracket Notation
```js
let myArray = ["a", "b", "c", "d"];
myArray[1]=3;
```
###  Add Items to an Array with push() and unshift()
###  Remove Items from an Array with pop() and shift()
###  Remove Items Using splice()
    * remove any number of consecutive elements from anywhere in an array.
    * splice() can take up to 3 parameters, but for now, we'll focus on just the first 2. The first two parameters of splice() are integers which represent indexes, or positions, of the array that splice() is being called upon. And remember, arrays are zero-indexed, so to indicate the first element of an array, we would use 0. splice()'s first parameter represents the index on the array from which to begin removing elements, while the second parameter indicates the number of elements to delete
```js
let array = ['I', 'am', 'feeling', 'really', 'happy'];
let newArray = array.splice(3, 2);
// newArray equals ['really', 'happy']
// array equals ['I', 'am', 'feeling']
```
### Add Items Using splice()  
  * Remember in the last challenge we mentioned that splice() can take up to three parameters? Well, you can use the third parameter, comprised of one or more element(s), to add to the array.
```js
const numbers = [10, 11, 12, 12, 15];
const startIndex = 3;
const amountToDelete = 1;

numbers.splice(startIndex, amountToDelete, 13, 14);
// the second entry of 12 is removed, and we add 13 and 14 at the same index
console.log(numbers);
// returns [ 10, 11, 12, 13, 14, 15 ]
```
### Copy Array Items Using slice()
slice() takes only 2 parameters — the first is the index at which to begin extraction, and the second is the index at which to stop extraction (extraction will occur up to, but not including the element at this index). Consider this:
```js
let weatherConditions = ['rain', 'snow', 'sleet', 'hail', 'clear'];
let todaysWeather = weatherConditions.slice(1, 3);
// todaysWeather equals ['snow', 'sleet'];
// weatherConditions still equals ['rain', 'snow', 'sleet', 'hail', 'clear']
```
### Copy an Array with the Spread Operator
```js
let thisArray = [true, true, undefined, false, null];
let thatArray = [...thisArray];
// thatArray equals [true, true, undefined, false, null]
// thisArray remains unchanged, and is identical to thatArray
```

### Combine Arrays with the Spread Operator
```js
let thisArray = ['sage', 'rosemary', 'parsley', 'thyme'];

let thatArray = ['basil', 'cilantro', ...thisArray, 'coriander'];
// thatArray now equals ['basil', 'cilantro', 'sage', 'rosemary', 'parsley', 'thyme', 'coriander']
```

### Check For The Presence of an Element With indexOf
```js
let fruits = ['apples', 'pears', 'oranges', 'peaches', 'pears'];
fruits.indexOf('dates'); // returns -1
fruits.indexOf('oranges'); // returns 2
fruits.indexOf('pears'); // returns 1, the first index at which the element exists
```

### Iterate Through All an Array's Items Using For Loops
```js
function greaterThanTen(arr) {
  let newArr = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 10) {
      newArr.push(arr[i]);
    }
  }
  return newArr;
}
greaterThanTen([2, 12, 8, 14, 80, 0, 1]);
// returns [12, 14, 80]
```

### Create complex multi-dimensional arrays

# Objects
### Add Key-Value Pairs to JavaScript Objects
```js
let FCC_User = {
  username: 'awesome_coder',
  followers: 572,
  points: 1741,
  completedProjects: 15
};
```
###  Modify an Object Nested Within an Object
```js
let userActivity = {
  id: 23894201352,
  date: 'January 1, 2017',
  data: {
    totalUsers: 51,
    online: 42
  }
};

// change code below this line
userActivity.data.online=45;
// change code above this line
```
### Access Property Names with Bracket Notation
```js
let selectedFood = getCurrentFood(scannedItem);
let inventory = foods[selectedFood];
```

### Use the delete Keyword to Remove Object Properties
```js
delete foods.apples;
```

### Check if an Object has a Property
```js
users.hasOwnProperty('Alan');
'Alan' in users;
// both return true
```

# Iterate Through the Keys of an Object with a for...in Statement
```js
for (let user in users) {
  console.log(user);
}

// logs:
Alan
Jeff
Sarah
Ryan
```

### Generate an Array of All Object Keys with Object.keys()
```js
function getArrayOfUsers(obj) {
  // change code below this line
  var result=[];
  for(let user in obj){
    result.push(user);
  }
  return result;
}
```
```js
function getArrayOfUsers(obj) {
  // change code below this line
  return Object.keys(obj);
  // change code above this line
}
```
