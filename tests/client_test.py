import unittest
import sys
sys.path.append("C:/GitHub/atomic_object_project/src")
import client

class TestGetMove(unittest.TestCase):
  def test_get_move_returns_a_valid_move(self):
    board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    self.assertEqual([2,3], [2, 3])

class TestPrepareResponse(unittest.TestCase):
  def test_prepare_response_returns_a_valid_response(self):
    self.assertEqual(client.prepare_response([2, 3]), b'[2, 3]\n')

if __name__ == '__main__':
  unittest.main()