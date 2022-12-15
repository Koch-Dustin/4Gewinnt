import os
from Player import Player
from Board import Board
from StatusValidator import StatusValidator

clear = lambda: os.system("clear")


class MainGame:
    def __init__(self) -> None:
        self.first_player: Player = Player()
        self.second_player: Player = Player()
        self.board: Board = Board()
        self.round_number = 0

    def prepare_game(self):
        self.first_player.name = self.get_user_name("Player 1")
        self.first_player.marker = "X"

        self.second_player.name = self.get_user_name("Player 2")
        self.second_player.marker = "O"

        clear()

    def round(self):
        self.round_number += 1
        if self.round_number > 21:
            return Player()
        if not self.first_player.won:
            self.turn(self.second_player)

        if not self.second_player.won:
            self.turn(self.first_player)

        if self.first_player.won:
            return self.first_player

        if self.second_player.won:
            return self.second_player

    def play(self):
        while True:
            player = self.round()

            if player is not None:
                break

        if player.name == "":
            print("Tie!")
        else:
            print(f"{player.name} has won the game!")
            self.board.show_board()

    def get_row_input(self, player_name):
        while True:
            row_inpput_as_string = input(
                f"{player_name}: Select a row to put your coin: "
            )
            clear()
            try:
                row_input_as_int = int(row_inpput_as_string)
                minimum_row_number = 1
                maximum_row_number = 7

                if (
                    row_input_as_int >= minimum_row_number
                    and row_input_as_int <= maximum_row_number
                ):
                    return row_input_as_int
                else:
                    print(f"Your input '{row_input_as_int}' is invalid. Try again!")
            except ValueError:
                print("Please enter a number")

    def turn(self, player: Player) -> Player:
        print(f"Round: {self.round}")
        self.board.show_board()

        while True:
            row: int = self.get_row_input(player.name)
            if self.board.is_valid_turn(row):
                self.board.add_coin_to_board(row, player.marker)

                if StatusValidator.is_win(self.board, player.marker, row):
                    player.won = True
                break

            else:
                print(f"Your can't put your coin in row '{row}'. Try again!")

    def get_user_name(self, player_name: str) -> str:
        user_name: str = input(f"{player_name}: Please enter your name: ")

        if user_name.isalpha() and len(user_name) > 0:
            return user_name
        else:
            print(f"Your input '{user_name}' is unvalid. Try again!")
