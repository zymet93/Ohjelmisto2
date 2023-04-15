document.addEventListener('DOMContentLoaded', () => {
  const searchForm = document.querySelector('#search-form');
  const searchInput = document.querySelector('#query');

  searchForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const query = searchInput.value;
    const apiUrl = `https://api.tvmaze.com/search/shows?q=${query}`;

    try {
      const response = await fetch(apiUrl);
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    }
  });
});
