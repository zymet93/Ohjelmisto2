const answer = confirm('Should I calculate the square root?');
if (answer == true) {
  const num = parseInt(prompt('Enter a number! '));
  if (num < 0) {
    document.querySelector(
        '#target').innerHTML = 'The square root of a negative number is not defined';
  } else {
    sq_num = Math.sqrt(num);

    document.querySelector('#target').innerHTML = sq_num;

  }
} else {
  document.querySelector(
      '#target').innerHTML = 'The square root is not calculated';
}
// printing the response to the console
console.log(answer);
