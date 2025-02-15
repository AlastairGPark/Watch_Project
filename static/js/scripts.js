function togglemenu() {
    const sidemenu = document.getElementById('sidemenu');
    sidemenu.classList.toggle("open");
}

document.addEventListener("DOMContentLoaded", function() {
    const brandToggle = document.querySelector(".brand-toggle");
    const submenu = document.querySelector(".Brandsubmenu");
    const sidemenu = document.querySelector(".side-menu");
    const hamburger = document.querySelector(".hamburger");

    brandToggle.addEventListener("click", function(event) {
        event.preventDefault();
        submenu.classList.toggle("active");
        event.stopPropagation();
    });

    window.togglemenu = function() {
        sidemenu.classList.toggle("open");
    };

document.addEventListener("click", function(event) {

    if (!submenu.contains(event.target) && !brandToggle.contains(event.target)) {
        submenu.classList.remove("active");
    }

    if (!sidemenu.contains(event.target) && !hamburger.contains(event.target)) {
        sidemenu.classList.remove("open");
    }
});

});