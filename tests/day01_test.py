"""Day 1: No Time for a Taxicab unit tests."""

# ruff: noqa: S101, ANN201, PLR2004

from aoc2016.day01 import Position, Runner


def test_position():
    """Test Position class."""
    assert Position(0, 0).md() == 0
    assert Position(2, 3).md() == 5
    assert Position(-3, 2).md() == 5
    assert Position(-2, -3).md() == 5


def test_runner():
    """Test Runner class."""
    r1 = Runner()
    for cmd in ["R8", "R4", "R4", "R8"]:
        r1.execute(cmd)
    assert r1.position == Position(4, 4)
