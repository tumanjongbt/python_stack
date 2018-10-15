# define class Bike
class Bike:
    # this method to run every time a new Bike object is instantiated
    def __init__(self, price, max_speed):
	# instance attributes 
        self.price = price
        self.max_speed = max_speed
        self.miles = 0 # set initial miles to 0 whenever a new instance is created

    # display price, maximum speed and total miles for a single instance
    def displayInfo(self, miles):
        self.miles += miles
        print(f"Purchase price is: {self.price}. Maximum speed is {self.max_speed}.  Total miles is {self.miles}.")
        return self
    # Riding method of the calling instance
    def ride(self, miles):
        self.miles += miles
        print(f"Riding: ", miles, "miles")
        return self

    # Reverse method of the calling instance
    def reverse(self, miles):
        self.miles -= miles
        print(f"Reversing: ", miles, "miles")
        return self
        
#create an instance of the Bike class
bike1 = Bike(200,"25mph")
bike2 = Bike(300,"30mph")
bike3 = Bike(400,"40mph")
bike1.ride(3).reverse(1).displayInfo(10)
bike2.ride(2).reverse(2).displayInfo(5)
bike3.reverse(3).displayInfo(4)

