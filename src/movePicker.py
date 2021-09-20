#!/usr/bin/python
import random as rd
class movePicker:
    
    used_directions = {"Up Right": 0,
                           "Down Right": 0, "Up Left": 0, "Down Left": 0, "Vertical Above":0}
    @classmethod
    def get_next_move(self, board):
        legal_moves = self.get_all_legal_moves(board)
        return self.get_best_move(legal_moves)

    @classmethod
    def get_all_legal_moves(self,board):
        all_legal_moves = []

        for row_idx in range(len(board)-1):
            for column_idx in range(len(board[row_idx])-1):
                possible_points = 1
                # check if there is a one a spot
                if(board[row_idx][column_idx] == 1):

                    # Horizontal Right
                    if(board[row_idx][column_idx+1] == 2):
                        for idx in range(column_idx+2, len(board[row_idx])):
                            if(board[row_idx][idx] == 1):
                                break
                            if(board[row_idx][idx] == 2):
                                possible_points += 1
                            if(board[row_idx][idx] == 0):
                                all_legal_moves.append([row_idx, idx, possible_points])
                                print('all legal moves are:', all_legal_moves)
                                break

                    # Horizontal Left
                    if(board[row_idx][column_idx-1] == 2):
                        for idx in reversed(range(0, column_idx-1)):
                            if(board[row_idx][idx] == 1):
                                break
                            if(board[row_idx][idx] == 2):
                                possible_points += 1
                            if(board[row_idx][idx] == 0):
                                all_legal_moves.append([row_idx, idx, possible_points])
                                print('all legal moves are:', all_legal_moves)
                                break
                            if(board[row_idx][idx] == 2):
                                possible_points += 1

                    # Vertical Above
                    if(board[row_idx-1][column_idx] == 2):
                        for idx in reversed(range(0, row_idx-1)):
                            if(board[idx][column_idx] == 1):
                                break
                            if(board[idx][column_idx] == 2):
                                possible_points += 1
                            if(board[idx][column_idx] == 0):
                                all_legal_moves.append([idx, column_idx, possible_points])
                                self.used_directions["Vertical Above"] += 1
                                print('all legal moves are:', all_legal_moves)
                                break

                    # Vertical Below
                    if(board[row_idx+1][column_idx] == 2):
                        for idx in range(row_idx+2, 8):
                            if(board[idx][column_idx] == 1):
                                break
                            if(board[idx][column_idx] == 2):
                                possible_points += 1
                            if(board[idx][column_idx] == 0):
                                all_legal_moves.append([idx, column_idx, possible_points])
                                print('all legal moves are:', all_legal_moves)
                                break

                    # Up Left diagonal
                    if(board[row_idx-1][column_idx-1] == 2):
                        temp_col_idx = column_idx-2
                        temp_row_idx = row_idx-2
                        while(temp_row_idx >= 0 and temp_col_idx >= 0):
                            if(board[temp_row_idx][temp_col_idx] == 1):
                                break
                            if(board[temp_row_idx][temp_col_idx] == 2):
                                possible_points += 1
                            if(board[temp_row_idx][temp_col_idx] == 0):
                                print('up left diagonal')
                                self.used_directions['Up Left'] += 1
                                all_legal_moves.append(
                                    [temp_row_idx, temp_col_idx, possible_points])
                                break
                            temp_col_idx -= 1
                            temp_row_idx -= 1

                    # Up Right diagonal
                    if(board[row_idx-1][column_idx+1] == 2):
                        temp_col_idx = column_idx+2
                        temp_row_idx = row_idx-2
                        while(temp_row_idx >= 0 and temp_col_idx < len(board)):
                            if(board[temp_row_idx][temp_col_idx] == 1):
                                break
                            if(board[temp_row_idx][temp_col_idx] == 2):
                                possible_points += 1
                            if(board[temp_row_idx][temp_col_idx] == 0):
                                print('up right diagonal')
                                self.used_directions['Up Right'] += 1
                                all_legal_moves.append(
                                    [temp_row_idx, temp_col_idx, possible_points])
                                break
                            temp_col_idx += 1
                            temp_row_idx -= 1

                    # Down Left diagonal
                    if(board[row_idx+1][column_idx-1] == 2):
                        temp_col_idx = column_idx-2
                        temp_row_idx = row_idx+2
                        while(temp_row_idx < len(board) and temp_col_idx >= 0):
                            if(board[temp_row_idx][temp_col_idx] == 1):
                                break
                            if(board[temp_row_idx][temp_col_idx] == 2):
                                possible_points += 1
                            if(board[temp_row_idx][temp_col_idx] == 0):
                                print('down left diagonal')
                                self.used_directions['Down Left'] += 1
                                all_legal_moves.append([temp_row_idx, temp_col_idx, possible_points])
                                print('temp_col_idx:',temp_col_idx)
                                print('temp_row_idx',temp_row_idx)
                                break
                            temp_col_idx -= 1
                            temp_row_idx += 1
                            

                    # Down Right diagonal
                    if(board[row_idx+1][column_idx+1] == 2):
                        temp_col_idx = column_idx+2
                        temp_row_idx = row_idx+2
                        while(temp_row_idx < len(board) and temp_col_idx < len(board)):
                            if(board[temp_row_idx][temp_col_idx] == 1):
                                break
                            if(board[temp_row_idx][temp_col_idx] == 2):
                                possible_points += 1
                            if(board[temp_row_idx][temp_col_idx] == 0):
                                print('down right diagonal')
                                self.used_directions['Down Right'] += 1
                                all_legal_moves.append([temp_row_idx, temp_col_idx, possible_points])
                                break
                            temp_col_idx += 1
                            temp_row_idx += 1

        print(self.used_directions)
        if(len(all_legal_moves) == 0):
            temp = []
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if(board[i][j] == 0):
                        if(board[row_idx][column_idx+1] == 2 or
                            board[row_idx][column_idx-1] == 2 or
                            board[row_idx-1][column_idx] == 2 or
                            board[row_idx+1][column_idx] == 2 or
                            board[row_idx-1][column_idx-1] == 2 or
                            board[row_idx-1][column_idx+1] == 2 or
                            board[row_idx+1][column_idx-1] == 2 or
                            board[row_idx+1][column_idx+1] == 2):
                            temp.append([board[i][j]])
                        if(temp[i][0] == 0 and temp[i][1] == 0 or temp[i][0] == 0 and temp[i][1] == 7 or temp[i][0] == 7 and temp[i][1] == 0 or temp[i][0] == 7 and temp[i][1] == 7):
                            return [[temp[i][0],temp[i][1]]]
            
            random_number = rd.randint(0,len(temp))
            return [temp[random_number]]
                    
        return all_legal_moves

    @staticmethod
    def get_best_move(legal_moves):
        print('LENGTH OF LEGAL MOVES',len(legal_moves))
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
