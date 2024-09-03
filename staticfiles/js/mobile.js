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
    const navbarToggler = document.querySelector('.navbar-toggler');
    
    if (navbarToggler) {
        navbarToggler.addEventListener('click', function() {
            if (navbarToggler.getAttribute('aria-expanded') === 'true') {
                document.body.classList.add('menu-open');
            } else {
                document.body.classList.remove('menu-open');
            }
        });
    }

  // Search bar toggle handling
  const searchToggleBtn = document.getElementById('searchToggleBtn');
  const searchForm = document.getElementById('mobileSearchForm');
  const searchIcon = document.getElementById('searchIcon');

  if (searchToggleBtn && searchForm) {
      searchToggleBtn.addEventListener('click', function(event) {
          event.preventDefault(); // Prevent the form from submitting
          if (searchForm.classList.contains('d-none')) {
              searchForm.classList.remove('d-none');
              searchIcon.classList.replace('fa-magnifying-glass-plus', 'fa-magnifying-glass-minus');
          } else {
              searchForm.classList.add('d-none');
              searchIcon.classList.replace('fa-magnifying-glass-minus', 'fa-magnifying-glass-plus');
          }
      });
  }
});