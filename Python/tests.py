#!/usr/bin/env python3

import unittest

# Imports for caesar.py tests
from caesar import decrypt
from caesar import encrypt


# Unit Tests for caesar.py
class CaesarTest(unittest.TestCase):

    def test_decrypt_key(self):
        self.assertEqual('I am a good boy', encrypt('L dp d jrrg erb',-3))

    def test_encrypt(self):
        self.assertEqual('L dp d jrrg erb', encrypt('I am a good boy', 3))

    def test_decrypt_big(self):
        self.assertEqual('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', decrypt('QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'))


if __name__ == '__main__':
    unittest.main()
