""" Day 21: Scrambled Letters and Hash unit tests """

from io import StringIO
from src.aoc2016day21 import Scrambler, process_commands

TEST_STR = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
"""

TEST_PASSWORD = "abcde"


def test_aoc2016day21():
    scr = Scrambler(TEST_PASSWORD)
    with StringIO(TEST_STR) as file:
        assert process_commands(file, scr) == "decab"
