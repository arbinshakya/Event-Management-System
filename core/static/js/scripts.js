function calculateTotal() {
    const quantity = parseFloat(document.getElementById('quantity').value) || 0; // Get ticket quantity
    const eventPrice = parseFloat(document.getElementById('event-price').getAttribute('data-price')) || 0; // Read price from data attribute

    const totalPrice = eventPrice * quantity; // Calculate total
    document.getElementById('total-price').innerText = totalPrice.toFixed(2); // Update total price with 2 decimal places
}
