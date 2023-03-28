let numbers, cont, numbers_list = [];
cont = true;
do {
  numbers = parseInt(prompt('Enter the numbers! '));
  if (numbers_list.includes(numbers)) {
    cont = false;
    alert('Number has already been entered.');
  } else {
    numbers_list.push(numbers);
  }
} while (cont);

numbers_list.sort(function(a, b) {
  return a - b;
});
for (let i = 0; i < numbers_list.length; i++) {

  console.log(numbers_list[i]);

}