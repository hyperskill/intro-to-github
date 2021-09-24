import unittest
import tokenizator
from tokenizator import Tokenizator
from collections import Generator
class TestMyCode(unittest.TestCase):
    # making a unit of Tokenizator class
    def setUp(self):
        self.x = Tokenizator()
    # the test itself
    def test_isgenerator(self):
        result= self.x.tokens_generator(' Ф 12 !!! @ # Alina is a student)))')
        self.assertIsInstance(result, Generator)
    def test_begins_with_no_alpha(self):
        result=list(self.x.tokens_generator(' ф 12 !!! @ # Alina is a student)))'))
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].s, 'ф')
        self.assertEqual(result[0].position, 1)
        self.assertEqual(result[1].s,'Alina')
        self.assertEqual(result[1].position,14)
    def test_begins_with_alpha(self):
        result=list(self.x.tokens_generator('ф 12 !!! @ # Alina is a student)))'))
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].s, 'ф')
        self.assertEqual(result[0].position, 0)
        self.assertEqual(result[1].s,'Alina')
        self.assertEqual(result[1].position,13)
    def test_ends_with_alpha(self):
        result=list(self.x.tokens_generator('ф 12 !!! @ # Alina is a student)))abc'))
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result[0].s, 'ф')
        self.assertEqual(result[0].position, 0)
        self.assertEqual(result[5].s,'abc')
        self.assertEqual(result[5].position,34)
    def test_ends_with_no_alpha(self):
        result=list(self.x.tokens_generator('ф 12 !!! @ # Alina is a student)))'))
        self.assertIsInstance(result,list)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].s, 'ф')
        self.assertEqual(result[0].position, 0)
        self.assertEqual(result[4].s,'student')
        self.assertEqual(result[4].position,24) 
    def  test_MyError_number(self):
        with self.assertRaises(ValueError):
            list(self.x.tokens_generator(12))
    def test_MyError_notList(self):
        s=[1, 2, 3, 'this is my string']
        with self.assertRaises(ValueError):
            list(self.x.tokens_generator(s))
            
    def test_Function_begins_with_no_alpha(self):
        result=self.x.tokenize(' ф 12 !!! @ # Alina is a student)))')
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].s, 'ф')
        self.assertEqual(result[0].position, 1)
        self.assertEqual(result[1].s,'Alina')
        self.assertEqual(result[1].position,14)
    def test_function_begins_with_alpha(self):
        result=self.x.tokenize('ф 12 !!! @ # Alina is a student)))')
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].s, 'ф')
        self.assertEqual(result[0].position, 0)
        self.assertEqual(result[1].s,'Alina')
        self.assertEqual(result[1].position,13)
    def test_function_ends_with_alpha(self):
        result=self.x.tokenize('ф 12 !!! @ # Alina is a student)))abc')
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result[0].s, 'ф')
        self.assertEqual(result[0].position, 0)
        self.assertEqual(result[5].s,'abc')
        self.assertEqual(result[5].position,34)
    def test_function_ends_with_no_alpha(self):
        result=self.x.tokenize('ф 12 !!! @ # Alina is a student)))')
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].s, 'ф')
        self.assertEqual(result[0].position, 0)
        self.assertEqual(result[4].s,'student')
        self.assertEqual(result[4].position,24)    
    def  test_MyError_function_number(self):
        with self.assertRaises(ValueError):
            self.x.tokenize(12)
    def test_MyError_function_notList(self):
        s=[1, 2, 3, 'this is my string']
        with self.assertRaises(ValueError):
            self.x.tokenize(s)
   
    def test_isgenerator_for_token_gen(self):
        result = self.x.token_gen(' Ф 12 !!! @ # Alina is a student)))')
        self.assertIsInstance(result, Generator)
    def test_my_token_gen(self):
        result = list(self.x.token_gen(' Ф 12 !!! @ # Alina is a student)))'))
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 6)
        self.assertEqual(result[0].s, 'Ф')
        self.assertEqual(result[0].tp, 'alpha')
        self.assertEqual(result[0].position,1)
        self.assertEqual(result[1].s, '12')
        self.assertEqual(result[1].tp, 'digit')
        self.assertEqual(result[1].position,3)
        self.assertEqual(result[5].s,'student')
        self.assertEqual(result[5].tp, 'alpha')
        self.assertEqual(result[5].position,25)
    def  test_MyError_token_gen_number(self):
        with self.assertRaises(ValueError):
            list(self.x.token_gen(12))
    def test_MyError_token_gen_notList(self):
        s=[1, 2, 3, 'this is my string']
        with self.assertRaises(ValueError):
            list(self.x.token_gen(s))
    def test_empty_string(self):
        result = ''
        self.assertEqual(len(result), 0)
                                      
        
            
if __name__ == '__main__':
    unittest.main()# общий способ вынести модуль чтобы запустить как прогу без импорта 
   








