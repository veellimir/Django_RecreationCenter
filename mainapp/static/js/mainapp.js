// User modal
const userIcon = document.querySelector(".user"),
      userModal = document.querySelector(".modal_user");

userIcon.addEventListener("click", () => {
  userModal.style.display = userModal.style.display == "none" ? "block" : "none";
});

document.addEventListener("click", (event) => {
  const targetElement = event.target;

  if (!userModal.contains(targetElement) && !userIcon.contains(targetElement)) {
    userModal.style.display = "none";
  }
});

// Scroll header
let header = document.querySelector("header"),
    headerH = document.querySelector("header").clientHeight,
    social = document.querySelector(".social");

document.onscroll = function () {
  let scroll = window.scrollY;

  if (scroll > headerH) {
    header.classList.add("active_header");
  } else {
    header.classList.remove("active_header");
  }
};

// Hover input auth
const inputAuth = document.querySelectorAll(".input_auth"),
  btnSubmit = document.querySelector(".btn_submit");

inputAuth.forEach((el) => {
  el.addEventListener("input", () => {
    if (el.value.trim() !== "") {
      el.style.border = "1px solid var(--blue)";
    } else {
      el.style.border = "1px solid var(--input_warning)";
    }
    el.style.transitionDuration = "0.1s";
  });
});

// Swiper
const swiper = new Swiper(".swiper", {
  direction: "horizontal",
  loop: true,
  pagination: {
    el: ".swiper-pagination",
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  scrollbar: {
    el: ".swiper-scrollbar",
  },
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
});


// Messages
const msgShow = document.querySelector('.wrapper--alert-alert'),
      msgPositive = document.querySelector('.alert-info'),
      msgWelcome = document.querySelector('.alert-success');

  if (msgShow) {
    msgShow.style.position = 'fixed'
    msgShow.style.top = 100 + 'px'
    msgShow.style.opacity = 1;

    if (msgPositive || msgPositive) {
      setTimeout(() => {
        msgPositive.style.display = 'none';
      }, 4000);
    }
  }    


// linking the search and pagination
let searchForm = document.getElementById('search'),
    pageLink = document.querySelectorAll('.page_link');

if (searchForm) {
  for (let i=0; pageLink.length > i; i++) {
    pageLink[i].addEventListener('click', function (event) {
      event.preventDefault();

      let page = this.dataset.page;
      searchForm.innerHTML += `<input value=${page} name="page" type="hidden">`;

      searchForm.submit();
    })
  }
}    

// Header mobile
const menuMobile = document.querySelector('.wrapper-burger'),
      headerMobile = document.querySelector('header'),
      backroundMenu = document.querySelector('.backround-modile-menu'),
      exitBtn = document.querySelector('.exit_modal');


      menuMobile.addEventListener('click', () => {
        headerMobile.style.display = 'block';
        backroundMenu.style.display = 'block';
      })
      function hideHeaderAndBackground() {
        headerMobile.style.display = 'none';
        backroundMenu.style.display = 'none';
    }
    
    backroundMenu.addEventListener('click', hideHeaderAndBackground);
    exitBtn.addEventListener('click', hideHeaderAndBackground);
    