document.addEventListener('DOMContentLoaded', function() {
    const dropdowns = document.querySelectorAll('.navbar-nav .nav-item.dropdown');
    
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('shown.bs.dropdown', function () {
            document.body.classList.add('menu-open');
        });
        dropdown.addEventListener('hidden.bs.dropdown', function () {
            document.body.classList.remove('menu-open');
        });
    });
});
