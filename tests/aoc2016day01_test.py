""" Day 1: No Time for a Taxicab unit tests """

from src.aoc2016day01 import next_position
from src.aoc2016day01 import manhattan_distance


def test_next_position():
    """ Unit test for calculating next position function """
    assert next_position([0, 0], []) == [0, 0]
    assert next_position([0, 0], ["R2", "L3"]) == [2, 3]
    assert next_position([0, 0], ["R5", "L5", "R5", "R3"]) == [10, 2]
    assert next_position([0, 0], ["R8", "R4", "R4", "R8"], True) == [4, 0]


def test_manhattan_distance():
    """ Unit test for calculating Manheten distance function """
    assert manhattan_distance([0, 0]) == 0
    assert manhattan_distance([2, 3]) == 5
    assert manhattan_distance([3, 2]) == 5
    assert manhattan_distance([-3, 2]) == 5
    assert manhattan_distance([-3, -2]) == 5
