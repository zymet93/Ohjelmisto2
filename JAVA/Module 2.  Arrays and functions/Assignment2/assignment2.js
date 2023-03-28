'use strict';

const name_list = [];
const participants = parseInt(prompt('How many people are participating?'));

for (let i = 0; i < participants; i++) {
  const name = prompt(`Enter name ${i+1}:`);
  name_list.push(name);
}

name_list.sort();

const list = document.getElementById("name_list");

for (let i = 0; i < name_list.length; i++) {
  const li = document.createElement('li');
  li.innerText = name_list[i];
  list.appendChild(li);
}

