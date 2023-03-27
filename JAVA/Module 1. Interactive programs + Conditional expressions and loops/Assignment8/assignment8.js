
const start_year = parseInt(prompt('enter a starting year! '));
const end_year = parseInt(prompt('enter an ending year! '));
const target = document.querySelector('#target');

for (let year = start_year; year <= end_year; year++) {
  if (year % 400 == 0 || year % 4 == 0 && year % 100 != 0) {
    target.innerHTML += `<li>${year}</li>`;
    console.log(year);
  }
}

