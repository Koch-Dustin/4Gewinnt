from MainGame import MainGame


def main() -> None:
    game = MainGame()

    game.prepare_game()
    game.play()


if __name__ == "__main__":
    main()
