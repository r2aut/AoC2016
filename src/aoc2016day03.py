"""Day 3: Squares With Three Sides."""

from collections.abc import Iterable
from io import TextIOBase
from pathlib import Path

from rich.console import Console


def is_a_valid_triangle(sides: Iterable) -> bool:
    """Decide if the triple is a valid triangle."""
    _sides = list(sides)
    if len(_sides) == 3:  # noqa: PLR2004
        _sides.sort()
        if _sides[2] < _sides[0] + _sides[1]:
            return True
    return False


def count_valid_triangles_variant_1(file: TextIOBase) -> int:
    """Count_valid_triangles_variant_1 for the 1st phase."""
    counter = 0
    for line in file:
        sides = [int(x) for x in line.strip().split()]
        if is_a_valid_triangle(sides):
            counter += 1
    return counter


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


def main():  # noqa: ANN201, D103
    rc = Console()

    with Path(r"puzzles/aoc2016day03_data.txt").open(encoding="utf-8") as file:
        res_1 = count_valid_triangles_variant_1(file)
        rc.print(f"[cyan](Part One)[/cyan] It is possible [green]{res_1}[/green] triangles.")

    with Path(r"puzzles/aoc2016day03_data.txt").open(encoding="utf-8") as file:
        res_2 = count_valid_triangles_variant_2(file)
        rc.print(f"[cyan](Part Two)[/cyan] It is possible [green]{res_2}[/green] triangles.")


if __name__ == "__main__":
    main()
