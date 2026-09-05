"""Day 22: Grid Computing."""

# ruff: noqa: S101, ANN201, PLR2004

from io import StringIO

from aoc2016.day24 import DuctParser, part_one, part_two

TEST_STR = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########
"""


def test_part_one():
    with StringIO(TEST_STR) as file:
        cluster = DuctParser.from_aoc_reader(file)
        res = part_one(cluster)
        assert res == 14


def test_part_two():
    with StringIO(TEST_STR) as file:
        cluster = DuctParser.from_aoc_reader(file)
        res = part_two(cluster)
        assert res == 20
