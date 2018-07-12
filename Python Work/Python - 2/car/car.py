class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    
    def display_all(self):
        print "Price: {} \nSpeed: {} \n Fuel: {} \n Mileage: {} \n Tax: {}".format(self.price, self.speed, self.fuel, self.mileage, self.tax) 

Pats_car = car(7500.00, 100, 75, 40000)
Michelles_car = car(21000.00, 120, 100, 15000)
Scots_car = car(1000.00, 75, 50, 75000)
Candaces_car = car(12000.00, 150, 25, 10000)
Matts_car = car(15000.00, 200, 250, 25000)
RacerXs_car = car(10001.00,150, 152, 89000)