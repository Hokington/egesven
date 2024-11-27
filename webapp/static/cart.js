function getCart() {
    const cart = document.cookie
        .split('; ')
        .find(row => row.startsWith('cart='));
    return cart ? JSON.parse(cart.split('=')[1]) : [];
}

function setCart(cart) {
    document.cookie = `cart=${JSON.stringify(cart)}; path=/; max-age=36000; SameSite=None; Secure`;
    updateCartIcon();
}

function addToCart(productId, quantity = 1) {
    let cart = getCart();
    const existingProduct = cart.find(item => item.id === productId);

    if (existingProduct) {
        existingProduct.quantity += quantity;
    } else {
        cart.push({ id: productId, quantity: quantity });
    }

    setCart(cart);
}

function clearCart() {
    setCart([]);
}

function updateCartIcon() {
    let cart = getCart();
    let itemCount = cart.reduce((total, item) => total + item.quantity, 0);
    const icon = document.getElementById('carrito-contador');
    icon.textContent = itemCount;
}

updateCartIcon();

document.getElementById('product-container').addEventListener('click', function (e) {
    if (e.target && e.target.classList.contains('add-to-cart')) {
        const productElement = e.target.closest('.product');
        const productId = productElement.dataset.id;

        addToCart(productId);
    }
});





function showCart() {
    const cart = getCart();

    if (cart.length === 0) {
        console.log("El carrito está vacío.");
        return;
    }

    console.log("Contenido del carrito:");
    cart.forEach(item => {
        console.log(`Producto ID: ${item.id}, Cantidad: ${item.quantity}`);
    });

    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    console.log(`Total de ítems en el carrito: ${totalItems}`);
}

showCart()