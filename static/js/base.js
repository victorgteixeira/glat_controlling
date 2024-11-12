document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const menuContainer = document.getElementById('menuContainer');

    menuToggle.addEventListener('click', function() {
        menuContainer.classList.toggle('expanded');
    });
});
