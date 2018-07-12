class store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    
    def add_product(self, item):
        self.products.append(item)
        return self
    def remove_product(self, item):
        if item not in self.products:
            print "That item does not exist"
        else:
            self.products.remove(item)
        return self
    def inventory(self):
        in_string = "Current Inventory \n"
        for x in range(0, len(self.products)):
            in_string += "Item: {}".format(self.products[x])
        print in_string

Geek_products = ['Board Games', 'Trading Cards', 'Dice', 'Tabletop Supplies', 'Playmats']

Pats_store = store(Geek_products, 'Metairie', 'Patrick')
Pats_store.inventory()
Pats_store.remove_product('Playmats')
Pats_store.inventory()
Pats_store.add_product('Miniatures')
Pats_store.inventory()