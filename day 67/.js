// 1. Which of the following keywords allows redeclaration within the same scope?
//  a) var b) let c)const d) None

// a . var ---> it allows the declaration. and it is used in globel scope. for the leakage purpose
//              we using very rarely


// 2. What will be the output? console.log(a); var a = 5;
//  a) undefined b) 5 c) ReferenceError d)TypeError

// a . undefined ---> var is allows the hoisting so as per the memory_phase it is undefined


// 3. Which of these has block scope in JavaScript?
//  a) var b) let c) const d) Both b and c

// d . let,const ---> let,const is block_scope variable. when we using them in block_scope it wont
//                    leaks the code after the function execution


// 4. Which variable cannot be reassigned once assigned?
//  a) var b) let c) const d) None

// c) const ---> this variable cant assign. if it holds an object or array we cant change that.


// 5. Which keyword is hoisted but initialized with undefined?
//  a) var b) let c) const d) None

// a) var ---> 


// 6. Which keyword leads to Temporal Dead Zone (TDZ) error if accessed before declaration? 
// a) var b) let c) const d) Both b and c

// d) both b and c


// 7. Which of these is allowed? const obj = {name: 'JS'}; obj.name = 'JavaScript';
//  a) Allowed b) NotAllowed

// a) allowed


// 8. What is the default value of a let variable if declared but not initialized?
//  a) null b) undefined c) 0 d) ReferenceError

// b) undefined


// 9. Which of the following can be redeclared in the same scope?
//  a) var b) let c) const d) None

// a) var


// 10. What is the scope of var declared inside a function?
//  a) Global b) Block c) Function d) Module

// c) function


// 11. What will this log? console.log(x); let x = 10;
//  a) undefined b) 10 c) ReferenceError d) null

// c) reference error


// 12. What will be the result? console.log(a); var a; a = 20; 
// a) undefined b) 20 c) ReferenceError d)TypeError

// a) undefined


// 13. What happens if we redeclare a let variable in the same scope? 
// a) It overwrites the old value b)It throws an error c) It creates a new variable d) It works like var

// b) it throws error


// 14. What happens if we try to change a const variable's value? a) It throws a TypeError b) It
// changes silently c) It behaves like let d) It creates a new variable

// a) it throw type error


// 15. Which variables are added to the global object (window in browsers)? a) var (in global scope) b)
// let (in global scope) c) const (in global scope) d) All of them

// a) var


// 16. Which of the following will not throw an error? { var a = 1; let b = 2; const c = 3; } console.log(a);
// a) a b) b c) c d) All throw error

// a) a


// 17. When is a variable declared with let accessible? a) Before its declaration (hoisting) b) After its
// declaration c) Anywhere in the function d) Anywhere in the file

// b) after its declaration


// 18. Which statement about const is TRUE? a) It makes the variable completely immutable b) It only
// prevents reassignment, not mutation of objects/arrays c) It cannot be hoisted d) It is
// function-scoped

// b) b


// 19. What will be logged? var x = 5; { var x = 10; } console.log(x); a) 5 b) 10 c) ReferenceError d)
// undefined

// b) 10


// 20. What will this code do? const a; a = 10; a) Works fine b) Throws SyntaxError c) Throws
// ReferenceError d) Returns undefined

// b) syntax error


// 21. Which of these is block-scoped? a) for (let i = 0; i < 5; i++) {} b) for (var i = 0; i < 5; i++) {} c) for
// (const i = 0; i < 5; i++) {} d) Both a and c

// a


// 22. What happens when var is declared twice in the same function? a) Error occurs b) Ignores
// second declaration c) Redeclares variable d) Creates new memory location

// c) redeclares variable


// 23. Which will throw an error? const arr = [1, 2]; arr.push(3); console.log(arr); a) Throws Error b)
// Logs [1, 2, 3]

// b


// 24. What will this output? { let a = 5; } console.log(a);
//  a) 5 b) undefined c) ReferenceError d) null

// c) reference error


// 25. Which of the following is TRUE about let and const? a) They are hoisted but in TDZ b) They are
// not hoisted at all c) They behave exactly like var d) They can be accessed before declaration

// a


// 26. What will happen? console.log(b); var b = 20; 
// a) undefined b) 20 c) ReferenceError d) null

// a) undefined


// 27. Which one allows declaration without initialization? a) var b) let c) const d) Both a and b

// d) both a and b


// 28. Which one is NOT a valid declaration? a) var x; b) let y; c) const z; d) None

// c


// 29. What will happen if you use var inside a block? a) It is block-scoped b) It is function-scoped c) It
// is globally scoped d) It throws an error

// b) it is function scoped


// 30. Which keyword is recommended for declaring variables that should not change?
//  a) var b) let c)const d) None

// const


// 31. Which is true? let x; console.log(x); a) undefined b) ReferenceError c) null d) SyntaxError

// a) undefined


// 32. Which is NOT allowed? a) const x = 10; b) const x; x = 10; c) let y; y = 20; d) var z = 30;

// b 


// 33. What is the output? var a = 1; { let a = 2; console.log(a); } a) 1 b) 2 c) undefined d)
// ReferenceError

// b) 2


// 34. What is the output? var x = 1; let x = 2; console.log(x); a) 2 b) 1 c) ReferenceError d) undefined

// c


// 35. Which of these avoids accidental redeclaration? a) var b) let c) const d) Both b and c

// d


// 36. Which one is most suitable for declaring loop counters? a) var b) let c) const d) None

// b) let


// 37. Which of the following allows you to reassign values? 
// a) const b) let c) Both a and b d) Neither anor b

// b) let


// 38. What happens if you declare a global let variable with the same name as a global var? a) It
// overwrites var b) It throws SyntaxError c) It works independently d) It creates a new global property

// b) it throws SyntaxError


// 39. Which is not hoisted? a) var b) function declarations c) let d) Both a and b

// c) let


// 40. Which of the following is true about const objects? a) Properties can be changed b) The object
// reference cannot be reassigned c) Both a and b d) Neither a nor b

// b) both a and b