let num = parseInt(prompt('Enter a number: '));

// Check if the number is 1 or less than 1
if (num <= 1) {
  document.querySelector('#target').innerHTML = 'Not a prime number';
}
// Check if the number is 2 or 3
else if (num == 2 || num == 3) {
  document.querySelector('#target').innerHTML = 'Prime number';
}
// Check if the number is divisible by 2 or 3
else if (num % 2 == 0 || num % 3 == 0) {
  document.querySelector('#target').innerHTML = 'Not a prime number';
}
// Check if the number is divisible by any odd number up to the square root of the number
else {
  let limit = Math.sqrt(num);
  for (let i = 5; i <= limit; i += 6) {
    if (num % i == 0 || num % (i + 2) == 0) {
      document.querySelector('#target').innerHTML = 'Not a prime number';
    }
  }
  document.querySelector('#target').innerHTML = 'Prime number';
}
