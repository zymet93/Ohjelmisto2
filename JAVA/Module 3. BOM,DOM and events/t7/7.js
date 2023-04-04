const p = document.querySelector('p');
p.addEventListener('mouseover', mouseOver);
p.addEventListener('mouseout', mouseOut);

function mouseOver() {
  document.getElementById('target').src = 'img/picB.jpg';
}

function mouseOut() {
    document.getElementById('target').src = 'img/picA.jpg';
}