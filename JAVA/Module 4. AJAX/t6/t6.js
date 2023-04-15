const searchForm = document.getElementById("search-form");
const searchInput = document.getElementById("search-input");
const jokesContainer = document.getElementById("jokes-container");

searchForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const searchTerm = searchInput.value;
    const url = `https://api.chucknorris.io/jokes/search?query=${searchTerm}`;
    fetch(url)
        .then(response => response.json())
        .then(data => {
            jokesContainer.innerHTML = "";
            data.result.forEach(joke => {
                const article = document.createElement("article");
                const jokeParagraph = document.createElement("p");
                jokeParagraph.textContent = joke.value;
                article.appendChild(jokeParagraph);
                jokesContainer.appendChild(article);
            });
        })
        .catch(error => console.error(error));
});