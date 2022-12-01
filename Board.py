class Board:
    def __init__(self) -> None:
        self.placeholder: str = "_"
        self.board: list[list[str]] = self.CreateBoard()

    def CreateBoard(self):
        emptyGameBoard: list[list[str]] = [
            [
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
            ],
            [
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
            ],
            [
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
            ],
            [
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
            ],
            [
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
                self.placeholder,
            ],
            ["1", "2", "3", "4", "5", "6", "7"],
        ]

        return emptyGameBoard

    def ShowBoard(self):
        for line in self.board:
            for element in line:
                print(f"|{element}", end="")
            print("|")

    def IsValidTurn(self, element: int):
        element -= 1
        for line in range(len(self.board)):
            fieldIsFree = self.board[line][element] != self.placeholder
            fieldIsValid = self.board[line - 1][element] == self.placeholder
            if fieldIsFree and fieldIsValid:
                return True
        return False

    def AddCoinToBoard(self, element: int, playerMarker: str):
        element -= 1
        for line in range(len(self.board)):
            fieldIsFree = self.board[line][element] != self.placeholder
            fieldIsValid = self.board[line - 1][element] == self.placeholder
            if fieldIsFree and fieldIsValid:
                self.board[line - 1][element] = playerMarker
