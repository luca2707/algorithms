# Exemple 8 : Matrice triée
# Étant donné une matrice de nombres entiers, où chaque ligne et chaque colonne sont
# triées par ordre croissant, imprimer tous les éléments dans l’ordre croissant.

# Let's assume that the input matrix is implemented using a tuple of tuples of integers
# Example 1: input_matrix = (( 1,  4, 11, 12),
#                            ( 2,  6, 14, 17),
#                            ( 3,  7, 15, 18))

# Example 2: input_matrix = (( 1,  2,  6, 11),
#                            ( 3,  4,  7, 15),
#                            (12, 14, 17, 18))

# Safe Idea:
# 1. Create as many cursors as there are lines in the matrix.
# 2. All cursors load their next element.
# 3. Choose the smallest element among the loaded matrix elements, then let the corresponding cursor advance.
# To manage each cursor we just need 1 variable: the position of the cursor (cursor_index).
# An int variable (min_value) is needed to keep track of the minimum value
# in the set of values that the cursors are pointing to.
# Another int variable (min_line_index) is needed to keep track of which line currently holds the minimum value.

import unittest


def matrix_sort(input_matrix: tuple(tuple[int])) -> list[int]:
    result_list = list()
    # Handle the limit cases
    nb_lines = len(input_matrix)
    if nb_lines == 0:
        # Empty matrix => return empty list
        return result_list
    # Check that the matrix is well formed, i.e. that every line has the same number of columns
    nb_columns = len(input_matrix[0])
    if nb_lines >= 2:
        for i in range(1, nb_lines):
            if len(input_matrix[i]) != nb_columns:
                raise RuntimeError("Input matrix is not well formatted (line {} does not have the same number of elements as line 0).".format(i))
    # Handle limit case where each line is empty
    if nb_columns == 0:
        return result_list
    # create the cursor_index list that will store the horizontal position of each cursor in its line
    # N.B. If a cursor has reached the end of the line, the cursor_index will be equal to nb_columns
    cursor_index = list()
    # Initial state:
    # - all cursor_indexes == 0, i.e. are pointing to the first element in the line
    # - min_value points to the smallest of the values (which is always the first element in the first line)
    # - min_line_index points to the line containing the smallest value (which is always the first line)
    min_value = input_matrix[0][0]
    min_line_index = 0
    for i in range(nb_lines):
        cursor_index.append(0)
    # Start the loop which will continue until we have nb_lines * nb_columns in the result_list
    while (len(result_list) < nb_lines * nb_columns):
        # Put the current minimum value on the result list, then move the cursor forward
        # on the line that holds the minimum value
        result_list.append(min_value)
        cursor_index[min_line_index] += 1
        # Scan all elements in the current cursor state to identify the smallest value.
        # Set the initial min_value to the value of the last element in the matrix, which is always the biggest
        min_value = input_matrix[nb_lines - 1][nb_columns - 1]
        for i in range(nb_lines):
            # If the index of a cursor is beyond nb_columns => ignore
            if cursor_index[i] < nb_columns:
            # The cursor is on a valid matrix element => compare it with the current min cursor value
                new_value = input_matrix[i][cursor_index[i]]
                if new_value < min_value:
                    min_value = new_value
                    min_line_index = i
    return result_list

class TestMatrixSort(unittest.TestCase):

    def test_matrix_sort_1(self):
        input_matrix = (( 1,  4, 11, 12),
                        ( 2,  6, 14, 17),
                        ( 3,  7, 15, 18))
        expected = [1, 2, 3, 4, 6, 7, 11, 12, 14, 15, 17, 18]
        self.assertEqual(matrix_sort(input_matrix), expected)

    def test_matrix_sort_2(self):
        input_matrix = (( 1,  2,  6, 11),
                        ( 3,  4,  7, 15),
                        (12, 14, 17, 18))
        expected = [1, 2, 3, 4, 6, 7, 11, 12, 14, 15, 17, 18]
        self.assertEqual(matrix_sort(input_matrix), expected)

    def test_matrix_sort_3(self):
        input_matrix = (( 1,  2,  6, 11),
                        ( 2,  4,  6, 15),
                        (12, 14, 15, 18))
        expected = [1, 2, 2, 4, 6, 6, 11, 12, 14, 15, 15, 18]
        self.assertEqual(matrix_sort(input_matrix), expected)

    def test_matrix_sort_empty_1(self):
        input_matrix = ()
        expected = []
        self.assertEqual(matrix_sort(input_matrix), expected)

    def test_matrix_sort_empty_2(self):
        input_matrix = ((), (), ())
        expected = []
        self.assertEqual(matrix_sort(input_matrix), expected)
    
    def test_matrix_sort_4(self):
        input_matrix = ((1, ), (4, ), (7, ))
        expected = [1, 4, 7]
        self.assertEqual(matrix_sort(input_matrix), expected)

    def test_matrix_sort_5(self):
        input_matrix = ((1, 4, 7))
        expected = [1, 4, 7]
        self.assertEqual(matrix_sort(input_matrix), expected)

    def test_matrix_sort_5(self):
        # Tests that the code within the body of the with statement raises a RuntimeError
        # (because the matrix passed as input argument is not well formed).
        with self.assertRaises(RuntimeError):
            input_matrix = ((1, 4, 7),
                            (2, 5))
            matrix_sort(input_matrix)

if __name__ == '__main__':
    unittest.main()

