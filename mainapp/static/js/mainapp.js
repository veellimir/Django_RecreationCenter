const userIcon = document.querySelector('.wrapper-burger'),
      userModal = document.querySelector('header');


userIcon.addEventListener('click', () => {
    userModal.style.display = (userModal.style.display == 'none') ? 'block' : 'none'
});


document.addEventListener('click', event => {
    const targetElement = event.target;

    if (!userModal.contains(targetElement) && !userIcon.contains(targetElement)) {
        userModal.style.display = 'none';
    }
});

