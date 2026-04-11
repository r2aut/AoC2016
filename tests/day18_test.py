"""Test module for Day 18: Like a Rogue."""

# ruff: noqa: S101, ANN201, PLR2004

from aoc2016.day18 import calc_safe_tiles, char_to_bool, pave_floor


def test_safe_tiles():
    """Test for module aoc2016day18."""
    pattern = char_to_bool(".^^.^.^^^^")
    floor = pave_floor(pattern, 10)
    safe_tiles = calc_safe_tiles(floor)
    assert safe_tiles == 38
