from typing import Set, Tuple, List, Dict


def power_plants(network: Set[Tuple[str, str]], ranges: List[int]) -> Dict[str, int]:
    pass



power_plants({("A", "B"), ("B", "C")}, [1])
# == {"B": 1}
power_plants({("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")}, [2])
# == {"C": 2}
power_plants({("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F")}, [1, 1])
# == {"B": 1, "E": 1}
power_plants({("A", "B"), ("B", "C"), ("A", "D"), ("B", "E")}, [1, 0])
# == {"B": 1, "D": 0, }


# assert power_plants({("A", "B"), ("B", "C")}, [1]) == {"B": 1}
# assert power_plants({("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")}, [2]) == {"C": 2}
# assert power_plants({("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F")}, [1, 1]) == {"B": 1, "E": 1}
# assert power_plants({("A", "B"), ("B", "C"), ("A", "D"), ("B", "E")}, [1, 0]) == {"B": 1, "D": 0, }
