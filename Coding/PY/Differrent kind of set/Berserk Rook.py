def berserk_rook(berserker, enemies):
    enemies = list(enemies)
    field_symbol_lst = ["a", "b", "c", "d", "e", "f", "g", "h"]
    field_numb_lst = ["1", "2", "3", "4", "5", "6", "7", "8"]
    lst_total_results = []
    lst_results = []
    wheel = True
    while wheel == True:
        for item in enemies:
            if item[0] == berserker[0]:
                marker = item
            elif item[1] == berserker[1]:
                marker = item

            else:
                break



berserk_rook('d3', {'d6', 'b6', 'c8', 'g4', 'b8', 'g6'})
berserk_rook('a2', {'f6', 'f2', 'a6', 'f8', 'h8', 'h6'})
berserk_rook('a2', {'f6', 'f8', 'f2', 'a6', 'h6'})

# assert berserk_rook('d3', {'d6', 'b6', 'c8', 'g4', 'b8', 'g6'}) == 5, "one path"
# assert berserk_rook('a2', {'f6', 'f2', 'a6', 'f8', 'h8', 'h6'}) == 6, "several paths"
# assert berserk_rook('a2', {'f6', 'f8', 'f2', 'a6', 'h6'}) == 4, "Don't jump through"
