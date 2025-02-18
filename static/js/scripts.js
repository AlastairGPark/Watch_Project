document.addEventListener("DOMContentLoaded", function() {
    const sidemenu = document.querySelector(".side-menu");
    const hamburger = document.querySelector(".hamburger");

    // Toggle menu when hamburger button is clicked
    hamburger.addEventListener("click", function() {
        sidemenu.classList.toggle("open");
    });

    // Close the side menu when clicking outside
    document.addEventListener("click", function(event) {
        if (!sidemenu.contains(event.target) && !hamburger.contains(event.target)) {
            sidemenu.classList.remove("open");
        }
    });

    // Close the submenu if clicking outside of the submenu
    document.addEventListener("click", function(event) {
        const activeSubmenu = document.querySelector(".menu-item.active");
        if (activeSubmenu && !activeSubmenu.contains(event.target)) {
            activeSubmenu.classList.remove("active");
        }
    });

    // Toggle submenus on click, ensuring only one submenu is visible at a time
    const menuItems = document.querySelectorAll(".menu-item");

    menuItems.forEach(function(item) {
        item.addEventListener("click", function(event) {
            event.stopPropagation(); // Prevent closing the menu when clicking the item

            // Close all other submenus
            menuItems.forEach(function(otherItem) {
                if (otherItem !== item) {
                    otherItem.classList.remove("active");
                }
            });

            // Toggle submenu visibility for the clicked item
            item.classList.toggle("active");
        });
    });

    // Header fade effect on scroll
    let lastScrollTop = 0; // Variable to track the last scroll position
    const header = document.querySelector("header"); // Select the header

    window.addEventListener("scroll", function() {
        let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

        if (currentScroll > lastScrollTop) {
            // Scrolling down
            header.classList.add("hidden");
        } else {
            // Scrolling up
            header.classList.remove("hidden");
        }

        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // Prevent negative scroll values
    });
});
