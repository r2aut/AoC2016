import sys
sys.path.append("src")

import io

from T08_Two_Factor_Authentication import Screen
from T08_Two_Factor_Authentication import ScreenProcessor


def test_screen_processor():

    input_text='''rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
'''

    expected_output_text = '''.#..#.#
#.#....
.#.....
'''

    WIDTH = 7
    HIGHT = 3

    with io.StringIO(input_text) as file:
        screen = Screen(WIDTH, HIGHT)
        sp = ScreenProcessor(screen, file)
        while sp.process_command() :
            pass

        assert str(screen) == expected_output_text
        assert screen.lit_pixels() == 6
