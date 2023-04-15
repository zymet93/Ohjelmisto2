const form = document.querySelector('#search-form');
const resultsContainer = document.querySelector('#results');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const query = document.querySelector('#query').value;
  const url = `https://api.tvmaze.com/search/shows?q=${query}`;
  try {
    const response = await fetch(url);
    const data = await response.json();
    displayResults(data);
  } catch (error) {
    console.error(error);
  }
});

function displayResults(data) {
  resultsContainer.innerHTML = '';

  if (data.length === 0) {
    resultsContainer.innerHTML = '<p>No results found.</p>';
    return;
  }

  data.forEach((result) => {
        const show = result.show;
        const name = show.name;
        const image = show.image?.medium ||
            'https://via.placeholder.com/210x295?text=No+image+available';
        const summary = show.summary;
        const url = show.url;

        const articleElement = document.createElement('article');
        articleElement.classList.add('show');
        articleElement.innerHTML = `
      <img src="${image}" alt="${name}">
      <h2>${name}</h2>
      <a href="${url}" target="_blank">${url}</a>
      <div>${summary}</div>
    `;

        resultsContainer.appendChild(articleElement);
      }
  );
}