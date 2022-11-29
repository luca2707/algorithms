# Exemple 9 : Tassement
# Poussez tous les “.” d’un tableau donné à la fin du tableau.
# Par exemple : “a,b,.,c,.,.,k” devient “a,b,c,k,.,.,.”

import unittest

def tasser(input_list: list, pebble = '.') -> list:
    result_list = list()
    i = 0
    for element in input_list:
        if element == pebble:
            # the current element is a pebble => insert it at the end of the new list
            result_list.append(element)
        else:
            result_list.insert(i, element)
            i += 1
    return result_list

class TestTasser(unittest.TestCase):

    def test_tasser_1(self):
        input = ('a','b','.','c','.','.','k')
        expected = ['a','b','c','k','.','.','.']
        self.assertEqual(tasser(input), expected)

    def test_tasser_2(self):
        input = ('.','a','b','.','c','.','.','d','e','f','.','g','.','.','.','h','i','j','.','.','.','k','.','.','.','.')
        expected = ['a','b','c','d','e','f','g','h','i','j','k','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
        self.assertEqual(tasser(input), expected)

    def test_tasser_empty(self):
        input = ()
        expected = []
        self.assertEqual(tasser(input), expected)

    def test_tasser_singleton(self):
        input = ('q')
        expected = ['q']
        self.assertEqual(tasser(input), expected)

    def test_tasser_singleton_pebble(self):
        input = ('.')
        expected = ['.']
        self.assertEqual(tasser(input), expected)

    def test_tasser_pair1(self):
        input = ('a','.')
        expected = ['a', '.']
        self.assertEqual(tasser(input), expected)

    def test_tasser_pair2(self):
        input = ('.','z')
        expected = ['z', '.']
        self.assertEqual(tasser(input), expected)

    def test_tasser_pair3(self):
        input = ('a','z')
        expected = ['a', 'z']
        self.assertEqual(tasser(input), expected)

    def test_tasser_pair4(self):
        input = ('.','.')
        expected = ['.', '.']
        self.assertEqual(tasser(input), expected)

if __name__ == '__main__':
    unittest.main()