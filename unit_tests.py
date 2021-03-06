__author__ = 'Adriel'


__author__ = 'Adriel'

import unittest
from reader import read_input

class TestSequenceFunctions(unittest.TestCase):

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def test_read_input(self):
        cDict, jDict = read_input('Unit_tests/sample_input.txt')
        self.assertEqual(cDict, {'C2': {'H': 7, 'E': 6, 'P': 4}, 'C1': {'H': 2, 'E': 1, 'P': 1}, 'C0': {'H': 7, 'E': 7, 'P': 10}})
        self.assertEqual(jDict, {'J8': {'H': 8, 'C': 'C1,C0,C2', 'E': 2, 'P': 8}, 'J9': {'H': 10, 'C': 'C1,C2,C0', 'E': 2, 'P': 10}, 'J4': {'H': 6, 'C': 'C0,C2,C1', 'E': 10, 'P': 6}, 'J5': {'H': 6, 'C': 'C0,C2,C1', 'E': 7, 'P': 6}, 'J6': {'H': 8, 'C': 'C2,C1,C0', 'E': 6, 'P': 8}, 'J7': {'H': 7, 'C': 'C2,C1,C0', 'E': 1, 'P': 7}, 'J0': {'H': 3, 'C': 'C2,C0,C1', 'E': 9, 'P': 3}, 'J1': {'H': 4, 'C': 'C0,C2,C1', 'E': 3, 'P': 4}, 'J2': {'H': 4, 'C': 'C0,C2,C1', 'E': 0, 'P': 4}, 'J3': {'H': 10, 'C': 'C2,C0,C1', 'E': 3, 'P': 10}, 'J10': {'H': 6, 'C': 'C0,C2,C1', 'E': 4, 'P': 6}, 'J11': {'H': 8, 'C': 'C0,C1,C2', 'E': 4, 'P': 8}})



def main():
    unittest.main()

if __name__ == '__main__':
    main()
