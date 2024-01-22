





def checkio(game_result: list[str]) -> str:
    if (game_result[0][0] == "X" and game_result[1][0] == "X" and game_result[2][0] == "X" or
        game_result[0][1] == "X" and game_result[1][1] == "X" and game_result[2][1] == "X" or
        game_result[0][2] == "X" and game_result[1][2] == "X" and game_result[2][2] == "X" or
        game_result[0][0] == "X" and game_result[0][1] == "X" and game_result[0][2] == "X" or
        game_result[1][0] == "X" and game_result[1][1] == "X" and game_result[1][2] == "X" or
        game_result[2][0] == "X" and game_result[2][1] == "X" and game_result[2][2] == "X" or
        game_result[0][0] == "X" and game_result[1][1] == "X" and game_result[2][2] == "X" or
        game_result[0][2] == "X" and game_result[1][1] == "X" and game_result[2][0] == "X"):
        print(f"X")
        return f"X"
    elif (game_result[0][0] == "O" and game_result[1][0] == "O" and game_result[2][0] == "O" or
        game_result[0][1] == "O" and game_result[1][1] == "O" and game_result[2][1] == "O" or
        game_result[0][2] == "O" and game_result[1][2] == "O" and game_result[2][2] == "O" or
        game_result[0][0] == "O" and game_result[0][1] == "O" and game_result[0][2] == "O" or
        game_result[1][0] == "O" and game_result[1][1] == "O" and game_result[1][2] == "O" or
        game_result[2][0] == "O" and game_result[2][1] == "O" and game_result[2][2] == "O" or
        game_result[0][0] == "O" and game_result[1][1] == "O" and game_result[2][2] == "O" or
        game_result[0][2] == "O" and game_result[1][1] == "O" and game_result[2][0] == "O"):
        print(f"O")
        return f"O"
    else:
        print(f"D")
        return f"D"





checkio(["X.O", "XX.", "XOO"])              #"X"
checkio(["OO.", "XOX", "XOX"])              #"O"
checkio(["OOX", "XXO", "OXX"])              #"D"
checkio(["O.X", "XX.", "XOO"])              #"X"
#
























