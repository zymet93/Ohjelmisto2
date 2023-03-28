function even(numbersArray) {
  let evenArray = [];
  for (let i = 0; i < numbersArray.length; i++) {
    if (numbersArray[i] % 2 === 0) {
      evenArray.push(numbersArray[i]);
    }
  }
  return evenArray;
}

const numbers = [2, 7, 4];
const evenNumbers = even(numbers);

console.log("Original array: ", numbers);
console.log("Even numbers: ", evenNumbers);

const consoleOutput = document.getElementById("console-output");
consoleOutput.innerHTML = "Original array: " + numbers + "<br>";
consoleOutput.innerHTML += "Even numbers: " + evenNumbers;
