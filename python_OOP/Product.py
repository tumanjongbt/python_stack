# define class Product
class Product:

    # this method to run every time a new Product object is instantiated    
    def __init__(self, price, item_name, weight, brand):
	# instance attributes 
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    # create sell method
    def sell(self, change_status):
        print(f"Status is currently {self.status}")
        self.status = change_status
        print(f"Status is now: ", change_status)
        return self

    # create add_tax method
    def add_tax(self, tax):
        print(f"Product Price before tax is: {self.price}")
        self.price = int(self.price * tax)
        print(f"tax is {tax}. Product Price plus tax is: {self.price}")
        return self
    
    # create return_item method
    def return_item(self, reason_for_return):
        self.status = reason_for_return
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
            print(f"Return_status is {reason_for_return}. Product Status: {self.status}. Product Price: {self.price}")
        if reason_for_return == "like new":
            self.status = "for sale"
            print(f"Return_status is {reason_for_return}. Product Status: {self.status}")

        if reason_for_return == "opened":
            self.status = "used"
            self.price = int(self.price - (self.price * 0.20))
            print(f"Return_status is {reason_for_return}. Product Status: {self.status}. Product Price: {self.price}")
        return self

    # create display_info method
    def display_info(self):
        print(f"Price: {self.price}\n Item_name: {self.item_name}\n Weight: {self.weight}\n Brand: {self.brand}\n")
        return self 

#create instances of the Product class
product1 = Product(2000,"Sofa", "40lb", "Ashley")

print(product1.price)
# change product status using sell method
product1.sell("sold")

# change product status and price using return_item method
# product1.return_item("opened")
# product1.return_item("defective")
product1.return_item("like new")

# Add tax to product price using add_tax method
product1.add_tax(1.06)

# display information about each Product
product1.display_info()


