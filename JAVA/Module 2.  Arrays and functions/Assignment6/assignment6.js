function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}
const resultList = document.createElement('ul');
document.body.appendChild(resultList);

let roll = 0;
while (roll !== 6) {
  roll = rollDice();
  const listItem = document.createElement('li');
  listItem.innerText = `Roll: ${roll}`;
  resultList.appendChild(listItem);
}
