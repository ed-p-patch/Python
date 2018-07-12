class a_bike(object):
    def __init__(self, price, mspeed, miles):
        self.price = price
        self.mspeed = mspeed
        self.miles = miles

    def display_info(self):
        print self.price, self.mspeed, self.miles
        # Because this is the last function we call, we do not need to return self (since we are not chaining it)
    def ride(self):
        print "Riding bike"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing..."
        self.miles -= 5
        return self
    
Pats_bike = a_bike(150.00, 20, 75)
Michelles_bike = a_bike(100.00, 15, 50)
Tsuns_bike = a_bike(200.00, 10, 25)

Pats_bike.ride().ride().ride().reverse().display_info()
Michelles_bike.ride().ride().reverse().reverse().display_info()
Tsuns_bike.reverse().reverse().reverse().display_info()