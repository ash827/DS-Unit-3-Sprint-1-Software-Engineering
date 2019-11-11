#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    def test_default_product_price(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_steal_and_explode(self):

        
if __name__ == '__main__':
    unittest.main()
