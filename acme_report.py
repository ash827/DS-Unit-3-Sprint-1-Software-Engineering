python
#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
name = random.sample(ADJECTIVES), + " ",+  random.sample(NOUNS)
price = random.randint(4,101)
weight = random.randint(4,101)
flammability = random.random(0.0,2.5)

def generate_products(num_products=30):
    products = []
    #I am completely stuck here, how do I add random products? Just making up names?
        return products


def inventory_report(products):
    pass  # TODO - your code! Loop over the products to calculate the report.


if __name__ == '__main__':
    inventory_report(generate_products())
