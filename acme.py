import numpy as np
import random
class Product(object):


    def __init__(self,name,price = 10,weight = 20,flammability = 0.5,identifier = random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        if self.price / self.weight < 0.5:
            return "Not so stealable..."
        elif self.price / self.weight > 0.5 and self.price < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        if self.flammability * self.weight < 10:
            return "...fizzle."
        elif self.flammability * self.weight >= 10 and self.flammability < 50:
            return "...boom!"
        else:
            return "...BABOOM!"



class BoxingGlove(Product):


    def __init__(self,name):
        self.name = name
        self.price = 10
        self.weight = 10
        self.flammability = 0.5
        self.identifier = random.randint(1000000, 9999999)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles"
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else: 
            return "OUCH!"