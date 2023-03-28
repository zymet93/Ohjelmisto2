function rollDice(numSides) {
  return Math.floor(Math.random() * numSides) + 1;
}
const resultList = document.createElement('ul');
document.body.appendChild(resultList);

const maxNumber = parseInt(prompt('Enter the maximum number on the dice: '));
let roll = 0;

while (roll !== maxNumber) {
  roll = rollDice(maxNumber);
  const listItem = document.createElement('li');
  listItem.innerText = `Roll: ${roll}`;
  resultList.appendChild(listItem);
}
