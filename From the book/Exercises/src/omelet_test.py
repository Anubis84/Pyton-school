'''
Created on 20/11/2012

@author: Anubis
'''
import unittest
import Execises_chp5

class Test(unittest.TestCase):


    def testomelet(self):
        Execises_chp5.make_omelet("cheese")
        Execises_chp5.make_omelet("western")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()