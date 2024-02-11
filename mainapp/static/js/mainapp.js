// User modal
const userIcon = document.querySelector(".user"),
  userModal = document.querySelector(".modal_user");

userIcon.addEventListener("click", () => {
  userModal.style.display =
    userModal.style.display == "none" ? "block" : "none";
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
