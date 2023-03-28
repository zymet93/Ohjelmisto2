//Write a program that asks the user for numbers until he gives zero.
// The given numbers are printed in the console from the largest to the smallest. (2p)

let numbers, numbers_list = [];

do {
  numbers = parseInt(prompt('Enter the numbers! '));
  numbers_list.push(numbers);
} while (numbers > 0);

numbers_list.sort((a, b) => b - a);

for (let i = 0; i < numbers_list.length; i++) {

  console.log(numbers_list[i]);

}