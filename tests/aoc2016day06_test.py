"""Day 6: Signals and Noise."""

# ruff: noqa: S101, ANN201, D103

from io import StringIO

from src.aoc2016day06 import get_most_least_chars, get_most_least_words, read_columns

TEST = """
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
"""


def test_read_columns():
    data = read_columns(StringIO(TEST))
    if data:
        assert "".join(data[0]) == "ederatsrnnstvvde"


def test_get_most_least_chars():
    data = read_columns(StringIO(TEST))
    if data:
        assert get_most_least_chars(data[0]) == ("e", "a")
        assert get_most_least_chars(data[5]) == ("r", "t")


def test_get_most_least_words():
    data = read_columns(StringIO(TEST))
    if data:
        assert get_most_least_words(data) == ("easter", "advent")
