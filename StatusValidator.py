from Board import Board


class StatusValidator:
    def __init__(self) -> None:
        pass

    @classmethod
    def game_was_won(cls, row: list[str], player_symbol: str) -> bool:
        winner_sequence = player_symbol * 4
        sequence_string = str.join("", row)
        win_sequece = winner_sequence in sequence_string

        return win_sequece

    @classmethod
    def is_win(cls, board: Board, player_marker: str, column: int):
        horizontal_win = cls.win_by_horizontal_placement(board, player_marker)
        vertical_win = cls.win_by_vertical_placement(board, player_marker, column)
        diagonal_win = cls.win_by_diagonal_placement(board, player_marker)

        return horizontal_win or vertical_win or diagonal_win

    @classmethod
    def win_by_horizontal_placement(cls, board: Board, player_marker: str):
        for row in board.board:
            if cls.game_was_won(row, player_marker):
                return True
        return False

    @classmethod
    def win_by_vertical_placement(cls, board: Board, player_marker: str, column: int):
        sequence = []
        column -= 1
        for row in range(len(board.board)):
            sequence.append(board.board[row][column])
        if cls.game_was_won(sequence, player_marker):
            return True

        return False

    @classmethod
    def win_by_diagonal_placement(cls, board: Board, player_marker: str):
        board_array: list[list[str]] = board.board
        columns: int = len(board_array[0])
        rows: int = len(board_array) - 1

        for column in range(columns - 3):
            for row in range(rows - 3):
                first_diagonal_placement = board_array[row][column] == player_marker
                second_diagonal_placement = (
                    board_array[row + 1][column + 1] == player_marker
                )
                third_diagonal_placement = (
                    board_array[row + 2][column + 2] == player_marker
                )
                fourth_diagonal_placement = (
                    board_array[row + 3][column + 3] == player_marker
                )
                if (
                    first_diagonal_placement
                    and second_diagonal_placement
                    and third_diagonal_placement
                    and fourth_diagonal_placement
                ):
                    return True

        for column in range(columns - 3):
            for row in range(3, rows):
                first_diagonal_placement = board_array[row][column] == player_marker
                second_diagonal_placement = (
                    board_array[row - 1][column + 1] == player_marker
                )
                third_diagonal_placement = (
                    board_array[row - 2][column + 2] == player_marker
                )
                fourth_diagonal_placement = (
                    board_array[row - 3][column + 3] == player_marker
                )
                if (
                    first_diagonal_placement
                    and second_diagonal_placement
                    and third_diagonal_placement
                    and fourth_diagonal_placement
                ):
                    return True

        return False
