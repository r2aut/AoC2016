"""Day 2: Bathroom Security."""

from pathlib import Path
from typing import TYPE_CHECKING, NamedTuple

from rich.console import Console

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from io import TextIOBase

type KeyPad = tuple

keypad1 = (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"))

keypad2 = (
    ("0", "0", "1", "0", "0"),
    ("0", "2", "3", "4", "0"),
    ("5", "6", "7", "8", "9"),
    ("0", "A", "B", "C", "0"),
    ("0", "0", "D", "0", "0"),
)


class Position(NamedTuple):  # (x, y), y increased down
    """Position."""

    x: int
    y: int


@stopwatch
def get_digits(keypad: KeyPad, start_pos: Position, file: TextIOBase) -> str:
    """Get_digits function."""
    cur_pos = start_pos
    result = []
    for command_line in file:
        for command in command_line.strip():
            match command:
                case "R":
                    next_pos = Position(cur_pos.x + 1, cur_pos.y)
                case "D":
                    next_pos = Position(cur_pos.x, cur_pos.y + 1)
                case "L":
                    next_pos = Position(cur_pos.x - 1, cur_pos.y)
                case "U":
                    next_pos = Position(cur_pos.x, cur_pos.y - 1)
                case _:
                    raise ValueError
            if (
                0 <= next_pos.y < len(keypad)
                and 0 <= next_pos.x < len(keypad[next_pos.y])
                and keypad[next_pos.y][next_pos.x] != "0"
            ):
                cur_pos = next_pos
        result.append(keypad[cur_pos.y][cur_pos.x])
    return "".join(result)


@stopwatch
def main() -> None:
    filename = "puzzles/day02.txt"

    with Path(filename).open(encoding="utf-8") as file:
        res_1 = get_digits(keypad1, Position(1, 1), file)

    with Path(filename).open(encoding="utf-8") as file:
        res_2 = get_digits(keypad2, Position(1, 1), file)

        rc = Console()
        rc.print(f"{P1} =  [green]{res_1}[/green]")
        rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
