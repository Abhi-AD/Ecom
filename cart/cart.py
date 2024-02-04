from store.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        # Get the current session key if it exists
        cart = self.session.get("session_key")
        # If the user is new, no session key! Create one!
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {"price": str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True

    def total(self):
        product_ids = self.cart.keys()  # get ids from cart
        products = Product.objects.filter(
            id__in=product_ids
        )  # user ids to looks products in db model
        quantities = self.cart  # get quantities
        total = 0  # start counting at 0
        for key, value in quantities.items():
            key = int(key)  # convert key string
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # get id from cart
        product_ids = self.cart.keys()
        # user ids to lookup products in DB
        products = Product.objects.filter(id__in=product_ids)
        # return products
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        ourcart = self.cart
        ourcart[product_id] = product_qty
        self.session.modified = True
        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True