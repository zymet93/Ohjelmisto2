let cls, name;
const house = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw'];
cls = Math.floor(Math.random() * 4) + 1;
name = prompt('what is your name? ');
switch (cls) {
  case 1:
    document.querySelector('#target').innerHTML = name + ' you are in ' +
        house[0];
    break;
  case 2:
    document.querySelector('#target').innerHTML = name + ' you are in ' +
        house[1];
    break;
  case 3:
    document.querySelector('#target').innerHTML = name + ' you are in ' +
        house[2];
    break;

  case 4:
    document.querySelector('#target').innerHTML = name + ' you are in ' +
        house[3];
    break;

}


