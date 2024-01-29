def safe_pawns(pawns: set) -> int:
    # add your code here
    return 0


print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

assert safe_pawns({"f4", "d4", "e3", "b4", "g5", "d2", "c3"}) == 6
assert safe_pawns({"f4", "c4", "b4", "e4", "g4", "d4", "e5"}) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
