"""Day 11: Radioisotope Thermoelectric Generators."""

# ruff: noqa: S101, ANN201, PLR2004

from io import StringIO

from aoc2016.day11 import read_data

TEST_DATA = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
"""


def test_day11():
    """Test day11."""
    with StringIO(TEST_DATA) as file:
        fac = read_data(file)
        res = fac.move_all()
        assert res == 11
