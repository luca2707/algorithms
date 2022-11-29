# Exemple 5 : En commun
# Concevoir un algorithme pour trouver tous les caractères communs à deux listes triées.
# Par exemple, pour les listes (a, e, e, e) et (b, b, c, e, e, g), la sortie doit être de (e, e).

from sys import argv
import unittest

def common(list1: list, list2: list) -> list:
    result = list()
    l1_index = 0
    l2_index = 0
    while l1_index < len(list1) and l2_index < len(list2):
        char1 = list1[l1_index]
        char2 = list2[l2_index]
        if char1 == char2:
            # Found identical caracters => record them to the result and move forward on both lists
            result.append(char1)
            l1_index += 1
            l2_index += 1
        elif char1 < char2:
            # Character in list1 is smaller => advance index in l1
            l1_index += 1
        else:
            l2_index += 1
    # Reached the end of one list => return the result
    return result

class TestCommon(unittest.TestCase):

    def test_common_1(self):
        l1 = ('a', 'e', 'e', 'e')
        l2 = ('b', 'b', 'c', 'e', 'e', 'g')
        expected = ['e', 'e']
        self.assertEqual(common(l1, l2), expected)

    def test_common_2(self):
        l1 = ('a', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'f', 'g', 'h', 'h', 'k')
        l2 = ('a', 'b', 'b', 'c', 'e', 'h', 'h', 'i', 'i', 'j', 'j', 'k')
        expected = ['a', 'c', 'e', 'h', 'h', 'k']
        self.assertEqual(common(l1, l2), expected)

    # test 3 (empty list)
    def test_common_3(self):
        l1 = ('a', 'e', 'e', 'e')
        l2 = ()
        expected = []
        self.assertEqual(common(l1, l2), expected)

    # test 4 (singleton list)
    def test_common_4(self):
        l1 = ('a', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'f', 'g', 'h', 'h', 'k')
        l2 = ('k')
        expected = ['k']
        self.assertEqual(common(l1, l2), expected)

    # test 5 (singleton list)
    def test_common_5(self):
        l1 = ('a')
        l2 = ('a', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'f', 'g', 'h', 'h', 'k')
        expected = ['a']
        self.assertEqual(common(l1, l2), expected)

if __name__ == '__main__':
    unittest.main()
