"""Test module for Day 20: Firewall Rules."""

# ruff: noqa: S101, ANN201, PLR2004

from io import StringIO

from aoc2016.day20 import calc_allowed_number, min_allowed_num, read_blacklist, unite_blacklist

TEST_DATA = """5-8
0-2
4-7
"""


def test_min_allowed_number():
    """Test cases for min_allowed_number function."""
    with StringIO(TEST_DATA) as file:
        blacklist = read_blacklist(file)
    blacklist.sort()
    blacklist = unite_blacklist(blacklist)
    assert min_allowed_num(0, 10, blacklist) == 3


def test_calc_allowed_number():
    """Test cases for calc_allowed_number."""
    with StringIO(TEST_DATA) as file:
        blacklist = read_blacklist(file)
    blacklist.sort()
    blacklist = unite_blacklist(blacklist)
    assert calc_allowed_number(0, 10, blacklist) == 2
