import unittest
import sys
sys.path.append("C:/GitHub/atomic_object_project/src")
from movePicker import movePicker


class movePicker_get_next_move_test(unittest.TestCase):
    def test_able_to_call(self):
        board = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 2, 0, 0, 0],
                 [0, 0, 0, 2, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        mp = movePicker()
        result = mp.get_next_move(board)

class movePicker_get_all_legal_moves_test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls._mp = movePicker()
    
    def test_has_get_all_legal_moves_function(self):
        
        board = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 2, 0, 0, 0],
                 [0, 0, 0, 2, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self._mp.get_all_legal_moves(board)

    def test_able_to_pass_args_to_get_all_legal_moves(self):
        
        board = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 2, 0, 0, 0],
                 [0, 0, 0, 2, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        self._mp.get_all_legal_moves(board)
    
    # Vertical/Horizontal Tests
    
    def test_vertical_above_two_spaces(self):
        board = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 2, 2, 2, 0, 0],
                 [0, 0, 0, 1, 0, 2, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        result = self._mp.get_next_move(board)
        self.assertListEqual(result,[3,5])
    
    def test_vertical_below_two_spaces(self):
        board = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 2, 2, 2, 0, 0],
                 [0, 0, 0, 1, 0, 2, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        result = self._mp.get_next_move(board)
        self.assertListEqual(result,[6,5])
        
    def test_horizontal_right_two_spaces(self):
        board = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 2, 2, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        result = self._mp.get_next_move(board)
        self.assertListEqual(result,[4,5])
    
    def test_horizontal_left_two_spaces(self):
        board = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 2, 0, 0, 0],
                 [0, 0, 2, 2, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        result = self._mp.get_next_move(board)
        self.assertListEqual(result,[4,1])
    
    # Diagonal Tests
    def test_up_right_diagonal_two_spaces(self):
        board = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 2, 0],
                 [0, 0, 0, 0, 0, 2, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        result = self._mp.get_next_move(board)
        self.assertListEqual(result,[1,7])
        
    def test_up_left_diagonal_two_spaces(self):
        board = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 2, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        result = self._mp.get_next_move(board)
        self.assertListEqual(result,[1,0])
    
    def test_down_right_diagonal_two_spaces(self):
        board = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 2, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 0, 0, 2, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        result = self._mp.get_next_move(board)
        self.assertListEqual(result,[7,6])
        
    def test_down_left_diagonal_two_spaces(self):
        board = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
        result = self._mp.get_next_move(board)
        self.assertListEqual(result,[5,1])
        
    
    
if __name__ == '__main__':
    unittest.main()

