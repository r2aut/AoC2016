"""Day 9: Explosives in Cyberspace."""

# ruff: noqa: S101, ANN201, PLR2004

from aoc2016.day09 import get_dec_length


def test_get_dec_length_1():
    """Test decompression function without recursion."""
    assert get_dec_length("ADVENT") == len("ADVENT")
    assert get_dec_length("A(1x5)BC") == len("ABBBBBC")
    assert get_dec_length("(3x3)XYZ") == len("XYZXYZXYZ")
    assert get_dec_length("A(2x2)BCD(2x2)EFG") == len("ABCBCDEFEFG")
    assert get_dec_length("(6x1)(1x3)A") == len("(1x3)A")
    assert get_dec_length("X(8x2)(3x3)ABCY") == len("X(3x3)ABC(3x3)ABCY")


def test_get_dec_length_2():
    """Test decompression function with recursion."""
    assert get_dec_length("(3x3)XYZ", recursively=True) == len("XYZXYZXYZ")
    assert get_dec_length("X(8x2)(3x3)ABCY", recursively=True) == len("XABCABCABCABCABCABCY")
    assert get_dec_length("(27x12)(20x12)(13x14)(7x10)(1x12)A", recursively=True) == 241920
    assert get_dec_length("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", recursively=True) == 445
