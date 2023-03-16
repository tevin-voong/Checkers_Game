# Author: Tevin Voong
# GitHub username: tevinvoong
# Date: 3/16/2023
# Description: This code allows two people to play the game of checkers. There is a class for Checkers that represents
# the game as played and a class for Players that represents the players in the game

class InvalidSquare(Exception):
    pass


class OutofTurn(Exception):
    pass


class InvalidPlayer(Exception):
    pass


class Checkers:
    """Class that creates the players for the game, allows players to play checkers, or returns checker details on a
    position on the board"""

    def __init__(self):
        """Initializes checkers game and sets the board as a dictionary"""
        self._board = [[None, "White", None, "White", None, "White", None, "White"],
                       ["White", None, "White", None, "White", None, "White", None],
                       [None, "White", None, "White", None, "White", None, "White"],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       ["Black", None, "Black", None, "Black", None, "Black", None],
                       [None, "Black", None, "Black", None, "Black", None, "Black"],
                       ["Black", None, "Black", None, "Black", None, "Black", None]]
        self._players = {}
        self._white_piece_counter = 0
        self._black_piece_counter = 0
        self._white_king_counter = 0
        self._black_king_counter = 0
        self._white_triple_king_counter = 0
        self._black_triple_king_counter = 0
        # self._turn = ["Black"]



    def create_player(self, player_name, piece_color):
        """Takes player name and piece color (black or white) as parameters and returns created player object"""
        checkers_player = (player_name, piece_color)
        self._players[player_name] = piece_color
        return checkers_player

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """Takes player name, starting square location(tuple), and destination square location(tuple) as parameters to
        move checker pieces across the board and accounts for various checker movement scenarios"""

        if self._players[player_name] not in self._board[starting_square_location[0]][starting_square_location[1]]:
            raise InvalidPlayer

        # if (self._board[starting_square_location[0]][starting_square_location[1]] != self._players[player_name]) and (self._board[starting_square_location[0]][starting_square_location[1]] != 'White_King'): # check if player name matches piece color
        #     raise InvalidSquare

        if player_name not in self._players:  # check if player name is in dictionary
            raise InvalidPlayer

        if starting_square_location[0] > 7 or starting_square_location[1] > 7:  # check if first tuple within board
            raise InvalidSquare

        if destination_square_location[0] > 7 or destination_square_location[1] > 7:  # check if 2nd tuple within board
            raise InvalidSquare

        for players in self._players:
            if player_name == players:
                capture_count = 0
                start_row_num = starting_square_location[0]
                start_column_num = starting_square_location[1]
                des_row_num = destination_square_location[0]
                des_column_num = destination_square_location[1]

                # if piece is white and there are no diagonal pieces to capture
                if self._board[start_row_num][start_column_num] == 'White':
                    if self._board[start_row_num + 1][start_column_num - 1] is None and start_column_num == 7:
                        start_row_num = starting_square_location[0]
                        start_column_num = starting_square_location[1]
                        self._board[start_row_num][start_column_num] = None
                        des_row_num = destination_square_location[0]
                        des_column_num = destination_square_location[1]
                        if des_row_num == 7:
                            self._board[des_row_num][des_column_num] = "White_King"
                            self._white_king_counter += 1
                            self._white_piece_counter += capture_count
                            return capture_count
                        else:
                            self._board[des_row_num][des_column_num] = self._players[players]
                            self._white_piece_counter += capture_count
                            return capture_count
                    if self._board[start_row_num + 1][start_column_num - 1] is None or self._board[start_row_num + 1][start_column_num + 1] is None:
                        if (self._board[start_row_num + 1][start_column_num - 1] != 'Black' and self._board[des_row_num][des_column_num] is None) and (self._board[start_row_num + 1][start_column_num + 1] != 'Black' and self._board[des_row_num][des_column_num] is None):
                            start_row_num = starting_square_location[0]
                            start_column_num = starting_square_location[1]
                            self._board[start_row_num][start_column_num] = None
                            des_row_num = destination_square_location[0]
                            des_column_num = destination_square_location[1]
                            if des_row_num == 7:
                                self._board[des_row_num][des_column_num] = "White_King"
                                self._white_king_counter += 1
                                self._white_piece_counter += capture_count
                                return capture_count
                            else:
                                self._board[des_row_num][des_column_num] = self._players[players]
                                self._white_piece_counter += capture_count
                                return capture_count
                        if (self._board[start_row_num + 1][start_column_num - 1] == 'Black' and self._board[start_row_num + 1][start_column_num + 1] != 'Black') or (self._board[start_row_num + 1][start_column_num + 1] == 'Black' and self._board[start_row_num + 1][start_column_num - 1] != 'Black'):
                            if (des_row_num != start_row_num + 2) and (des_column_num != start_column_num + 2):
                                start_row_num = starting_square_location[0]
                                start_column_num = starting_square_location[1]
                                self._board[start_row_num][start_column_num] = None
                                des_row_num = destination_square_location[0]
                                des_column_num = destination_square_location[1]
                                if des_row_num == 7:
                                    self._board[des_row_num][des_column_num] = "White_King"
                                    self._white_king_counter += 1
                                    self._white_piece_counter += capture_count
                                    return capture_count
                                else:
                                    self._board[des_row_num][des_column_num] = self._players[players]
                                    self._white_piece_counter += capture_count
                                    return capture_count

                # If piece is a White King and there are no diagonal pieces to capture
                if self._board[start_row_num][start_column_num] == 'White_King':
                    if self._board[start_row_num - 1][start_column_num - 1] is None or self._board[start_row_num - 1][start_column_num + 1] is None or self._board[start_row_num + 1][start_column_num - 1] is None or self._board[start_row_num + 1][start_column_num + 1] is None:
                        if (self._board[start_row_num - 1][start_column_num - 1] == self._board[des_row_num][des_column_num]) and (self._board[start_row_num - 1][start_column_num + 1] == self._board[des_row_num][des_column_num]) and (self._board[start_row_num + 1][start_column_num - 1] == self._board[des_row_num][des_column_num]) and (self._board[start_row_num + 1][start_column_num + 1] == self._board[des_row_num][des_column_num]):
                            start_row_num = starting_square_location[0]
                            start_column_num = starting_square_location[1]
                            self._board[start_row_num][start_column_num] = None
                            des_row_num = destination_square_location[0]
                            des_column_num = destination_square_location[1]
                            if des_row_num == 0:
                                self._board[des_row_num][des_column_num] = "White_Triple_King"
                                self._white_triple_king_counter += 1
                                self._white_king_counter -= 1
                                self._white_piece_counter += capture_count
                                return capture_count
                            else:
                                self._board[des_row_num][des_column_num] = 'White_King'
                                self._white_piece_counter += capture_count
                                return capture_count

                # If piece is Black and there are no diagonal pieces to capture
                if self._board[start_row_num][start_column_num] == 'Black':
                    if self._board[start_row_num - 1][start_column_num - 1] is None or self._board[start_row_num - 1][start_column_num + 1] is None:
                        if (self._board[start_row_num - 1][start_column_num - 1] != 'White' and self._board[des_row_num][des_column_num] is None) and (self._board[start_row_num - 1][start_column_num + 1] != 'White' and self._board[des_row_num][des_column_num] is None):
                            if (self._board[start_row_num - 1][start_column_num - 1] != 'White_King' and self._board[des_row_num][des_column_num] is None) and (self._board[start_row_num - 1][start_column_num + 1] != 'White_King' and self._board[des_row_num][des_column_num] is None):
                                start_row_num = starting_square_location[0]
                                start_column_num = starting_square_location[1]
                                self._board[start_row_num][start_column_num] = None
                                des_row_num = destination_square_location[0]
                                des_column_num = destination_square_location[1]
                                if des_row_num == 0:
                                    self._board[des_row_num][des_column_num] = "Black_King"
                                    self._black_king_counter += 1
                                    self._black_piece_counter += capture_count
                                    return capture_count
                                else:
                                    self._board[des_row_num][des_column_num] = self._players[players]
                                    self._black_piece_counter += capture_count
                                    return capture_count
                        if (self._board[start_row_num - 1][start_column_num - 1] == 'White' and self._board[start_row_num - 1][start_column_num + 1] != 'White') or (self._board[start_row_num - 1][start_column_num + 1] == 'White' and self._board[start_row_num - 1][start_column_num - 1] != 'White'):
                            if (des_row_num != start_row_num - 2) and (des_column_num != start_column_num - 2):
                                start_row_num = starting_square_location[0]
                                start_column_num = starting_square_location[1]
                                self._board[start_row_num][start_column_num] = None
                                des_row_num = destination_square_location[0]
                                des_column_num = destination_square_location[1]
                                if des_row_num == 0:
                                    self._board[des_row_num][des_column_num] = "Black_King"
                                    self._black_king_counter += 1
                                    self._black_piece_counter += capture_count
                                    return capture_count
                                else:
                                    self._board[des_row_num][des_column_num] = self._players[players]
                                    self._black_piece_counter += capture_count
                                    return capture_count

                # If piece is a Black King and there are no diagonal pieces to take
                if self._board[start_row_num][start_column_num] == 'Black_King':
                    if self._board[start_row_num - 1][start_column_num - 1] is None or self._board[start_row_num - 1][start_column_num + 1] is None or self._board[start_row_num + 1][start_column_num - 1] is None or self._board[start_row_num + 1][start_column_num + 1] is None:
                        if (start_row_num - 1 == des_row_num and start_column_num - 1 == des_column_num) or (start_row_num - 1 == des_row_num and start_column_num + 1 == des_column_num) or (start_row_num + 1 == des_row_num and start_column_num - 1 == des_column_num) or (start_row_num + 1 == des_row_num and start_column_num + 1 == des_column_num):
                            start_row_num = starting_square_location[0]
                            start_column_num = starting_square_location[1]
                            self._board[start_row_num][start_column_num] = None
                            des_row_num = destination_square_location[0]
                            des_column_num = destination_square_location[1]
                            if des_row_num == 7:
                                self._board[des_row_num][des_column_num] = "Black_Triple_King"
                                self._black_triple_king_counter += 1
                                self._black_king_counter -= 1
                                self._black_piece_counter += capture_count
                                return capture_count
                            else:
                                self._board[des_row_num][des_column_num] = 'Black_King'
                                self._black_piece_counter += capture_count
                                return capture_count

                # If piece is a Black Triple King and there are no diagonal pieces to take
                if self._board[start_row_num][start_column_num] == 'Black_Triple_King':
                    if self._board[start_row_num - 1][start_column_num - 1] is None or self._board[start_row_num - 1][start_column_num + 1] is None or self._board[start_row_num + 1][start_column_num - 1] is None or self._board[start_row_num + 1][start_column_num + 1] is None:
                        if (start_row_num - 1 == des_row_num and start_column_num - 1 == des_column_num) or (start_row_num - 1 == des_row_num and start_column_num + 1 == des_column_num) or (start_row_num + 1 == des_row_num and start_column_num - 1 == des_column_num) or (start_row_num + 1 == des_row_num and start_column_num + 1 == des_column_num):
                            start_row_num = starting_square_location[0]
                            start_column_num = starting_square_location[1]
                            self._board[start_row_num][start_column_num] = None
                            des_row_num = destination_square_location[0]
                            des_column_num = destination_square_location[1]
                            self._board[des_row_num][des_column_num] = 'Black_Triple_King'
                            self._black_piece_counter += capture_count
                            return capture_count

                if self._board[start_row_num][start_column_num] == 'White_Triple_King':
                    if self._board[start_row_num - 1][start_column_num - 1] is None or self._board[start_row_num - 1][start_column_num + 1] is None or self._board[start_row_num + 1][start_column_num - 1] is None or self._board[start_row_num + 1][start_column_num + 1] is None:
                        if (start_row_num - 1 == des_row_num and start_column_num - 1 == des_column_num) or (start_row_num - 1 == des_row_num and start_column_num + 1 == des_column_num) or (start_row_num + 1 == des_row_num and start_column_num - 1 == des_column_num) or (start_row_num + 1 == des_row_num and start_column_num + 1 == des_column_num):
                            start_row_num = starting_square_location[0]
                            start_column_num = starting_square_location[1]
                            self._board[start_row_num][start_column_num] = None
                            des_row_num = destination_square_location[0]
                            des_column_num = destination_square_location[1]
                            self._board[des_row_num][des_column_num] = 'White_Triple_King'
                            self._white_piece_counter += capture_count
                            return capture_count


                # if there are diagonal pieces to capture
                if (self._board[start_row_num - 1][start_column_num - 1] is not None or self._board[start_row_num - 1][start_column_num + 1]) is not None or (self._board[start_row_num + 1][start_column_num - 1] is not None or self._board[start_row_num + 1][start_column_num + 1]) is not None:
                    # if piece is white
                    if self._board[start_row_num][start_column_num] == 'White':
                        if self._board[start_row_num + 1][start_column_num - 1] and self._board[des_row_num - 1][des_column_num + 1] is not None:
                            capture_count += 1
                            if start_column_num - 1 == -1:
                                self._board[start_row_num + 1][start_column_num + 1] = None
                                self._board[start_row_num][start_column_num] = None
                                if des_row_num == 7:
                                    self._board[des_row_num][des_column_num] = "White_King"
                                    self._white_king_counter += 1
                                    self._white_piece_counter += capture_count
                                    return capture_count
                                else:
                                    self._board[des_row_num][des_column_num] = 'White'
                                    self._white_piece_counter += capture_count
                                    return capture_count
                            else:
                                self._board[start_row_num + 1][start_column_num - 1] = None
                                self._board[start_row_num][start_column_num] = None
                                if des_row_num == 7:
                                    self._board[des_row_num][des_column_num] = "White_King"
                                    self._white_king_counter += 1
                                    self._white_piece_counter += capture_count
                                    return capture_count
                                else:
                                    self._board[des_row_num][des_column_num] = 'White'
                                    self._white_piece_counter += capture_count
                                    return capture_count
                        if self._board[start_row_num + 1][start_column_num + 1] and self._board[des_row_num - 1][des_column_num - 1] is not None:
                            capture_count += 1
                            self._board[start_row_num + 1][start_column_num + 1] = None
                            self._board[start_row_num][start_column_num] = None
                            if des_row_num == 7:
                                self._board[des_row_num][des_column_num] = "White_King"
                                self._white_king_counter += 1
                                self._white_piece_counter += capture_count
                                return capture_count
                            else:
                                self._board[des_row_num][des_column_num] = 'White'
                                self._white_piece_counter += capture_count
                                return capture_count

                    # if piece is white king
                    if self._board[start_row_num][start_column_num] == 'White_King':
                        if self._board[start_row_num - 1][start_column_num + 1] is not None or self._board[start_row_num - 1][start_column_num - 1] is not None or self._board[start_row_num + 1][start_column_num + 1] is not None or self._board[start_row_num + 1][start_column_num - 1] is not None:
                            capture_count += 1
                            if self._board[start_row_num - 2][start_column_num + 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num - 1][start_column_num + 1] = None
                                self._board[start_row_num][start_column_num] = None
                                if des_row_num == 0:
                                    self._board[des_row_num][des_column_num] = "White_Triple_King"
                                    self._white_triple_king_counter += 1
                                    self._white_king_counter -= 1
                                    self._white_piece_counter += capture_count
                                    return capture_count
                                else:
                                    self._board[des_row_num][des_column_num] = 'White_King'
                                    self._white_piece_counter += capture_count
                                    return capture_count
                            if self._board[start_row_num - 2][start_column_num - 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num - 1][start_column_num - 1] = None
                                self._board[start_row_num][start_column_num] = None
                                if des_row_num == 0:
                                    self._board[des_row_num][des_column_num] = "White_Triple_King"
                                    self._white_triple_king_counter += 1
                                    self._white_king_counter -= 1
                                    self._white_piece_counter += capture_count
                                    return capture_count
                                else:
                                    self._board[des_row_num][des_column_num] = 'White_King'
                                    self._white_piece_counter += capture_count
                                    return capture_count
                            if self._board[start_row_num + 2][start_column_num - 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num + 1][start_column_num - 1] = None
                                self._board[start_row_num][start_column_num] = None
                                if des_row_num == 0:
                                    self._board[des_row_num][des_column_num] = "White_Triple_King"
                                    self._white_triple_king_counter += 1
                                    self._white_king_counter -= 1
                                    self._white_piece_counter += capture_count
                                    return capture_count
                                else:
                                    self._board[des_row_num][des_column_num] = 'White_King'
                                    self._white_piece_counter += capture_count
                                    return capture_count
                            if self._board[start_row_num + 2][start_column_num + 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num + 1][start_column_num + 1] = None
                                self._board[start_row_num][start_column_num] = None
                                if des_row_num == 0:
                                    self._board[des_row_num][des_column_num] = "White_Triple_King"
                                    self._white_triple_king_counter += 1
                                    self._white_piece_counter += capture_count
                                    return capture_count
                                else:
                                    self._board[des_row_num][des_column_num] = 'White_King'
                                    self._white_piece_counter += capture_count
                                    return capture_count


                    # if piece is white triple king
                    if self._board[start_row_num][start_column_num] == 'White_Triple_King':
                        if self._board[start_row_num - 1][start_column_num + 1] is not None or self._board[start_row_num - 1][start_column_num - 1] is not None or self._board[start_row_num + 1][start_column_num + 1] is not None or self._board[start_row_num + 1][start_column_num - 1] is not None:
                            capture_count += 1
                            if self._board[start_row_num - 2][start_column_num + 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num - 1][start_column_num + 1] = None
                                self._board[start_row_num][start_column_num] = None
                                self._board[des_row_num][des_column_num] = 'White_Triple_King'
                                self._white_piece_counter += capture_count
                                return capture_count
                            if self._board[start_row_num - 2][start_column_num - 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num - 1][start_column_num - 1] = None
                                self._board[start_row_num][start_column_num] = None
                                self._board[des_row_num][des_column_num] = 'White_Triple_King'
                                self._white_piece_counter += capture_count
                                return capture_count
                            if self._board[start_row_num + 2][start_column_num - 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num + 1][start_column_num - 1] = None
                                self._board[start_row_num][start_column_num] = None
                                self._board[des_row_num][des_column_num] = 'White_Triple_King'
                                self._white_piece_counter += capture_count
                                return capture_count
                            if self._board[start_row_num + 2][start_column_num + 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num + 1][start_column_num + 1] = None
                                self._board[start_row_num][start_column_num] = None
                                self._board[des_row_num][des_column_num] = 'White_Triple_King'
                                self._white_piece_counter += capture_count
                                return capture_count

                    # if piece is black
                    if self._board[start_row_num][start_column_num] == 'Black':
                        if self._board[start_row_num - 1][start_column_num - 1] and self._board[des_row_num + 1][des_column_num + 1] is not None:
                            capture_count += 1
                            if self._board[start_row_num - 1][start_column_num - 1] == "White_King":
                                self._white_king_counter -= 1
                            self._board[start_row_num - 1][start_column_num - 1] = None
                            self._board[start_row_num][start_column_num] = None
                            if des_row_num == 0:
                                self._board[des_row_num][des_column_num] = "Black_King"
                                self._black_king_counter += 1
                                self._black_piece_counter += capture_count
                                return capture_count
                            else:
                                self._board[des_row_num][des_column_num] = 'Black'
                                self._black_piece_counter += capture_count
                                return capture_count
                        if self._board[start_row_num - 1][start_column_num + 1] and self._board[des_row_num + 1][des_column_num - 1] is not None:
                            capture_count += 1
                            self._board[start_row_num - 1][start_column_num + 1] = None
                            self._board[start_row_num][start_column_num] = None
                            if des_row_num == 0:
                                self._board[des_row_num][des_column_num] = "Black_King"
                                self._black_king_counter += 1
                                self._black_piece_counter += capture_count
                                return capture_count
                            else:
                                self._board[des_row_num][des_column_num] = 'Black'
                                self._black_piece_counter += capture_count
                                return capture_count

                    # if piece is black king
                    if self._board[start_row_num][start_column_num] == 'Black_King':
                        if self._board[start_row_num - 1][start_column_num + 1] is not None or self._board[start_row_num - 1][start_column_num - 1] is not None or self._board[start_row_num + 1][start_column_num + 1] is not None or self._board[start_row_num + 1][start_column_num - 1] is not None:
                            capture_count += 1
                            if self._board[start_row_num - 2][start_column_num + 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num - 1][start_column_num + 1] = None
                                self._board[start_row_num][start_column_num] = None
                                if des_row_num == 0:
                                    self._board[des_row_num][des_column_num] = "Black_Triple_King"
                                    self._black_triple_king_counter += 1
                                    self._black_king_counter -= 1
                                    self._black_piece_counter += capture_count
                                    return capture_count
                                else:
                                    self._board[des_row_num][des_column_num] = 'Black_King'
                                    self._black_piece_counter += capture_count
                                    return capture_count
                            if self._board[start_row_num - 2][start_column_num - 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num - 1][start_column_num - 1] = None
                                self._board[start_row_num][start_column_num] = None
                                if des_row_num == 0:
                                    self._board[des_row_num][des_column_num] = "Black_Triple_King"
                                    self._black_triple_king_counter += 1
                                    self._black_king_counter -= 1
                                    self._black_piece_counter += capture_count
                                    return capture_count
                                else:
                                    self._board[des_row_num][des_column_num] = 'Black_King'
                                    self._black_piece_counter += capture_count
                                    return capture_count
                            if self._board[start_row_num + 2][start_column_num - 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num + 1][start_column_num - 1] = None
                                self._board[start_row_num][start_column_num] = None
                                if des_row_num == 0:
                                    self._board[des_row_num][des_column_num] = "Black_Triple_King"
                                    self._black_triple_king_counter += 1
                                    self._black_king_counter -= 1
                                    self._black_piece_counter += capture_count
                                    return capture_count
                                else:
                                    self._board[des_row_num][des_column_num] = 'Black_King'
                                    self._black_piece_counter += capture_count
                                    return capture_count
                            if self._board[start_row_num + 2][start_column_num + 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num + 1][start_column_num + 1] = None
                                self._board[start_row_num][start_column_num] = None
                                if des_row_num == 0:
                                    self._board[des_row_num][des_column_num] = "Black_Triple_King"
                                    self._black_triple_king_counter += 1
                                    self._black_king_counter -= 1
                                    self._black_piece_counter += capture_count
                                    return capture_count
                                else:
                                    self._board[des_row_num][des_column_num] = 'Black_King'
                                    self._black_piece_counter += capture_count
                                    return capture_count

                    # if piece is black triple king
                    if self._board[start_row_num][start_column_num] == 'Black_Triple_King':
                        if self._board[start_row_num - 1][start_column_num + 1] is not None or self._board[start_row_num - 1][start_column_num - 1] is not None or self._board[start_row_num + 1][start_column_num + 1] is not None or self._board[start_row_num + 1][start_column_num - 1] is not None:
                            capture_count += 1
                            if self._board[start_row_num - 2][start_column_num + 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num - 1][start_column_num + 1] = None
                                self._board[start_row_num][start_column_num] = None
                                self._board[des_row_num][des_column_num] = 'Black_Triple_King'
                                self._black_piece_counter += capture_count
                                return capture_count
                            if self._board[start_row_num - 2][start_column_num - 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num - 1][start_column_num - 1] = None
                                self._board[start_row_num][start_column_num] = None
                                self._board[des_row_num][des_column_num] = 'Black_Triple_King'
                                self._black_piece_counter += capture_count
                                return capture_count
                            if self._board[start_row_num + 2][start_column_num - 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num + 1][start_column_num - 1] = None
                                self._board[start_row_num][start_column_num] = None
                                self._board[des_row_num][des_column_num] = 'Black_Triple_King'
                                self._black_piece_counter += capture_count
                                return capture_count
                            if self._board[start_row_num + 2][start_column_num + 2] == self._board[des_row_num][des_column_num]:
                                self._board[start_row_num + 1][start_column_num + 1] = None
                                self._board[start_row_num][start_column_num] = None
                                self._board[des_row_num][des_column_num] = 'Black_Triple_King'
                                self._black_piece_counter += capture_count
                                return capture_count

    def get_checker_details(self, square_location):
        """Takes square location as a parameter and returns details on the checker piece at that location if
        a checker piece is present at the location"""

        checker_row = square_location[0]
        row_square = square_location[1]

        if square_location[0] > 7 or square_location[1] > 7:
            raise InvalidSquare

        else:
            return self._board[checker_row][row_square]

    def print_board(self):
        """Takes no parameters. Returns the current layout of the board and piece positions on the board in the
        form of an array"""
        return self._board

    def game_winner(self):
        """Takes no parameters. Returns the winner of the game. Returns "Game not ended" if game has not ended"""
        if self._white_piece_counter == 12:
            for players in self._players:
                if self._players[players] == "White":
                    return players

        if self._black_piece_counter == 12:
            for players in self._players:
                if self._players[players] == "Black":
                    return players

        else:
            return "Game has not ended."

    def get_white_king_counter(self):
        return self._white_king_counter

    def get_black_king_counter(self):
        return self._black_king_counter

    def get_white_triple_king_counter(self):
        return self._white_triple_king_counter

    def get_black_triple_king_counter(self):
        return self._black_triple_king_counter


