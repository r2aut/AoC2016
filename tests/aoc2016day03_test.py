"""Day 3: Squares With Three Sides unit tests."""

# ruff: noqa: S101, ANN201, PLR2004

import io

from src.aoc2016day03 import count_valid_triangles_variant_1, count_valid_triangles_variant_2

TEST_STR = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
603 403 603
"""


def test_count_valid_triangles_variant_1():
    """Count_valid_triangles_(var 1)."""
    with io.StringIO(TEST_STR) as file:
        assert count_valid_triangles_variant_1(file) == 3


def test_count_valid_triangles_variant_2():
    """Count_valid_triangles_(var 2)."""
    with io.StringIO(TEST_STR) as file:
        assert count_valid_triangles_variant_2(file) == 5
