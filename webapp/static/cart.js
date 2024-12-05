const currentRoute = window.location.pathname

// Cart CRUD

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

// Header component

function updateCartIcon() {
    let cart = getCart();
    let itemCount = cart.reduce((total, item) => total + item.quantity, 0);
    const icon = document.getElementById('carrito-contador');
    icon.textContent = itemCount;

    const bubbleIcon = document.getElementById('cart-bubble');
    bubbleIcon.classList.add('bounce');
    bubbleIcon.addEventListener('animationend', () => {
        bubbleIcon.classList.remove('bounce');
    }, { once: true });
}

updateCartIcon();

// Product detail

if (document.getElementById('product-container')) {
    document.getElementById('product-container').addEventListener('click', function (e) {
        if (e.target && e.target.classList.contains('add-to-cart')) {
            const productElement = e.target.closest('.product');
            const productId = productElement.dataset.id;

            addToCart(productId);
        }
    });
}

// Producto detalle

if (currentRoute.includes('/producto')) {
    let quantityProduct = 0;

    function updateQuantityHTML() {
        document.getElementById('quantity').innerText = quantityProduct.toString();
    }

    document.getElementById('minus-btn').addEventListener('click', () => {
        quantityProduct = Math.max(0, quantityProduct - 1);
        updateQuantityHTML();
    })

    document.getElementById('plus-btn').addEventListener('click', () => {
        quantityProduct += 1;
        updateQuantityHTML()
    })

    updateQuantityHTML()

    document.getElementById('add-to-cart').addEventListener('click', () => {
        if (quantityProduct > 0) {
            const productId = document.getElementById('add-to-cart').getAttribute('data-id');
            addToCart(productId, quantityProduct);
        }
    })
}

if (document.getElementById('clear-cart')) {
    document.getElementById('clear-cart').addEventListener('click', () => {
        clearCart()
        window.location.reload()
    })
}

console.log(currentRoute)
if (currentRoute.includes('/success')) {
    clearCart()
}












// Debugging

function showCart() {
    const cart = getCart();

    if (cart.length === 0) {
        console.log("El carrito está vacío.");
        return;
    }

    console.log("Contenido del carrito:");
    cart.forEach(item => {
        console.log(`Producto ID: ${item.id}, Cantidad: ${item.quantity}, tipo ID: ${typeof (item.id)}, tipo Cantidad: ${typeof (item.quantity)}`);
    });

    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    console.log(`Total de ítems en el carrito: ${totalItems}`);
}

showCart()