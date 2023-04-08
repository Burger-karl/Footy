let navbar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = () => {
    navbar.classList.toggle('active');
    searchForm.classList.remove('active');
    cartItem.classList.remove('active');
}


let searchForm = document.querySelector('.search-form');

document.querySelector('#search-btn').onclick = () => {
    searchForm.classList.toggle('active');
    navbar.classList.remove('active');
    cartItem.classList.remove('active');
}


let cartItem = document.querySelector('.cart-items-container');

document.querySelector('#cart-btn').onclick = () => {
    cartItem.classList.toggle('active');
    navbar.classList.remove('active');
    searchForm.classList.remove('active');
}

window.onscroll = () => {
    navbar.classList.remove('active');
    searchForm.classList.remove('active');
    cartItem.classList.remove('active');
}


const modalBtn = document.getElementById('modal-btn');
const modalBtn1 = document.getElementById('modal-btn1');
const modalBtn2 = document.getElementById('modal-btn2');
const modalContainer = document.getElementById('modal-container');

modalBtn.addEventListener('click', function() {
    modalContainer.style.display = 'block';
});

modalBtn1.addEventListener('click', function() {
    modalContainer.style.display = 'block';
});

modalBtn2.addEventListener('click', function() {
    modalContainer.style.display = 'block';
});


window.addEventListener('click', function(event) {
    if (event.target == modalContainer) {
        modalContainer.style.display = 'none';
    }
});

window.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        modalContainer.style.display = 'none';
    }
});