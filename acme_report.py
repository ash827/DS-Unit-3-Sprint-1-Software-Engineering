#!/usr/bin/env python
import random
from random import randint, sample, uniform
from acme import Product



ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
products = []

def generate_products(num=30):
  
  for i in range(num):
    adjective = random.choice(ADJECTIVES)
    noun = random.choice(NOUNS)
    name = adjective + ' ' + noun
    price = random.randint(5,100)
    weight = random.randint(5,100)
    flammability = random.uniform(0.0, 2.5)
    
    prod = Product(name, price, weight, flammability)
    products.append(prod)
  return products

def inventory_report(products):
  mean_price = sum([Product.price for Product in products]) / len(products)
  mean_weight = sum([Product.weight for Product in products]) / len(products)
  mean_flammability = sum([Product.flammability for Product in products]) / len(products)
  return mean_price, mean_weight, mean_flammability
 

products = generate_products() 

unique_names = []
for i in products:
  if i.name not in unique_names:
    unique_names.append(i.name)   
 
num_unique_names = len(unique_names)
mean_price, mean_weight, mean_flammability = inventory_report(products)


print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
print("Unique Product Names: ", num_unique_names)
print("Average Price: ", mean_price)
print("Average Weight: ", mean_weight)
print("Average Flammability: ", mean_flammability)
