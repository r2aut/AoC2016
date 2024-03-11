""" Day 8: Two-Factor Authentication unit tests """

# import sys
# sys.path.append("src")

import io

from src.aoc2016day08 import Screen
from src.aoc2016day08 import ScreenProcessor


def test_screen_processor():
    """ screen_processor function unit test """

    input_text='''rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
'''

    expected_output_text = '''.#..#.#
#.#....
.#.....
'''

    width = 7
    hight = 3

    with io.StringIO(input_text) as file:
        screen = Screen(width, hight)
        sp = ScreenProcessor(screen, file)
        while sp.process_command() :
            pass

        assert str(screen) == expected_output_text
        assert screen.lit_pixels() == 6
