
class Cart:
    def __init__(self, request):
        self.session = request.session
        self.session["products"] = self.session.get("products", {})

    def __len__(self):
        return len(self.session["products"])

    @property
    def products(self):
        return self.session["products"] 


    def add_product(self, product, quantity):
        self.session["products"][product] = quantity + self.session["products"].get(product, 0)
        self.save()

    def clear_cart(self):
        print("Should empty cart")
        del self.session["products"] 
        self.session["products"] = {}
        self.save()

    def save(self):
        self.session.modified = True 