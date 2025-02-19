document.addEventListener("DOMContentLoaded", function() {
    const filterItems = document.querySelectorAll(".filter-submenu li");
    const watchItems = document.querySelectorAll(".watch-item"); // Placeholder for watch items

    // Filtering functionality
    filterItems.forEach(item => {
        const filterText = item.querySelector(".filter-text"); // The text part to trigger the filter

        filterText.addEventListener("click", function () {
            // Remove active class from all filters
            filterItems.forEach(i => i.classList.remove("active"));
            item.classList.add("active");

            const filter = item.getAttribute("data-filter");

            // Show/hide watches based on filter (assuming watches have a matching class)
            watchItems.forEach(watch => {
                if (filter === "allmodels" || watch.classList.contains(filter)) {
                    watch.style.display = "block";
                } else {
                    watch.style.display = "none";
                }
            });
        });
    });
});
