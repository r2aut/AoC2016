"""Day 9: Explosives in Cyberspace unit tests."""

# ruff: noqa: S101, ANN201, PLR2004

from io import StringIO

from aoc2016.day10 import process

TEST_DATA = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""


def test_process():
    """Test process function."""
    with StringIO(TEST_DATA) as file:
        bot, mult = process(file, (2, 5))
        assert bot == 2
        assert mult == 30
