'use strict ';

async function fetchChuckNorrisJoke() {
  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random');
    const data = await response.json();
    console.log(data.value);

    const jokeElement = document.getElementById('joke');
    jokeElement.innerText = data.value;
  } catch (error) {
    console.error(error);
  }
}

fetchChuckNorrisJoke();
