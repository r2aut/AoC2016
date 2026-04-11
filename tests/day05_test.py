"""Day 5: How About a Nice Game of Chess."""

# ruff: noqa: S101, ANN201

from aoc2016.day05 import hash_gen, part_1, part_2


def test_hash_gen():
    """Test hash generator."""
    hasher = hash_gen("abc", "00000")
    assert next(hasher) == "00000155f8105dff7f56ee10fa9b9abd"
    assert next(hasher) == "000008f82c5b3924a1ecbebf60344e00"
    assert next(hasher) == "00000f9a2c309875e05c5a5d09f1b8c4"


def test_part_1():
    """Test Part One."""
    assert part_1("abc", "00000", 8) == "18f47a30"


def test_part_2():
    """Test Part Two."""
    assert part_2("abc", "00000", 8) == "05ace8e3"
