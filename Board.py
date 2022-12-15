class Board:
    def __init__(self) -> None:
        self.place_holder: str = "_"
        self.board: list[list[str]] = self.CreateBoard()

    def create_board(self):
        empty_game_board: list[list[str]] = [
            [
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
            ],
            [
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
            ],
            [
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
            ],
            [
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
            ],
            [
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
                self.place_holder,
            ],
            ["1", "2", "3", "4", "5", "6", "7"],
        ]

        return empty_game_board

    def show_board(self):
        for line in self.board:
            for element in line:
                print(f"|{element}", end="")
            print("|")

    def is_valid_turn(self, element: int):
        element -= 1
        for line in range(len(self.board)):
            field_is_free = self.board[line][element] != self.place_holder
            field_is_valid = self.board[line - 1][element] == self.place_holder
            if field_is_free and field_is_valid:
                return True
        return False

    def add_coin_to_board(self, element: int, player_marker: str):
        element -= 1
        for line in range(len(self.board)):
            field_is_free = self.board[line][element] != self.place_holder
            field_is_valid = self.board[line - 1][element] == self.place_holder
            if field_is_free and field_is_valid:
                self.board[line - 1][element] = player_marker
