"""Day 7: Internet Protocol Version 7."""

# ruff: noqa: S101, ANN201, PLR2004

from io import StringIO

from aoc2016.day07 import part_1, part_2, read_addresses

TEST_1 = """
abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
"""


def test_part_1():
    """Test scan_line_for_tls."""
    data = read_addresses(StringIO(TEST_1))
    assert part_1(data) == 2


TEST_2 = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb
"""


def test_part_2():
    """Test scan_line_for_ssl."""
    data = read_addresses(StringIO(TEST_2))
    assert part_2(data) == 3
