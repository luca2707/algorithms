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

# The following classes were used in an attempt to solve the problem above.
# But the attemps failed.
# I just keep the MatrixCursor classes because they show an interesting example  in which
# A base class (MatrixCursor) is used to hold common attributes and methods that are used by both
# sub-classes (VerticalMatrixCursor and HorizontalMatrixCursor)
# - The horizontal cursor just moves horizontally, left to right.
#   When he reaches the end of the line, he jumps vertically to the next line.
# - The vertical cursor just moves vertically, top to bottom.
#   When he reaches the end of the column, he jumps horizontally to the next column.

import unittest

class MatrixCursor():
    """ This class is a base class for matrix cursors. It should not be instanciated directly.
        Use the subclasses like HorizontalMatrixCursor and VerticalMatrixCursor instead.
    """

    matrix: tuple(tuple[int])
    nb_lines: int
    nb_columns: int
    hor_index: int
    hor_init: int
    vert_index: int
    vert_init: int
    
    def __init__(self, matrix: tuple(tuple[int]), hor_init: int, vert_init: int) -> None:
        self.matrix = matrix
        self.nb_lines = len(matrix)
        self.nb_columns = len(matrix[0])
        self.hor_init = hor_init
        self.hor_index = hor_init
        self.vert_init = vert_init
        self.vert_index = vert_init

    def has_next(self) -> bool:
        """ Returns True if the cursor has not yet reached the end of the matrix,
            Returns False if the cursor is already on the last element in the matrix.
        """
        if (self.vert_index == (self.nb_lines -1)) and (self.hor_index == (self.nb_columns - 1)):
            return False
        return True 
    
    def get_current(self) -> int:
        """ Returns the matrix element at the current cursor position, without moving the cursor"""
        return self.matrix[self.vert_index][self.hor_index]


class VerticalMatrixCursor(MatrixCursor):
    """ This class implements a cursor that navigates through a matrix vertically.
        It starts at the top-left corner, goes down the first column, then jumps back to the
        top of the next column, goes down again, until it finally goes back to the top of the last column
        and goes down one last time until the bottom right element.
    """

    def __init__(self, matrix: tuple(tuple[int])) -> None:
        super().__init__(matrix, hor_init=0, vert_init=-1)
    
    def next(self) -> int:
        """ Advances the cursor to the next element in the matrix, and returns that element.
            Returns 'None' if the cursor was already at the end of the matrix.
            Tip: use method has_next() to check if there is a 'next' element before calling next().
        """
        # advance to the next vertical element
        if self.vert_index < (self.nb_lines - 1):
            # The cursor is not yet on the last line => jump to the next line
            self.vert_index += 1
        else:
            # The cursor is on the last line => it has to jump to the first line of the next column.
            # First check on which column the cursor is
            if self.hor_index < (self.nb_columns - 1):
                # The cursor is not yet on the last column => jump to the next colum
                self.hor_index += 1
                self.vert_index = 0
            else:
                # The cursor is already on the last column => end of the matrix has been reached
                # Reset the cursors and return None
                self.vert_index = self.vert_init
                self.hor_index = self.hor_init
                return None
        # The cursor has been advanced, now return the matrix element at the cursor position
        return self.get_current()

class HorizontalMatrixCursor(MatrixCursor):
    """ This class implements a cursor that navigates through a matrix horizontally.
        It starts at the top-left corner, goes right on the first line, then jumps back to the
        left-most position of the next line, goes right again, until it finally goes back to the
        left-most element of the last line and goes right one last time until the bottom right element.
    """

    def __init__(self, matrix: tuple(tuple[int])) -> None:
        super().__init__(matrix, hor_init=-1, vert_init=0)
        
    def next(self) -> int:
        """ Advances the cursor to the next element in the matrix, and returns that element.
            Returns 'None' if the cursor was already at the end of the matrix.
            Tip: use method has_next() to check if there is a 'next' element before calling next().
        """
        # advance to the next horizontal element
        if self.hor_index < (self.nb_columns - 1):
            # The cursor is not yet on the last column => jump to the next column
            self.hor_index += 1
        else:
            # The cursor is in the last column => it has to jump to the first column of the next line.
            # First check on which line the cursor is
            if self.vert_index < (self.nb_lines - 1):
                # The cursor is not yet on the last line => jump to the next line
                self.vert_index += 1
                self.hor_index = 0
            else:
                # The cursor is already on the last line => end of the matrix has been reached
                # Reset the cursors and return None
                self.vert_index = self.vert_init
                self.hor_index = self.hor_init
                return None
        # The cursor has been advanced, now return the matrix element at the cursor position
        return self.get_current()

class TestMatrixCursors(unittest.TestCase):

    input_matrix_1 = (( 1,  4, 11, 12),
                      ( 2,  6, 14, 17),
                      ( 3,  7, 15, 18))

    input_matrix_2 = (( 1,  2,  6, 11),
                      ( 3,  4,  7, 15),
                      (12, 14, 17, 18))

    def test_vertical_cursor(self):
        vert_cursor = VerticalMatrixCursor(self.input_matrix_1)
        expected = [1, 2, 3, 4, 6, 7, 11, 14, 15, 12, 17, 18]
        result_list = []
        while vert_cursor.has_next():
            result_list.append(vert_cursor.next())
        self.assertEqual(result_list, expected)
        vert_cursor = VerticalMatrixCursor(self.input_matrix_2)
        expected = [1, 3, 12, 2, 4, 14, 6, 7, 17, 11, 15, 18]
        result_list = []
        while vert_cursor.has_next():
            result_list.append(vert_cursor.next())
        self.assertEqual(result_list, expected)
        
    def test_horizontal_cursor(self):
        vert_cursor = HorizontalMatrixCursor(self.input_matrix_1)
        expected = [1, 4, 11, 12, 2, 6, 14, 17, 3, 7, 15, 18]
        result_list = []
        while vert_cursor.has_next():
            result_list.append(vert_cursor.next())
        self.assertEqual(result_list, expected)
        vert_cursor = HorizontalMatrixCursor(self.input_matrix_2)
        expected = [1, 2, 6, 11, 3, 4, 7, 15, 12, 14, 17, 18]
        result_list = []
        while vert_cursor.has_next():
            result_list.append(vert_cursor.next())
        self.assertEqual(result_list, expected)

if __name__ == '__main__':
    unittest.main()

