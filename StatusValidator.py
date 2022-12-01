from Board import Board


class StatusValidator:
    def __init__(self) -> None:
        pass

    @classmethod
    def GameWasWon(cls, row: list[str], playerSymbol: str) -> bool:
        winnerSequence = playerSymbol * 4
        sequenceString = str.join("", row)
        winSequece = winnerSequence in sequenceString

        return winSequece

    @classmethod
    def IsWin(cls, board: Board, playerMarker: str, column: int):
        horizontalWin = cls.WinByHorizontalPlacement(board, playerMarker)
        verticalWin = cls.WinByVerticalPlacement(board, playerMarker, column)
        diagonalWin = cls.WinByDiagonalPlacement(board, playerMarker)

        return horizontalWin or verticalWin or diagonalWin

    @classmethod
    def WinByHorizontalPlacement(cls, board: Board, playerMarker: str):
        for row in board.board:
            if cls.GameWasWon(row, playerMarker):
                return True
        return False

    @classmethod
    def WinByVerticalPlacement(cls, board: Board, playerMarker: str, column: int):
        sequence = []
        column -= 1
        for row in range(len(board.board)):
            sequence.append(board.board[row][column])
        if cls.GameWasWon(sequence, playerMarker):
            return True

        return False

    @classmethod
    def WinByDiagonalPlacement(cls, board: Board, playerMarker: str):
        boardArray: list[list[str]] = board.board
        columns: int = len(boardArray[0])
        rows: int = len(boardArray) - 1

        for column in range(columns - 3):
            for row in range(rows - 3):
                firstDiagonalPlacement = boardArray[row][column] == playerMarker
                secondDiagonalPlacement = (
                    boardArray[row + 1][column + 1] == playerMarker
                )
                thirdDiagonalPlacement = boardArray[row + 2][column + 2] == playerMarker
                fourthDiagonalPlacement = (
                    boardArray[row + 3][column + 3] == playerMarker
                )
                if (
                    firstDiagonalPlacement
                    and secondDiagonalPlacement
                    and thirdDiagonalPlacement
                    and fourthDiagonalPlacement
                ):
                    return True

        for column in range(columns - 3):
            for row in range(3, rows):
                firstDiagonalPlacement = boardArray[row][column] == playerMarker
                secondDiagonalPlacement = (
                    boardArray[row - 1][column + 1] == playerMarker
                )
                thirdDiagonalPlacement = boardArray[row - 2][column + 2] == playerMarker
                fourthDiagonalPlacement = (
                    boardArray[row - 3][column + 3] == playerMarker
                )
                if (
                    firstDiagonalPlacement
                    and secondDiagonalPlacement
                    and thirdDiagonalPlacement
                    and fourthDiagonalPlacement
                ):
                    return True

        return False
