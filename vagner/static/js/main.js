$(document).ready(function(){
  $('.slider-for').on('afterChange', function(event, slick, currentSlide){
    $('.slider-nav img').removeClass('active-thumbnail');
    $('.slider-nav img[data-slick-index="' + currentSlide + '"]').addClass('active-thumbnail');
  });

  $('.slider-for').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    mobileFirst: true,
    useCSS: true,
    asNavFor: '.slider-nav',
  });

  $('.slider-nav').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    asNavFor: '.slider-for',
    centerMode: true,
    mobileFirst: true,
    focusOnSelect: true,
    centerPadding: '0',
    nextArrow: "<img src='/static/img/right.svg' class='arrows_next' alt='1'>",
    prevArrow: "<img src='/static/img/left.svg' class='arrows_prev' alt='2'>",
  });
});


const images = document.querySelectorAll('.img_container img');
let currentIndex = 0;

// Функция для открытия изображения
const openImage = (index) => {
  document.querySelector('.popup-image').style.display = 'block';
  document.querySelector('.popup-image img').src = images[index].getAttribute('src');
  currentIndex = index;
};

// Функция для закрытия изображения
const closeImage = () => {
  document.querySelector('.popup-image').style.display = 'none';
};

// Обработчик клика по изображению
images.forEach((image, index) => {
  image.onclick = () => {
    openImage(index);
  };
});

// Обработчик клика по крестику
document.querySelector('.popup-image span').onclick = () => {
  closeImage();
};

// Обработчик стрелок влево и вправо
document.addEventListener('keydown', (event) => {
  if (document.querySelector('.popup-image').style.display === 'block') {
    if (event.key === 'ArrowLeft') {
      currentIndex = (currentIndex - 1 + images.length) % images.length;
      openImage(currentIndex);
    } else if (event.key === 'ArrowRight') {
      currentIndex = (currentIndex + 1) % images.length;
      openImage(currentIndex);
    }
  }
});
