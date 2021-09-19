#!/usr/bin/python
class movePicker:
    @classmethod
    def get_next_move(self,board):
        legal_moves = self.get_all_legal_moves(board)
        return self.get_best_move(legal_moves)
        
      
   
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
                                all_legal_moves.append([row_idx,idx,possible_points])
                                print('all legal moves are:',all_legal_moves)
                                break       
                            
                    # Horizontal Left
                    if(board[row_idx][column_idx-1] == 2):
                        for idx in reversed(range(0,column_idx-1)):
                            if(board[row_idx][idx] == 1):
                                break
                            if(board[row_idx][idx] == 2):
                                possible_points += 1
                            if(board[row_idx][idx] == 0):
                                all_legal_moves.append([row_idx,idx,possible_points])
                                print('all legal moves are:',all_legal_moves)
                                break
                            if(board[row_idx][idx] == 2):
                                possible_points += 1
                    
                    # Vertical Above
                    if(board[row_idx-1][column_idx] == 2):
                        for idx in reversed(range(0,row_idx-1)):
                            if(board[idx][column_idx] == 1):
                                break
                            if(board[idx][column_idx] == 2):
                                possible_points += 1
                            if(board[idx][column_idx] == 0):
                                all_legal_moves.append([idx,column_idx,possible_points])
                                print('all legal moves are:',all_legal_moves)
                                break
                    
                    # Vertical Below
                    if(board[row_idx+1][column_idx] == 2):
                        for idx in range(row_idx+2,8):
                            if(board[idx][column_idx] == 1):
                                break
                            if(board[idx][column_idx] == 2):
                                possible_points += 1
                            if(board[idx][column_idx] == 0):
                                all_legal_moves.append([idx,column_idx,possible_points])
                                print('all legal moves are:',all_legal_moves)
                                break
                    
                    # Up Left Diagnol
                    if(board[row_idx-1][column_idx-1] == 2):
                        temp_col_idx = column_idx-2
                        temp_row_idx = row_idx-2
                        while(temp_row_idx >= 0 and temp_col_idx >= 0):
                            if(board[temp_row_idx][temp_col_idx] == 1):
                                break
                            if(board[temp_row_idx][temp_col_idx] == 2):
                                possible_points += 1
                            if(board[temp_row_idx][temp_col_idx] == 0):
                                print('up left diagnol')
                                all_legal_moves.append([temp_row_idx,temp_col_idx,possible_points])
                                break
                            temp_col_idx -= 1
                            temp_row_idx -= 1
                                
                    
                    # Up Right Diagnol
                    if(board[row_idx-1][column_idx+1] == 2):
                        temp_col_idx = column_idx+2
                        temp_row_idx = row_idx-2
                        while(temp_row_idx >= 0 and temp_col_idx > len(board)):
                            if(board[temp_row_idx][temp_col_idx] == 1):
                                break
                            if(board[temp_row_idx][temp_col_idx] == 2):
                                possible_points += 1
                            if(board[temp_row_idx][temp_col_idx] == 0):
                                print('up right diagnol')
                                all_legal_moves.append([temp_row_idx,temp_col_idx,possible_points])
                                break
                            temp_col_idx += 1
                            temp_row_idx -= 1
                    
                    # Down Left Diagnol
                    
                    # Down Right Diagnol
                    
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