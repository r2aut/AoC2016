"""Day 8: Two-Factor Authentication unit tests."""

# ruff: noqa: S101, ANN201, PLR2004

from io import StringIO

from aoc2016.day08 import Screen, ScreenProcessor

TEST_INPUT = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
"""

EXPECTED_OUTPUT = """.#..#.#
#.#....
.#.....
"""


def test_screen_processor():
    """Test screen_processor."""
    width = 7
    hight = 3

    with StringIO(TEST_INPUT) as file:
        screen = Screen(width, hight)
        sp = ScreenProcessor(screen, file)
        sp.process_all_commands()

        assert screen.count_lit_pixels() == 6
        assert str(screen) == EXPECTED_OUTPUT
