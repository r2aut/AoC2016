""" Day 2: Bathroom Security unit tests """

import io

from src.aoc2016day02 import get_digits

def test_get_digits():
    """ get_gigits function unit test """

    test_keypad = ( ('1','2','3','0'),
                    ('4','5','6','0'),
                    ('7','8','9','0'),
                    ('0','0','0','0')
                  )

    test_str = "ULL\nRRDDD\nLURDL\nUUUUD"

    with io.StringIO(test_str) as file:
        gen = get_digits(test_keypad, (1,1), file)
        assert "".join((gen)) == "1985"
