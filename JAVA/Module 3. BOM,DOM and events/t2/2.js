const targetElement = document.getElementById("target");

const ulElement = document.createElement("ul");

// Create the li elements
const liElement1 = document.createElement("li");
liElement1.textContent = "First item";

const liElement2 = document.createElement("li");
liElement2.textContent = "Second item";
liElement2.classList.add("my-item");

const liElement3 = document.createElement("li");
liElement3.textContent = "Third item";

ulElement.appendChild(liElement1);
ulElement.appendChild(liElement2);
ulElement.appendChild(liElement3);

// Append the ul element to the target element
targetElement.appendChild(ulElement);
