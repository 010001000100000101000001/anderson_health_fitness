// Update the cart total in both the desktop and mobile header
function updateCartIcon(grandTotal) {
    const desktopCartTotal = document.querySelector('.cart-total.desktop');
    const mobileCartTotal = document.querySelector('.cart-total.mobile');

    // Check if the elements exist before updating their content
    if (desktopCartTotal) {
        desktopCartTotal.innerText = `(${grandTotal.toFixed(2)})`;
    }

    if (mobileCartTotal) {
        mobileCartTotal.innerText = `(${grandTotal.toFixed(2)})`;
    }
}

// Add item to the cart with AJAX and update cart totals
function addToCart(itemId, quantity = 1) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const url = `/cart/add/${itemId}/`;

    // Prepare the data for the AJAX request
    const data = {
        'csrfmiddlewaretoken': csrfToken,
        'quantity': quantity
    };

    // Make the AJAX POST request
    $.post(url, data)
    .done(function(response) {
        // Display success message to user
        alert("Item added to your cart! Time to push your limits and achieve new fitness milestones.");
        
        // Update the cart total in the header
        updateCartIcon(response.grand_total);
    })
    .fail(function() {
        // Handle errors with a helpful message
        alert("Oops! Something went wrong. Please give it another try soon.");
    });
}
