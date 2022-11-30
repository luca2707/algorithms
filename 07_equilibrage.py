# Exemple 7 : Équilibrage
# Diviser un tableau (array) de nombre en deux de manière à ce que la différence entre les deux
# tableaux soit la plus petite possible.

# I assume that the input is a list of numbers.
# The algorithm has to cut the list in two, so that the difference between the sums
# of the numbers in the 2 lists is as small as possible, i.e. so that the sum of all the numbers
# in the first list is as close as possible to the sum of the numbers in the second list.

import unittest
import logging

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.DEBUG)

def split_list(in_list: list[int]) -> tuple(list[int]):
    """ This function takes as input a list of integers, and splits the input list in two.
        The function returns a tuple with 2 elements that contain the 2 lists of integers
        that resulted from the split.
        The function will split the list so that the sum of all integers in the first list
        is as close as possible to the sum of all integers in the second list.
    """
    # First handle the obvious limit cases
    if len(in_list) == 0:
        return ((), ())
    if len(in_list) == 1:
        return (in_list, ())
    if len(in_list) == 2:
        return ((in_list[0]), (in_list[1]))
    # At this point the input list contains at least 3 elements => we can use the algorithm
    left_cursor = 0
    left_sum = in_list[left_cursor]
    logging.debug("left_sum={}".format(left_sum))
    right_cursor = len(in_list) - 1;
    right_sum = in_list[right_cursor]
    logging.debug("right_sum={}".format(right_sum))
    while(left_cursor + 1 < right_cursor):
        if left_sum < right_sum:
            # Push the left_cursor one position to the right
            left_cursor += 1
            logging.debug("Moving left cursor to position {}".format(left_cursor))
            left_sum += in_list[left_cursor]
            logging.debug("left_sum={}".format(left_sum))
        else:
            # Push the right_cursor one position to the left
            right_cursor -= 1
            logging.debug("Moving right cursor to position {}".format(right_cursor))
            right_sum += in_list[right_cursor]
            logging.debug("right_sum={}".format(right_sum))
    # End position reached => build the sub lists
    left_list = in_list[:right_cursor]
    right_list = in_list[right_cursor:]
    return (left_list, right_list)

class TestSplitList(unittest.TestCase):

    def test_split_list_short1(self):
        in_list = (12, 34, 23, 20, 5, 5, 12, 16, 5)
        expected = ((12, 34, 23), (20, 5, 5, 12, 16, 5))
        self.assertEqual(split_list(in_list), expected)

    def test_split_list_short2(self):
        in_list = (1, 1, 1, 1, 1, 1, 2, 2, 2)
        expected = ((1, 1, 1, 1, 1, 1), (2, 2, 2))
        self.assertEqual(split_list(in_list), expected)

    def test_split_list_short3(self):
        in_list = (31, 1, 1, 1, 1, 1, 34)
        expected = ((31, 1, 1, 1, 1), (1, 34))
        self.assertEqual(split_list(in_list), expected)

    def test_split_list_empty(self):
        in_list = ()
        expected = ((), ())
        self.assertEqual(split_list(in_list), expected)

    def test_split_list_singleton(self):
        in_list = (123345, )
        expected = ((123345, ), ())
        self.assertEqual(split_list(in_list), expected)

    def test_split_list_pair(self):
        in_list = (123345, 52345)
        expected = ((123345), (52345))
        self.assertEqual(split_list(in_list), expected)

# The following instruction will automatically launch any tests that are defined in this module
if __name__ == '__main__':
    unittest.main()