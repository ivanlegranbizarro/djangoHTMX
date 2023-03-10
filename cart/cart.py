from django.conf import settings

from products.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]["product"] = Product.objects.get(pk=p)

        for item in self.cart.values():
            item["total_price"] = item["quantity"] * item["product"].price
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 1, "id": product_id}
        else:
            self.cart[product_id]["quantity"] += 1

            if self.cart[product_id]["quantity"] == 0:
                self.remove(product_id)

        self.save()

    def subs(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if self.cart[product_id]["quantity"] >= 1:
            self.cart[product_id]["quantity"] -= 1

            if self.cart[product_id]["quantity"] == 0:
                self.remove(product_id)

        self.save()

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]["product"] = Product.objects.get(pk=p)

        return sum(
            item["quantity"] * item["product"].price for item in self.cart.values()
        )
