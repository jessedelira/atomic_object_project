#!/usr/bin/python

import sys
import json
import socket
import numpy as np
import random
from movePicker import movePicker

mp = movePicker()

def get_move(player, board):
  moves = mp.get_next_move(board)
  print('number of possible moves:',len(moves))
  random_index = random.randint(0,len(moves)-1)
  # TODO determine valid moves
  # TODO determine best move
  # Final: return np.get_next_move(board)
  return moves[random_index]

def prepare_response(move):
  response = '{}\n'.format(move).encode()
  print('sending {!r}'.format(response))
  return response

if __name__ == "__main__":
  port = int(sys.argv[1]) if (len(sys.argv) > 1 and sys.argv[1]) else 1337
  host = sys.argv[2] if (len(sys.argv) > 2 and sys.argv[2]) else socket.gethostname()

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    sock.connect((host, port))
    while True:
      data = sock.recv(1024)
      if not data:
        print('connection to server closed')
        break
      json_data = json.loads(str(data.decode('UTF-8')))
      board = json_data['board']
      maxTurnTime = json_data['maxTurnTime']
      player = json_data['player']
      board = np.array(board)
      print(f"Player:{player}\n", f"Max Turn Time:{maxTurnTime}\n", board)
      board = board.tolist()
      move = get_move(player, board)
      response = prepare_response(move)
      sock.sendall(response)
  finally:
    sock.close()
