// Function that returns a closure for division
function divideBy(firstNumber) {
    return function(secondNumber) {
      return secondNumber / firstNumber;
    };
  }
  
  // Function that returns a closure for addition
  function addBy(firstNumber) {
    return function(secondNumber) {
      return firstNumber + secondNumber;
    };
  }
  
  // Creating closures with specific values
  const addBy100 = addBy(100);
  const addBy1000 = addBy(1000);
  const divideBy10 = divideBy(10);
  const divideBy100 = divideBy(100);
// Test
console.log(addBy100(20));     
console.log(divideBy10(20));   
console.log(divideBy100(200)); 
console.log(addBy1000(20)); 