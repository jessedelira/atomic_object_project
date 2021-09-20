#!/usr/bin/python
import random as rd
class movePicker:
    @classmethod
    def get_next_move(self, board):
        return self.get_best_move(self.get_all_legal_moves(board))

    

    @classmethod
    def get_all_legal_moves(self,board):
        all_legal_moves = []

        for row_idx in range(len(board)-1):
            for column_idx in range(len(board[row_idx])-1):
                possible_points = 1
                
                if(self.player_token_in_current_position(board, column_idx, row_idx)):
                    
                    if(self.opp_coin_to_right_of_current_position(board,row_idx,column_idx)):
                        for idx in range(column_idx+2, len(board[row_idx])):
                            if(board[row_idx][idx] == 1):
                                break
                            if(board[row_idx][idx] == 2):
                                possible_points += 1
                            if(board[row_idx][idx] == 0):
                                all_legal_moves.append([row_idx, idx, possible_points])
                                break

                    if(self.opp_coin_to_left_of_current_position(board, row_idx, column_idx)):
                        for idx in reversed(range(0, column_idx-1)):
                            if(board[row_idx][idx] == 1):
                                break
                            if(board[row_idx][idx] == 2):
                                possible_points += 1
                            if(board[row_idx][idx] == 0):
                                all_legal_moves.append([row_idx, idx, possible_points])
                                break
                            

                    if(self.opp_coin_above_current_position(board,row_idx,column_idx)):
                        for idx in reversed(range(0, row_idx-1)):
                            if(board[idx][column_idx] == 1):
                                break
                            if(board[idx][column_idx] == 2):
                                possible_points += 1
                            if(board[idx][column_idx] == 0):
                                all_legal_moves.append([idx, column_idx, possible_points])
                                break

                    if(self.opp_coin_below_current_position(board,row_idx,column_idx)):
                        for idx in range(row_idx+2, 8):
                            if(board[idx][column_idx] == 1):
                                break
                            if(board[idx][column_idx] == 2):
                                possible_points += 1
                            if(board[idx][column_idx] == 0):
                                all_legal_moves.append([idx, column_idx, possible_points])
                                break

                    if(self.opp_coin_above_and_left_diagonal_to_current_position(board,row_idx,column_idx)):
                        temp_col_idx = column_idx-2
                        temp_row_idx = row_idx-2
                        while(temp_row_idx >= 0 and temp_col_idx >= 0):
                            if(board[temp_row_idx][temp_col_idx] == 1):
                                break
                            if(board[temp_row_idx][temp_col_idx] == 2):
                                possible_points += 1
                            if(board[temp_row_idx][temp_col_idx] == 0):
                                all_legal_moves.append([temp_row_idx, temp_col_idx, possible_points])
                                break
                            temp_col_idx -= 1
                            temp_row_idx -= 1

                    if(self.opp_coin_above_and_right_diagonal_to_current_position(board,row_idx,column_idx)):
                        temp_col_idx = column_idx+2
                        temp_row_idx = row_idx-2
                        while(temp_row_idx >= 0 and temp_col_idx < len(board)):
                            if(board[temp_row_idx][temp_col_idx] == 1):
                                break
                            if(board[temp_row_idx][temp_col_idx] == 2):
                                possible_points += 1
                            if(board[temp_row_idx][temp_col_idx] == 0):
                                all_legal_moves.append([temp_row_idx, temp_col_idx, possible_points])
                                break
                            temp_col_idx += 1
                            temp_row_idx -= 1

                    if(self.opp_coin_below_and_left_diagonal_to_current_position(board,row_idx,column_idx)):
                        temp_col_idx = column_idx-2
                        temp_row_idx = row_idx+2
                        while(temp_row_idx < len(board) and temp_col_idx >= 0):
                            if(board[temp_row_idx][temp_col_idx] == 1):
                                break
                            if(board[temp_row_idx][temp_col_idx] == 2):
                                possible_points += 1
                            if(board[temp_row_idx][temp_col_idx] == 0):
                                all_legal_moves.append([temp_row_idx, temp_col_idx, possible_points])
                                break
                            temp_col_idx -= 1
                            temp_row_idx += 1
                            
                    if(self.opp_coin_below_and_right_diagonal_to_current_position(board,row_idx,column_idx)):
                        temp_col_idx = column_idx+2
                        temp_row_idx = row_idx+2
                        while(temp_row_idx < len(board) and temp_col_idx < len(board)):
                            if(board[temp_row_idx][temp_col_idx] == 1):
                                break
                            if(board[temp_row_idx][temp_col_idx] == 2):
                                possible_points += 1
                            if(board[temp_row_idx][temp_col_idx] == 0):
                                all_legal_moves.append([temp_row_idx, temp_col_idx, possible_points])
                                break
                            temp_col_idx += 1
                            temp_row_idx += 1
        
        
        if(self.is_empty(all_legal_moves)):
            return self.give_available_move(board)
            
        return all_legal_moves

    @staticmethod
    def get_best_move(legal_moves):
        best_move = []
        max_value = 0
        max_index = 0
        for i in range(len(legal_moves)):
            if(legal_moves[i][0] == 0 and legal_moves[i][1] == 0 or legal_moves[i][0] == 0 and legal_moves[i][1] == 7 or legal_moves[i][0] == 7 and legal_moves[i][1] == 0 or legal_moves[i][0] == 7 and legal_moves[i][1] == 7):
                return [legal_moves[i][0],legal_moves[i][1]]
        
        for i in range(len(legal_moves)):
            if(legal_moves[i][2] > max_value):
                max_value = legal_moves[i][2]
                max_index = i

        best_move.append(legal_moves[max_index][0])
        best_move.append(legal_moves[max_index][1])
        return best_move
    
    @staticmethod
    def player_token_in_current_position(board, column_idx, row_idx):
        return board[row_idx][column_idx] == 1
    
    
    @staticmethod
    def opp_coin_to_right_of_current_position(board,row_idx,column_idx):
        return board[row_idx][column_idx+1] == 2
    
    @staticmethod
    def opp_coin_to_left_of_current_position(board, row_idx, column_idx):
        return board[row_idx][column_idx-1] == 2
    
    @staticmethod
    def opp_coin_above_current_position(board, row_idx, column_idx):
        return  board[row_idx-1][column_idx] == 2
    
    @staticmethod
    def opp_coin_below_current_position(board, row_idx, column_idx):
        return board[row_idx+1][column_idx] == 2
    
    
    @staticmethod
    def opp_coin_above_and_left_diagonal_to_current_position(board, row_idx, column_idx):
        return board[row_idx-1][column_idx-1] == 2
    
    @staticmethod
    def opp_coin_above_and_right_diagonal_to_current_position(board, row_idx, column_idx):
        return board[row_idx-1][column_idx+1] == 2
    
    @staticmethod
    def opp_coin_below_and_left_diagonal_to_current_position(board, row_idx, column_idx):
        return board[row_idx+1][column_idx-1] == 2
    
    @staticmethod
    def opp_coin_below_and_right_diagonal_to_current_position(board, row_idx, column_idx):
        return board[row_idx+1][column_idx+1] == 2
    
    
    @staticmethod
    def current_position_is_available(board,row_idx,column_idx):
        return board[row_idx][column_idx] == 0
    
    @staticmethod
    def give_available_move(board):
        temp = []
        for i in range(len(board)):
            for j in range(len(board)):
                if(board[i][j] == 0):
                    temp.append([i,j])
            random_number = rd.randint(0,len(temp))
            return temp[random_number]  
      
    @staticmethod
    def is_empty(all_legal_moves):
        return len(all_legal_moves) == 0