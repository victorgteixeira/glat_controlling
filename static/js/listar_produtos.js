document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle-filter");
    const filterSection = document.getElementById("filter-section");

    if (toggleButton) {
        toggleButton.addEventListener("click", function () {
            if (filterSection.style.display === "none" || filterSection.style.display === "") {
                filterSection.style.display = "block";
            } else {
                filterSection.style.display = "none";
            }
        });
    }

    const resetButton = document.getElementById("reset-filters");
    if (resetButton) {
        resetButton.addEventListener("click", function () {
            const inputs = document.querySelectorAll("#filter-section input, #filter-section select");
            inputs.forEach((input) => (input.value = ""));
        });
    }
});
