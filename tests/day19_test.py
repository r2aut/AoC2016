"""Day 19: An Elephant Named Joseph."""

# ruff: noqa: S101, ANN201, PLR2004

from aoc2016.day19 import calc_part_one, calc_part_two

DATA = 5


def test_part_one():
    res = calc_part_one(DATA)
    assert res == 3


def test_part_two():
    res = calc_part_two(DATA)
    assert res == 2
