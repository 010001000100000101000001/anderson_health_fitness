document.addEventListener('DOMContentLoaded', function() {
    const dropdowns = document.querySelectorAll('.navbar-nav .nav-item.dropdown');
    
    // Adjust hero text when dropdown menu opens
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('shown.bs.dropdown', function () {
            document.body.classList.add('menu-open');
        });
        dropdown.addEventListener('hidden.bs.dropdown', function () {
            document.body.classList.remove('menu-open');
        });
    });

     // Adjust hero text when hamburger menu opens
     navbarToggler.addEventListener('click', function() {
        if (navbarToggler.getAttribute('aria-expanded') === 'true') {
            document.body.classList.add('menu-open');
        } else {
            document.body.classList.remove('menu-open');
        }
    });
});
