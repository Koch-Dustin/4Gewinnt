from Player import Player
from Board import Board
from StatusValidator import StatusValidator
import os

clear = lambda: os.system("clear")


class MainGame:
    def __init__(self) -> None:
        self.firstPlayer: Player = Player()
        self.secondPlayer: Player = Player()
        self.board: Board = Board()
        self.round = 0

    def PrepareGame(self):
        self.firstPlayer.name = self.GetUserName("Player 1")
        self.firstPlayer.marker = "X"

        self.secondPlayer.name = self.GetUserName("Player 2")
        self.secondPlayer.marker = "O"

        clear()

    def Round(self):
        self.round += 1
        if self.round > 21:
            return Player()
        if not self.firstPlayer.won:
            self.Turn(self.secondPlayer)

        if not self.secondPlayer.won:
            self.Turn(self.firstPlayer)

        if self.firstPlayer.won:
            return self.firstPlayer

        if self.secondPlayer.won:
            return self.secondPlayer

    def Play(self):
        while True:
            player = self.Round()

            if player is not None:
                break

        if player.name == "":
            print("Tie!")
        else:
            print(f"{player.name} has won the Game!")
            self.board.ShowBoard()

    def GetRowInput(self, playerName):
        print()
        while True:
            rowInputAsString = input(f"{playerName}: Select a row to put your coin: ")
            clear()
            try:
                rowInputAsInt = int(rowInputAsString)
                minimumRowNumber = 1
                maximumRowNumber = 7

                if (
                    rowInputAsInt >= minimumRowNumber
                    and rowInputAsInt <= maximumRowNumber
                ):
                    return rowInputAsInt
                else:
                    print(f"Your input '{rowInputAsInt}' is invalid. Try again!")
            except ValueError:
                print("Please enter a number")

    def Turn(self, player: Player) -> Player:
        print(f"Round: {self.round}")
        self.board.ShowBoard()

        while True:
            row: int = self.GetRowInput(player.name)
            if self.board.IsValidTurn(row):
                self.board.AddCoinToBoard(row, player.marker)

                if StatusValidator.IsWin(self.board, player.marker, row):
                    player.won = True
                break

            else:
                print(f"Your cant put your coin in row '{row}'. Try again!")

    def GetUserName(self, playerName: str) -> str:
        userName: str = input(f"{playerName}: Please enter your name: ")

        if userName.isalpha() and len(userName) > 0:
            return userName
        else:
            print(f"Your input '{userName}' is unvalid. Try again!")
