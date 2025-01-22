""" Test module for Day 17: Two Steps Forward """

from src.aoc2016day18 import char_to_bool, pave_floor, calc_safe_tiles


def test_safe_tiles():
    """Test for module aoc2016day18"""
    pattern = char_to_bool(".^^.^.^^^^")
    floor = pave_floor(pattern, 10)
    safe_tiles = calc_safe_tiles(floor)
    assert safe_tiles == 38
