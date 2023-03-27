'use strict';

function rollDice(dice) {
  let randomNum,sum = 0;
  for (let i = 1; i <= dice; i++) {
    randomNum = Math.floor(Math.random() * 6) + 1;
//  document.querySelector('#target').innerHTML = i+'. dice'+ randomNum;
    sum += randomNum;
  }
  return sum;
}

let dice, eyes, prob, count = 0;
dice = parseInt(prompt('How many dice would you like to roll? '));
eyes = parseInt(prompt('How many eyes would you like to have? '));

for (let i = 0; i < 10000; i++) {
  if (rollDice(dice) === eyes) {
    count++;
    console.log(count);
  }
}
prob = (count / 10000) * 100;

document.querySelector('#target').innerHTML =
    'The probability to get sum ' + eyes + ' with ' + dice + ' dice is ' +
    prob + '%';