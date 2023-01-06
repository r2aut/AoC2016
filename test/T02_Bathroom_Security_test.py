import sys
sys.path.append("src")

import io

from T02_Bathroom_Security import get_digits

def test_get_digits():

    test_keypad = ( ('1','2','3','0'),
                    ('4','5','6','0'),
                    ('7','8','9','0'),
                    ('0','0','0','0')
                  )

    test_str = "ULL\nRRDDD\nLURDL\nUUUUD"

    with io.StringIO(test_str) as file:
        gen = get_digits(test_keypad, (1,1), file)
        assert "".join((gen)) == "1985"
 