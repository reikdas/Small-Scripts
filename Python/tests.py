#!/usr/bin/env python3

import unittest
from Python.caesar import decrypt
from Python.caesar import encrypt

# Unit Tests for caesar.py
class CaesarTest(unittest.TestCase):

    def test_decrypt(self):
        self.assertEqual('I am a good boy', decrypt('N fr f ltti gtd'))

    def test_encrypt(self):
        self.assertEqual('L dp d jrrg erb', encrypt('I am a good boy', 3))


if __name__ == '__main__':
    unittest.main()