class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Current Health: {}".format(self.health)
        return self

goat = animal('Goat', 50)
goat.walk().walk().walk().run().run().display_health()

class dog(animal):
    def set_health(self):
        self.health = 150
        return self

    def pet(self):
        self.health += 5
        return self

pupper = dog('Lil Pupper', 50).set_health()
pupper.walk().walk().walk().run().run().pet().display_health()

class dragon(animal):
    def set_health(self):
        self.health = 170
        return self
    
    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print "I am a dragon"

Drago = dragon('Drago', 200).set_health()
Drago.fly().fly().display_health()