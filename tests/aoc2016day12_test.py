""" Day 12: Leonardo's Monorail unit tests """

from io import StringIO

from src.aoc2016day12 import read_program
from src.aoc2016day12 import Op
from src.aoc2016day12 import Computer


TEST_PROG = R"""cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
"""

# def op(x):
#     return Op(x)

def test_op():
    """ Unit test for Op class"""
    test_string_1 = "a"
    test_string_2 = "42"
    test_string_3 = "-42"

    op1 = Op(test_string_1)
    assert repr(op1) == "Op('a')"
    assert op1.is_reg_ is True
    assert op1.value_ is None

    op2 = Op(test_string_2)
    assert repr(op2) == "Op('42')"
    assert op2.is_reg_ is False
    assert op2.value_ == 42

    op3 = Op(test_string_3)
    assert repr(op3) == "Op('-42')"
    assert op3.is_reg_ is False
    assert op3.value_ == -42



def test_read_program():
    """ unit test for read_program function """
    with StringIO(TEST_PROG) as file:
        prog = read_program(file)
    assert repr(prog) == "[['cpy', Op('41'), Op('a')], ['inc', Op('a')], ['inc', Op('a')], "+ \
        "['dec', Op('a')], ['jnz', Op('a'), Op('2')], ['dec', Op('a')]]"


def test_computer():
    """ unit test for class Computer """
    comp = Computer(TEST_PROG)
    assert repr(comp) == "{a = 0, b = 0, c = 0, d = 0, pos = 0}"
    # comp.execute_program()
    # assert repr(comp) == "{a = 42, b = 0, c = 0, d = 0, pos = 6}"
