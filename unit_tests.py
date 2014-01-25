__author__ = 'Adriel'


__author__ = 'Adriel'

import unittest


class TestSequenceFunctions(unittest.TestCase):

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def test(self):
        self.assertEqual()

    def test_1(self):
        self.assertTrue()
        self.assertFalse()



def main():
    unittest.main()

if __name__ == '__main__':
    main()
