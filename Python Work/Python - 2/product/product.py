Attributes:
• Price
• Item Name
• Weight
• Brand
• Status: default "for sale"
Methods:
• Sell: changes status to "sold"
• Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
• Return: takes reason for return as a parameter and changes status accordingly. If the item is being
 returned because it is defective, change status to "defective" and change price to 0. If it is being returned
  in the box, like new, mark it "for sale".
If the box has been, opened, set the status to "used" and apply a 20% discount.
• Display Info: show all product details.
Every method that doesn't have to return something should return self so methods can be chained.

class product(object):
    def __init__(self, price, name, weight, brand, status):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        if(status == ''):
            self.status = "for sale"
        else:
            self.status = status
    
    def Sell():
        self.status = "sold"
        return self
    def Add_Tax(num):
        self.price = (self.price * num)
        return self
    def Return(reason):
        if reason == 'defective':
            self.status = "Returned: {}".format(reason)
            self.price = 0
        elif reason == 'opened':
            self.status = 'used'
            self.price = self.price * 0.20
        return self
    def Display_Info():
        print "Name: {}\n Price: {}\n Weight: {}\n Brand: {}\n Status: {}\n".format(self.name, self.price, self.weight, self.brand, self.status)
        return self