def main():
    game = Checkers()
    Player1 = game.create_player("Adam", "White")
    Player2 = game.create_player("Lucy", "Black")
    game.play_game("Lucy", (5, 0), (4, 1))
    game.play_game("Adam", (2, 1), (3, 2))
    game.print_board()


if __name__ == '__main__':
  main()


class Player:
    """Class that represents the player in the game. Initialized with player name and checker color"""

    def __init__(self, player_name, checker_color):
        self._player_name = player_name
        self._checker_color = checker_color

    def get_king_count(self):
        """Takes no parameters. Returns the number of kings a player has"""

    def get_triple_king_count(self):
        """Takes no parameters. Returns number of triple kings a player has"""

    def get_captured_pieces_count(self):
        """Takes no parameters. Returns number of opponent's pieces that a player has captured"""


# game = Checkers()
# Player1 = game.create_player("Adam", "White")
# Player2 = game.create_player("Lucy", "Black")
# print(Player1)
# print(Player2)
# # print(game._board[2][1])
# print(game.print_board())
# game.play_game("Lucy", (5, 0), (4, 1))
# print(game.print_board())
# game.play_game("Adam", (2, 1), (3, 2))
# print(game.print_board())
# print(game.get_checker_details((4, 1)))
# print(game.game_winner())
# game.play_game("Lucy", (5, 2), (4, 3))
# print(game.print_board())
# game.play_game("Adam", (3, 2), (5, 0))
# print(game.print_board())
# game.play_game("Lucy", (4, 3), (3, 4))
# print(game.print_board())
# game.play_game("Adam", (2, 3), (4, 5))
# print(game.print_board())
# game.play_game("Lucy", (5, 6), (3, 4))
# print(game.print_board())
# game.play_game("Adam", (2, 5), (4, 3))
# print(game.print_board())
# game.play_game("Lucy", (5, 4), (3, 2))
# print(game.print_board())
# game.play_game("Adam", (2, 7), (3, 6))
# print(game.print_board())
# game.play_game("Lucy", (6, 1), (5, 2))
# print(game.print_board())
# game.play_game("Adam", (1, 0), (2, 1))
# print(game.print_board())
# game.play_game("Lucy", (3, 2), (1, 0))
# print(game.print_board())
# game.play_game("Adam", (1, 2), (2, 3))
# print(game.print_board())
# game.play_game("Lucy", (7, 2), (6, 1))
# print(game.print_board())
# game.play_game("Adam", (5, 0), (7, 2))
# print(game.print_board())
# game.play_game("Adam", (7, 2), (5, 4))
# print(game.print_board())
# game.play_game("Lucy", (6, 5), (4, 3))
# print(game.print_board())
# game.play_game("Adam", (0, 1), (1, 2))
# print(game.print_board())
# game.play_game("Lucy", (1, 0), (0, 1))
# print(game.print_board())
# game.play_game("Adam", (1, 2), (2, 1))
# print(game.print_board())
# game.play_game("Lucy", (0, 1), (1, 2))
# print(game.print_board())
# game.play_game("Adam", (2, 3), (3, 4))
# print(game.print_board())
# game.play_game("Lucy", (1, 2), (3, 0))
# print(game.print_board())
# game.play_game("Adam", (3, 4), (4, 5))
# print(game.print_board())
# game.play_game("Lucy", (3, 0), (4, 1))
# print(game.print_board())
# game.play_game("Adam", (0, 3), (1, 2))
# print(game.print_board())
# game.play_game("Lucy", (4, 1), (5, 0))
# print(game.print_board())
# game.play_game("Adam", (1, 2), (2, 1))
# print(game.print_board())
# game.play_game("Lucy", (5, 0), (6, 1))
# print(game.print_board())
# game.play_game("Adam", (2, 1), (3, 0))
# print(game.print_board())
# game.play_game("Lucy", (6, 1), (7, 2))
# print(game.print_board())
# game.play_game("Adam", (1, 4), (2, 3))
# print(game.print_board())
# game.play_game("Lucy", (7, 2), (6, 3))
# print(game.print_board())

# print(game.get_king_count)

# print("White Player Captures:", game._white_piece_counter)
# print("Black Player Captures:", game._black_piece_counter)
# print("White King Count:", game._white_king_counter)
# print("Black King Count:", game._black_king_counter)
# print("White Triple King Count:", game._white_triple_king_counter)
# print("Black Triple King Count:", game._black_triple_king_counter)
# # Player1.get_captured_pieces_count()
# # Player2.get_captured_pieces_count()
# print(game.game_winner())

# game.play_game("Lucy", (4, 3), (3, 4))
# print(game.print_board())
# game.play_game("Adam", (2, 3), (4, 5))
# print(game.print_board())
