
// alert("Welcome to JS");

// Chapter 1 : //Introduction, Variables & Data Type

// Our 1st JS code
console.log("Hello World!");
console.log('This is Kartik C T');

// in console we can do basic calculations
age = 21;
console.log(age);
age = age + 1;

// Variable naming conventions
// 1. Variable names are case sensitive; “a” & “A” is different.
fullName = "Kartik";
fullname = "Xon";
console.log(fullName);
console.log(fullname);

// 2. Only letters, digits, underscore( _ ) and $ is allowed. (not even space)
cityName = "Hangal";
city_Name = "Hangal";
city$Name = "Hangal";
// city Name = "Hangal"; // not allowed

// 3. Only a letter, underscore( _ ) or $ should be 1st character.
animal7 = "Dog";
// 7animal = "Dog"; // not allowed

// 4. Reserved words cannot be variable names.
// var, let, const, if, else, for, while, do, break, true, false, null, undefined etc.

// 5. Use meaningful names (not a,b,c or x,y,z)
var studentName = "Kartik";
var studentAge = 21;
var studentCity = "Hangal";

// Variable declaration keywords
// var, let, const

var age = 21;
var age = 22; // re-declaration allowed
age = 23; // update allowed
console.log(age);

{
    let age1 = 21;
    // let age1 = 22; // re-declaration not allowed
    age1 = 25; // update allowed
    console.log(age1);
}

{
    const age2 = 21;
    // const age2 = 22; // re-declaration not allowed
    // age2 = 25; // update not allowed
    console.log(age2);
}

// Data Types in JS

fullName = "Kartik C T";
age = 21;
isStudent = true;
x = null;
y = undefined;

id = Symbol('id');
person = { name: "Kartik", age: 21 };
fruits = ["Apple", "Banana", "Orange"];
greet = function() { console.log("Hello!"); }

// Function to display data type
console.log(typeof fullName);
console.log(typeof age);
console.log(typeof isStudent);
console.log(typeof x);
console.log(typeof y);

console.log(typeof id);
console.log(typeof person);
console.log(typeof fruits);
console.log(typeof greet);

const student = {
    name: "Kartik",
    age: 21,
    isStudent: true,
    city: "Hangal"
};

console.log(student["age"]);
console.log(student['age']);
console.log(student.age);
console.log(student[age]); // undefined


student["age"] = student["age"] + 1;
student['age'] = 23

console.log(student["age"]);

student["name"] = "Xon";
console.log(student.name);

// Chapter 2 : Comments, Operators & Conditional Statements

// Comments in JS
// Single line comment
/* Multi line comment
   Multi line comment */

// Operators in JS

// Arithmetic Operators : +, -, *, /, %, **, ++, --
let a = 5;
let b = 2;

console.log("a = ", a, "& b = ", b);
console.log("a + b = ", a + b);
console.log("a - b = ", a - b);
console.log("a * b = ", a * b);
console.log("a / b = ", a / b);
console.log("a % b = ", a % b); // modulus operator (remainder)
console.log("a ** b = ", a ** b);

// Unary Operators : ++, --
let c = 5;
let d = 2;

console.log("c = ", c, "& d = ", d);
console.log("++c = ", ++c);
console.log("--d = ", --d);
console.log("c++ = ", c++);
console.log("d-- = ", d--);

// Assignment Operators : =, +=, -=, *=, /=, %=, **=
let e = 5;
console.log("e = ", e);
e += 3;
console.log("e += 3; e = ", e);
e -= 2;
console.log("e -= 2; e = ", e);
e *= 2;
console.log("e *= 2; e = ", e);
e /= 3;
console.log("e /= 3; e = ", e);
e %= 2;
console.log("e %= 2; e = ", e);
e **= 3;
console.log("e **= 3; e = ", e);

// Comparison Operators : ==, ===, !=, !==, >, <, >=, <=
let f = 5;
let g = '5';
console.log("f = ", f, "& g = ", g);
console.log("f == g : ", f == g); // value
console.log("f === g : ", f === g); // value + data type
console.log("f != g : ", f != g); // value
console.log("f !== g : ", f !== g); // value + data type
let h = 3;
let i = 7;
console.log("h = ", h, "& i = ", i);
console.log("h > i : ", h > i);
console.log("h < i : ", h < i);
console.log("h >= i : ", h >= i);
console.log("h <= i : ", h <= i);

// Logical Operators : &&, ||, !
let j = 5;
let k = 10;
console.log("j = ", j, "& k = ", k);
console.log("j > 0 && k > 0 : ", j > 0 && k > 0); // AND Both true
console.log("j > 0 && k < 0 : ", j > 0 && k < 0); // AND One false
console.log("j < 0 && k < 0 : ", j < 0 && k < 0); // AND Both false
console.log("j > 0 || k > 0 : ", j > 0 || k > 0); // OR Both true
console.log("j > 0 || k < 0 : ", j > 0 || k < 0); // OR One true
console.log("j < 0 || k < 0 : ", j < 0 || k < 0); // OR Both false
console.log("!(j > 0) : ", !(j > 0)); // NOT

// Conditional Statements : if, if...else, if...else if...else, switch

// if statement
let color;
if (mode = "dark") {
    color = "black";
}

// if...else statement
let age1 = 21;
if (age1 >= 18) {
    console.log("You are eligible to vote.");
} else {
    console.log("You are not eligible to vote.");
}

// if...else if...else statement
let age2 = 65;
if (age2 < 18) {
    console.log("You are a minor.");
} else if (age2 >= 18 && age2 < 60) {
    console.log("You are an adult.");
} else {
    console.log("You are a senior citizen.");
}

// Ternary Operator
let age3 = 21;
console.log(age3 > 18 ? "adult" : "minor");

// switch statement
const expr = 'Papayas';
switch (expr) {
    case 'Oranges':
        console.log('Oranges are $0.59 a pound.');
        break;
    case 'Mangoes':
    case 'Papayas':
        console.log('Mangoes and papayas are $2.79 a pound.');
        // expected output: "Mangoes and papayas are $2.79 a pound."
        break;
    default:
        console.log(`Sorry, we are out of ${expr}.`);
}
