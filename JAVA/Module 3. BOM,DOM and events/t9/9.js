'use strict';
const button = document.getElementById('start');
const calc = document.querySelector('#result');
button.addEventListener('click', options);

function options() {
  let x = document.getElementById('calculation').value;
  let result = Function('return ' + x)();
  calc.innerHTML = result;

}