"""Day 2: Bathroom Security unit tests."""

# ruff: noqa: S101, ANN201

import io

from src.aoc2016day02 import Position, get_digits


def test_get_digits1():
    """Get_gigits function (var 1)."""
    test_keypad1 = (("1", "2", "3", "0"), ("4", "5", "6", "0"), ("7", "8", "9", "0"), ("0", "0", "0", "0"))

    test_str = "ULL\nRRDDD\nLURDL\nUUUUD"

    with io.StringIO(test_str) as file:
        dig = get_digits(test_keypad1, Position(1, 1), file)
        assert dig == "1985"


def test_get_digits2():
    """Get_gigits function (var 2)."""
    test_keypad2 = (
        ("0", "0", "1", "0", "0"),
        ("0", "2", "3", "4", "0"),
        ("5", "6", "7", "8", "9"),
        ("0", "A", "B", "C", "0"),
        ("0", "0", "D", "0", "0"),
    )
    test_str = "ULL\nRRDDD\nLURDL\nUUUUD"

    with io.StringIO(test_str) as file:
        dig = get_digits(test_keypad2, Position(0, 2), file)
        assert dig == "5DB3"
