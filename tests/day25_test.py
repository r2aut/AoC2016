"""Day 25: Clock Signal."""

# ruff: noqa: S101, ANN201, PLR2004

from io import StringIO

from aoc2016.day25 import part_one, read_program

TEST_STR = """cpy a d
cpy 9 c
cpy 282 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a
jnz 0 0
cpy a b
cpy 0 a
cpy 2 c
jnz b 2
jnz 1 6
dec b
dec c
jnz c -4
inc a
jnz 1 -7
cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
jnz a -19
jnz 1 -21
"""


def test_day25():
    with StringIO(TEST_STR) as file:
        program = read_program(file)
        res = part_one(program)
        assert res == 192
