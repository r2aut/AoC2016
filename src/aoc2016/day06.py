"""Day 6: Signals and Noise."""

from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING

from rich.console import Console

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from collections.abc import Iterable
    from io import TextIOBase


def read_columns(file: TextIOBase) -> list[list[str]] | None:
    """Get data by columns."""
    columns: list[list[str]] | None = None
    for line in file:
        if not columns:
            columns = [[] for _ in range(len(line.strip()))]

        for num, ch in enumerate(line.strip()):
            columns[num].append(ch)
    return columns


def get_most_least_chars(data: Iterable) -> tuple[str, str]:
    """Get the most common and the least common characters."""
    c = Counter(data)
    c_list = list(c.items())
    c_list.sort(key=lambda item: item[1], reverse=True)
    return (c_list[0][0], c_list[-1][0])


@stopwatch
def get_most_least_words(columns: list[list[str]]) -> tuple[str, str]:
    """Get words with the most common and least common chars."""
    m_list = []
    l_list = []
    for col in columns:
        c_m, c_l = get_most_least_chars(col)
        m_list.append(c_m)
        l_list.append(c_l)

    return ("".join(m_list), "".join(l_list))


@stopwatch
def main():  # noqa : ANN201
    file_name = r"puzzles/day06.txt"
    with Path(file_name).open(encoding="utf-8") as file:
        col = read_columns(file)

        rc = Console()
        if col:
            res_1, res_2 = get_most_least_words(col)

            rc = Console()
            rc.print(f"{P1} =  [green]{res_1}[/green]")
            rc.print(f"{P2} =  [green]{res_2}[/green]")

        else:
            rc.print("[red]No data[/red]")


if __name__ == "__main__":
    main()
