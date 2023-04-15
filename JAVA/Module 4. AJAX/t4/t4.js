   const form = document.getElementById('search-form');
    const resultsContainer = document.getElementById('results');

    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      const query = event.target.elements['q'].value;

      resultsContainer.innerHTML = '';

      const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
      const data = await response.json();

      data.forEach((tvShow) => {
        const article = document.createElement('article');
        const heading = document.createElement('h2');
        const link = document.createElement('a');
        const image = document.createElement('img');
        const summary = document.createElement('div');

        heading.textContent = tvShow.show.name;
        link.href = tvShow.show.url;
        link.target = '_blank';
        link.textContent = tvShow.show.url;
        image.src = tvShow.show.image ? tvShow.show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
        image.alt = tvShow.show.name;
        summary.innerHTML = tvShow.show.summary;

        article.appendChild(heading);
        article.appendChild(link);
        article.appendChild(image);
        article.appendChild(summary);

        resultsContainer.appendChild(article);
      });
    });