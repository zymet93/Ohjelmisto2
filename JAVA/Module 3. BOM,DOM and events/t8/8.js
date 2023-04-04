function options() {
    let a = parseInt(document.querySelector('#num1').value);
    let b = parseInt(document.querySelector('#num2').value);


    if (select.value === 'add'){
        p.innerHTML = a + b;
    }
    if (select.value ==='sub'){
        p.innerHTML = a - b;
    }
    if (select.value === 'multi'){
        p.innerHTML = a * b;
    }
    if (select.value === 'div'){
        p.innerHTML = a / b;
    }
}
const button = document.querySelector('button');
const p = document.querySelector('#result');
const select = document.querySelector("#operation");
button.addEventListener('click', options);