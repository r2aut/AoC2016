"""Day 1: No Time for a Taxicab unit tests."""

# ruff: noqa: S101, ANN201, PLR2004

from src.aoc2016day01 import Position, Runner


def test_position():
    """Test Position class."""
    assert Position(0, 0).manhattan_distance() == 0
    assert Position(2, 3).manhattan_distance() == 5
    assert Position(-3, 2).manhattan_distance() == 5
    assert Position(-2, -3).manhattan_distance() == 5


def test_runner():
    """Test Runner class."""
    r1 = Runner()
    for cmd in ["R8", "R4", "R4", "R8"]:
        r1.execute(cmd)
    assert r1.position == Position(4, 4)
