from typing import Tuple
Coordinate = Tuple[int, int]


def square_board(side: int, token: int, steps: int) -> Coordinate:
    game_lst = [item for item in range(side * 4 - 4)]
    possition = game_lst[token + steps]
    row = None
    line = None
    print(game_lst, len(game_lst), possition)

square_board(4, 1, 4)
square_board(6, 2, -3)
# assert square_board(4, 1, 4) == (1, 0)
# assert square_board(6, 2, -3) == (4, 5)

