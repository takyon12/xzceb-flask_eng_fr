import unittest

import sys
import os
  
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
  
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
  
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)

import translator as t

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(t.frenchToEnglish('Bonjour'), 'Hello') 
        self.assertRaises(ValueError, t.frenchToEnglish, None)

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(t.englishToFrench('Hello'), 'Bonjour') 
        self.assertRaises(ValueError, t.englishToFrench, None)

unittest.main()
