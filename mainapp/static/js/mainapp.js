const userIcon = document.querySelector('.account'),
      userModal = document.querySelector('.modal_user');


userIcon.addEventListener('click', () => {
    userModal.style.display = (userModal.style.display == 'none') ? 'block' : 'none'
});
