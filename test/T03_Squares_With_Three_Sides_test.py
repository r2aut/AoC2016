import sys
sys.path.append("src")

import io

from T03_Squares_With_Three_Sides import count_valid_triangles_variant_1
from T03_Squares_With_Three_Sides import count_valid_triangles_variant_2

test_str = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
603 403 603
"""

def test_count_valid_triangles_variant_1():
    with io.StringIO(test_str) as file:
        assert count_valid_triangles_variant_1(file) == 3

def test_count_valid_triangles_variant_2():
    with io.StringIO(test_str) as file:
        assert count_valid_triangles_variant_2(file) == 5
