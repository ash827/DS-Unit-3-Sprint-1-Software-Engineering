#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):

    def test_default_product_price(self):
        
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_stealability(self):
    
        prod = Product('Test Product', price=10, weight=20)
        self.assertEqual(prod.stealability(), 'Very stealable!')


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        
        test_prod = generate_products()
        self.assertEqual(len(test_prod), 30)

    def test_legal_names(self):
        
        test_prod = generate_products()
        for i in test_prod:
            adj, noun = i.name.split()
            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)

    def test_legal_flammability(self):
    
        test_prod = generate_products()
        counts = 0
        for i in test_prod:
            if i.flammability < 0 or i.flammability > 2.5:
                counts += 1
            else:
                pass

        self.assertEqual(counts, 0)


if __name__ == '__main__':
    unittest.main()