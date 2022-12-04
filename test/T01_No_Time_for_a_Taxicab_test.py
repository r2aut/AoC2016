import sys
sys.path.append("src")


from T01_No_Time_for_a_Taxicab import next_position
from T01_No_Time_for_a_Taxicab import Manhattan_distance


def test_next_position():
    assert next_position([0, 0], []) == [0, 0]
    assert next_position([0, 0], ["R2", "L3"]) == [2, 3]
    assert next_position([0, 0], ["R5", "L5", "R5", "R3"]) == [10, 2]
    assert next_position([0, 0], ["R8", "R4", "R4", "R8"], True) == [4, 0]


def test_Manhattan_distance():
    assert Manhattan_distance([0, 0]) == 0
    assert Manhattan_distance([2, 3]) == 5
    assert Manhattan_distance([3, 2]) == 5
    assert Manhattan_distance([-3, 2]) == 5
    assert Manhattan_distance([-3, -2]) == 5
