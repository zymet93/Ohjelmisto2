const nums_list = [];
let numbers,counter=1;

do {
  numbers = parseInt(prompt('Enter the '+counter+'. number! '));
  nums_list.push(numbers);
  counter++
} while (nums_list.length < 5);

for (i = nums_list.length - 1; i >= 0; i--) {
  console.log(nums_list[i]);
}