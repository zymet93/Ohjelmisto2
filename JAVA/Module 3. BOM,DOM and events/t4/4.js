'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const target = document.querySelector('#target')

for(let student of students) {
  const option = document.createElement('option')
  option.innerText = student.name;
  option.value = student.id;
  target.appendChild(option);
}