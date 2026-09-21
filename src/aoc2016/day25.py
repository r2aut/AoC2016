"""Day 25: Clock Signal."""

from copy import deepcopy
from pathlib import Path
from typing import TYPE_CHECKING

from rich.console import Console

from aoc2016.common import P1, Command, Computer, stopwatch

if TYPE_CHECKING:
    from io import TextIOBase


def read_program(file: TextIOBase) -> list[Command]:
    """Read programm from file."""
    program: list[Command] = []
    for line in file:
        if line:
            parts = line.split()
            cmd = parts[0]
            op1 = parts[1] if len(parts) >= 2 else None  # noqa: PLR2004
            op2 = parts[2] if len(parts) >= 3 else None  # noqa: PLR2004
            command = Command(cmd, op1, op2)
            program.append(command)
    return program


@stopwatch
def part_one(program: list[Command]) -> int:
    a_value = 0
    while True:
        prog = deepcopy(program)
        comp = Computer(prog)
        comp.set_reg("a", a_value)
        comp.execute_program_qsize(qsize=10)
        res = comp.get_output(10)
        if res == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]:
            return a_value
        a_value += 1


def main() -> None:

    with Path("puzzles/day25.txt").open(encoding="utf-8") as file:
        program = read_program(file)

    rc = Console()

    res_1 = part_one(program)
    rc.print(f"{P1} =  [green]{res_1}[/green]")


if __name__ == "__main__":
    main()
