""" Test module for Day 20: Firewall Rules """

from io import StringIO
from src.aoc2016day20 import read_blacklist
from src.aoc2016day20 import unite_blacklist
from src.aoc2016day20 import min_allowed_num
from src.aoc2016day20 import calc_allowed_number

TEST_DATA = """5-8
0-2
4-7
"""


def test_min_allowed_number():
    """Tast cases for min_allowed_number function"""

    with StringIO(TEST_DATA) as file:
        blacklist = read_blacklist(file)
    blacklist.sort()
    blacklist = unite_blacklist(blacklist)
    assert min_allowed_num(0, 10, blacklist) == 3


def test_calc_allowed_number():
    """Tast cases for calc_allowed_number"""

    with StringIO(TEST_DATA) as file:
        blacklist = read_blacklist(file)
    blacklist.sort()
    blacklist = unite_blacklist(blacklist)
    assert calc_allowed_number(0, 10, blacklist) == 2
