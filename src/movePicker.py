#!/usr/bin/python
class movePicker:
    @classmethod
    def get_next_move(self,board):
        legal_moves = self.get_all_legal_moves(board)
        # return get_best_move(legal_moves)
        return legal_moves
      
   
    @staticmethod
    def get_all_legal_moves(board):
        all_legal_moves = []
        
        for row_idx in range(len(board)-1):
            for column_idx in range(len(board[row_idx])-1):
                possible_points = 1
                # check if there is a one if a spot
                if(board[row_idx][column_idx] == 1):
                    # Horizontal Right
                    if(board[row_idx][column_idx+1] == 2):
                        for idx in range(column_idx+2,len(board[row_idx])):  
                            if(board[row_idx][idx] == 1):
                                break
                            # checking if more than one 2, then adding
                            if(board[row_idx][idx] == 2):
                                possible_points += 1
                            if(board[row_idx][idx] == 0):
                                print('to my right!')
                                all_legal_moves.append([row_idx,idx,possible_points])
                                print('all legal moves are:',all_legal_moves)
                                break
                            
                            
                    # Horizontal Left
                    if(board[row_idx][column_idx-1] == 2):
                        for idx in reversed(range(0,column_idx-1)):
                            if(board[row_idx][idx] == 1):
                                break
                            if(board[row_idx][idx] == 0):
                                print('to my left!')
                                all_legal_moves.append([row_idx,idx])
                                print('all legal moves are:',all_legal_moves)
                                break
                            if(board[row_idx][idx] == 2):
                                possible_points += 1
                    # Vertical Above
                    if(board[row_idx-1][column_idx] == 2):
                        for idx in reversed(range(0,row_idx-1)):
                            if(board[idx][column_idx] == 1):
                                break
                            if(board[idx][column_idx] == 0):
                                print('above!')
                                all_legal_moves.append([idx,column_idx])
                                print('all legal moves are:',all_legal_moves)
                                break
                    
                    # Vertical Below
                    if(board[row_idx+1][column_idx] == 2):
                        for idx in range(row_idx+2,8):
                            if(board[idx][column_idx] == 1):
                                break
                            if(board[idx][column_idx] == 0):
                                print('below')
                                all_legal_moves.append([idx,column_idx])
                                print('all legal moves are:',all_legal_moves)
                                break
                    
                    # Diagnol Case
                    # Diagnol to up left, up right, down left, down right
                    
                    
                    # Up Left Diagnol
                    # if(board[row_idx-1][column_idx-1] == 2):
                        # blah blah
                    
                    # Else
                    else:
                        continue
                    
        if(len(all_legal_moves) == 0):
            return 
        return all_legal_moves
    
    @staticmethod
    def get_best_move(legal_moves):
        best_move = []
        max_value = 0
        max_index = 0
        for i in range(len(legal_moves)):
            if(legal_moves[i][2] > max_value):
                max_value = legal_moves[i][2]
                max_index = i
        
        best_move.append(legal_moves[max_index][0])
        best_move.append(legal_moves[max_index][1])

        return best_move