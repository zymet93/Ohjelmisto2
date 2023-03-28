//Write a program that asks for the names of six dogs.
// The program prints dog names to unordered list <ul> in reverse alphabetical order. (2p)

'use strict';

const name_list = [];

for (let i = 1; i <= 6; i++) {
  const name = prompt(`Enter dog ${i}:`);
  name_list.push(name);
}

name_list.sort();
name_list.reverse();

const list = document.getElementById('name_list');

for (let i = 0; i < name_list.length; i++) {
  const li = document.createElement('li');
  li.innerText = name_list[i];

  list.appendChild(li);

}

