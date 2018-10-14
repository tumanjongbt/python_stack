# define class Car
class Car:

    # this method to run every time a new Car object is instantiated    
    def __init__(self, price, speed, fuel, mileage):
	# instance attributes 
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

	# instance method 
    # display price, speed, fuel, mileage and tax a single instance
    def display_all(self):
        print(f"Price: {self.price}\n Speed: {self.speed}\n Fuel: {self.fuel}\n Mileage: {self.mileage}\n Tax: {self.tax} \n")
        return self
        
#create instances of the Car class
car1 = Car(2000,"25mph", "Full", "15mpg")
car2 = Car(2000,"5mph", "Not Full", "105mpg")
car3 = Car(2000,"15mph", "Kind of Full", "95mpg")
car4 = Car(2000,"25mph", "Full", "25mpg")
car5 = Car(2000,"45mph", "Empty", "25mpg")
car6 = Car(20000000,"35mph", "Empty", "15mpg")

# display information about each car once teh attributes have been defined
car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
