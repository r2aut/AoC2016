"""Test module for Day 16: Dragon Checksum."""

# ruff: noqa: S101, ANN201

from aoc2016.day16 import calc_check_sum, calc_part_check_sum, calc_random_data, mod_dragon_curve


def test_mod_dragon_curv():
    """Tast cases for mod_dragon_curve function."""
    assert mod_dragon_curve("1") == "100"
    assert mod_dragon_curve("0") == "001"
    assert mod_dragon_curve("11111") == "11111000000"
    assert mod_dragon_curve("111100001010") == "1111000010100101011110000"


def test_calc_random_data():
    """Tast cases for calc_random_data function."""
    assert calc_random_data("1", 3) == "100"
    assert calc_random_data("1", 2) == "10"
    assert calc_random_data("1", 10) == "1000110010"


def test_calc_part_check_sum():
    """Tast cases for calc_part_check_sum function."""
    assert calc_part_check_sum("110010110100") == "110101"


def test_calc_check_sum():
    """Tast cases for calc_check_sum function."""
    assert calc_check_sum("110010110100") == "100"
    assert calc_check_sum("10000011110010000111") == "01100"


def test_all():
    """Tast cases for all calculations."""
    rd = calc_random_data("10000", 20)
    check = calc_check_sum(rd)
    assert check == "01100"
