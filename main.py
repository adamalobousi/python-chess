import src.game

example_game = [
        "d2d4","g8f6","g1f3","g7g6",
        "g2g3","f8g7","f1g2","e8g8",
        "e1g1","d7d6","b1c3","b8d7",
        "b2b3","e7e5","d4e5","d6e5",
        "e2e4","f8e8","c1a3","c7c6",
        "a3d6","d8a5","d1d3","e8e6",
        "b3b4","a5a3","d6c7","a3b4",
        "a1b1","b4e7","f1d1","f6e8",
        "c7a5","e6d6","d3e2","d6d1",
        "e2d1","g7f8","f3d2","e7a3",
        "d2c4","a3c5","g2f1","b7b5",
        "c4d2","c5a3","d2b3","d7c5"
        ]

def main():
    game_instance = src.game.Game()
    print("Choose a game mode:")
    print("1. Example game")
    print("2. Interactive game")

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        game_instance.play_automated_round(example_game)
    elif choice == '2':
        game_instance.play_round()
    else: print("Invalid choice. Exiting...")



if __name__ == "__main__":
    main()