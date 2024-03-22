document.addEventListener("DOMContentLoaded", function() {

    var container = document.getElementById('container');
    var slider = document.getElementById('slider');
    var slides = document.getElementsByClassName('slide').length;
    var leftButton = document.getElementById("leftButton");
    var rightButton = document.getElementById("rightButton");

    var currentPosition = 0;
    var currentMargin = 0;
    var slidesPerPage = 0;
    var slidesCount = slides - 1; // Reduzir o número de slides para compensar o índice baseado em zero
    var containerWidth = container.offsetWidth;

    window.addEventListener("resize", checkWidth);

    function checkWidth() {
        containerWidth = container.offsetWidth;
        setParams(containerWidth);
    }

    function setParams(w) {
        if (w < 551) {
            slidesPerPage = 1;
        } else if (w < 901) {
            slidesPerPage = 2;
        } else if (w < 1101) {
            slidesPerPage = 3;
        } else {
            slidesPerPage = 4;
        }
        
        slidesCount = Math.ceil(slides / slidesPerPage) - 1;
        currentPosition = Math.min(currentPosition, slidesCount);
        currentMargin = -currentPosition * (100 / slidesPerPage) + '%'; // Adicionando % para garantir que a margem seja configurada corretamente
        slider.style.marginLeft = currentMargin;
        updateNavButtons();
    }

    setParams();

    function slideRight() {
        if (currentPosition < slidesCount) {
            currentPosition++;
            currentMargin = -currentPosition * (100 / slidesPerPage) + '%';
            slider.style.marginLeft = currentMargin;
        }
        updateNavButtons();
    }

    function slideLeft() {
        if (currentPosition > 0) {
            currentPosition--;
            currentMargin = -currentPosition * (100 / slidesPerPage) + '%';
            slider.style.marginLeft = currentMargin;
        }
        updateNavButtons();
    }

    function updateNavButtons() {
        if (currentPosition === 0) {
            leftButton.classList.add('inactive');
        } else {
            leftButton.classList.remove('inactive');
        }
        
        if (currentPosition >= slidesCount) {
            rightButton.classList.add('inactive');
        } else {
            rightButton.classList.remove('inactive');
        }
    }

    rightButton.addEventListener("click", slideRight);
    leftButton.addEventListener("click", slideLeft);

});
