"""Day 3: Squares With Three Sides."""

from pathlib import Path
from typing import TYPE_CHECKING

from rich.console import Console

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from collections.abc import Iterable
    from io import TextIOBase


def is_a_valid_triangle(sides: Iterable) -> bool:
    """Decide if the triple is a valid triangle."""
    _sides = list(sides)
    if len(_sides) == 3:  # noqa: PLR2004
        _sides.sort()
        if _sides[2] < _sides[0] + _sides[1]:
            return True
    return False


@stopwatch
def count_valid_triangles_variant_1(file: TextIOBase) -> int:
    """Count_valid_triangles_variant_1 for the 1st phase."""
    counter = 0
    for line in file:
        sides = [int(x) for x in line.strip().split()]
        if is_a_valid_triangle(sides):
            counter += 1
    return counter


@stopwatch
def count_valid_triangles_variant_2(file: TextIOBase) -> int:
    """Count_valid_triangles_variant_2 for the 2nd phase."""
    counter = 0
    eof = False
    while not eof:
        triple_lines: list[list[int]] = []
        for _ in range(3):
            line = file.readline().strip()
            if line:
                triple_lines.append([int(x) for x in line.split()])
            else:
                eof = True
                break  # break for circle
        if triple_lines:
            for i in range(3):
                sides: list[int] = []
                for j in range(3):
                    sides.append(triple_lines[j][i])  # noqa: PERF401

                if is_a_valid_triangle(sides):
                    counter += 1
    return counter


@stopwatch
def main():  # noqa: ANN201
    file_name = "puzzles/day03.txt"

    with Path(file_name).open(encoding="utf-8") as file:
        res_1 = count_valid_triangles_variant_1(file)

    with Path(file_name).open(encoding="utf-8") as file:
        res_2 = count_valid_triangles_variant_2(file)

    rc = Console()
    rc.print(f"{P1} =  [green]{res_1}[/green]")
    rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
