'''
Created on 16/11/2012

@author: Anubis
'''
import unittest
import ex_5test

class Test(unittest.TestCase):


    def test_ex_5test(self):
        ex_5test.do_plus(5, 5)
        

        self.assertEqual(10, ex_5test.do_plus(5,5), "The numbers are not the right ones, try again")
        self.assertEqual(1, ex_5test.do_plus(0, 1), "not right do it again")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()