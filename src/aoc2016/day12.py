"""Day 12: Leonardo's Monorail."""

from pathlib import Path
from typing import TYPE_CHECKING

from rich.console import Console

from aoc2016.common import P1, P2, Command, Computer, stopwatch

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
    comp = Computer(program)
    comp.execute_program()
    return comp.a_


@stopwatch
def part_two(program: list[Command]) -> int:
    comp = Computer(program)
    comp.set_reg("c", 1)
    comp.execute_program()
    return comp.a_


@stopwatch
def main() -> None:

    with Path("puzzles/day12.txt").open(encoding="utf-8") as file:
        program = read_program(file)

    rc = Console()

    res_1 = part_one(program)
    rc.print(f"{P1} =  [green]{res_1}[/green]")

    res_2 = part_two(program)
    rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
