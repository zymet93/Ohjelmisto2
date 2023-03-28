function concat(str) {
    let strings = " ";
    for (let i in str) {
      strings += str[i];
    }
    return strings;
  }
  const ul = document.createElement("ul");
  const checklist = [" Johnny", " DeeDee", " Joey", " Marky"];
  ul.innerHTML = concat(checklist);
  document.body.appendChild(ul);