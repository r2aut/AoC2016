"""Day 23: Safe Cracking."""

# ruff: noqa: S101, ANN201, PLR2004

from io import StringIO

from aoc2016.day23 import part_one, read_program

TEST_STR = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
"""


def test_day23():
    with StringIO(TEST_STR) as file:
        program = read_program(file)
        res = part_one(program)
        assert res == 3
