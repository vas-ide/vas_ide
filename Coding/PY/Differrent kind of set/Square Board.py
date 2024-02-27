from typing import Tuple

Coordinate = Tuple[int, int]


def square_board(side: int, token: int, steps: int) -> Coordinate:
    game_lst = [item for item in range(side * 4 - 4)]
    matrix = []
    possition = possition_analiz(game_lst, steps, token)

    create_init_matrix(matrix, side)

    create_full_matrix(game_lst, matrix, side)

    [print(f"{item}") for item in matrix]
    for num, item in enumerate(matrix):
        for num_add, item_add in enumerate(item):
            if item_add == possition:
                print(f"{num}: {num_add}")
                return (num, num_add)


def possition_analiz(game_lst, steps, token):
    possition = 0
    if abs(steps) + abs(token) < len(game_lst):
        possition = game_lst[token + steps]
    elif abs(steps) + abs(token) == len(game_lst):
        possition = 0
    elif steps % len(game_lst) == 0:
        possition = game_lst[token]
    elif steps > len(game_lst):
        for item in range(steps):
            if abs(steps) > len(game_lst):
                if steps > 0:
                    steps -= len(game_lst)
                else:
                    steps += len(game_lst)
            else:
                possition = game_lst[token + steps]
                break
    elif abs(steps) + abs(token) > len(game_lst):
        possition = game_lst[token + (steps - len(game_lst))]
    return possition


def create_full_matrix(game_lst, matrix, side):
    for num, item in enumerate(matrix):
        if num == 0:
            first_elem = game_lst[len(game_lst) // 2:]
            first_elem = first_elem[:side]
            matrix[0] = first_elem
            last_elem = game_lst[side - 1::-1]
            matrix[len(matrix) - 1] = last_elem
            game_lst = game_lst[side:]
            [game_lst.remove(item) for item in first_elem if item in game_lst]
        elif len(game_lst) == 2 and num != len(matrix) - 1:
            matrix[num][0] = game_lst[0]
            matrix[num][-1] = game_lst[1]
        elif len(game_lst) != 2 and num != len(matrix) - 1:
            start = game_lst[len(game_lst) // 2 - 1]
            end = game_lst[len(game_lst) // 2]
            matrix[num][0] = start
            matrix[num][-1] = end
            game_lst.remove(start)
            game_lst.remove(end)


def create_init_matrix(matrix, side):
    for item in range(side):
        elem_lst = []
        for elem in range(side):
            elem_lst.append(f"_")
        matrix.append(elem_lst)



square_board(10,33,34)
# assert square_board(6,pillow_ticket,40) == (0, 3)
# assert square_board(11, 18, 56) == (4,10)
# assert square_board(7, 12, 12) == (6, 6)
# assert square_board(4, 1, 4) == (1, 0)
# assert square_board(6, 2, -3) == (4, 5)
