#!/usr/bin/env python3

import unittest
from Python.caesar import decrypt

#Unit Tests for caesar.py
class CaesarTest(unittest.TestCase):

    def test_decrypt(self):
        self.assertEqual('I am a good boy', decrypt('N fr f ltti gtd'))

if __name__ == '__main__':
    unittest.main()