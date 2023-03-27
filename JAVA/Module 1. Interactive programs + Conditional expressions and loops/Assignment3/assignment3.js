//Write a program that prompts for three integers.
// The program prints the sum, product and average of the numbers to the HTML document. (3p)

'use strict';
const num1 = parseInt(prompt('first number? '));
const num2 = parseInt(prompt('second number? '));
const num3 = parseInt(prompt('third number? '));

let sum = num1 + num2 + num3;
let product = num1 * num2 * num3;
let avg = sum / 3;

document.querySelector('#target').innerHTML = 'sum ' + sum;

document.querySelector('#target1').innerHTML = 'product ' + product;

document.querySelector('#target2').innerHTML = 'average ' + avg;