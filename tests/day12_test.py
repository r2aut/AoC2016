"""Day 12: Leonardo's Monorail unit tests."""

# ruff: noqa: S101, ANN201, PLR2004

from io import StringIO

from aoc2016.common import Computer, Op
from aoc2016.day12 import read_program

TEST_PROG = R"""cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
"""


def test_op():
    """Unit test for Op class."""
    test_string_1 = "a"
    test_string_2 = "42"
    test_string_3 = "-42"

    op1 = Op(test_string_1)
    assert repr(op1) == "Op('a')"
    assert op1.is_reg_ is True

    op2 = Op(test_string_2)
    assert repr(op2) == "Op('42')"
    assert op2.is_reg_ is False
    assert op2.value_ == 42

    op3 = Op(test_string_3)
    assert repr(op3) == "Op('-42')"
    assert op3.is_reg_ is False
    assert op3.value_ == -42


def test_computer():
    """Unit test for class Computer."""
    with StringIO(TEST_PROG) as file:
        prog = read_program(file)
    comp = Computer(prog)
    assert repr(comp) == "{a = 0, b = 0, c = 0, d = 0, pos = 0}"
