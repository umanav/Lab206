class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = float(price)
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status =  "for sale"

    def Sell(self):
        self.status = "sold"
        return self

    def add_Tax(self, tax):
        sum_tax=self.price*tax
        self.price = self.price + sum_tax
        return self.price

    def Return(self, reason_return):
        if reason_return == "defective":
            self.status = "defective"
            self.price = 0
        elif reason_return == "closed box":
            self.status = "for sale"
        elif reason_return == "opened box":
            self.status = "used"
            discount = self.price * 0.20
            self.price = self.price - discount

    def display_Info(self):
        print "price: ", int(self.price)
        print "item_name: ", self.item_name
        print "weight: ", self.weight
        print "brand: ", self.brand
        print "status: ", self.status


test1 = Product(300, "PS4", "500 grams", "playstation")
test1.display_Info()
test1.Sell()
test1.add_Tax(0.15)
test1.Return("opened box")
test1.display_Info()