"""Day 8: Two-Factor Authentication."""

import re
from pathlib import Path
from typing import TYPE_CHECKING

from rich.console import Console

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from io import TextIOBase


class Screen:
    """Class Screen."""

    def __init__(self, width: int, hight: int) -> None:
        self.rows: list[list[bool]] = [[False for ch in range(width)] for row in range(hight)]

    def __str__(self) -> str:
        return "\n".join(["".join(["#" if ch else "." for ch in row]) for row in self.rows]) + "\n"

    def rect(self, width: int, hight: int) -> None:
        """Do rect comand."""
        for row in range(hight):
            for col in range(width):
                self.rows[row][col] = True

    def rotate_row(self, row_num: int, shifts: int) -> None:
        """Do rotate_row command."""
        width = len(self.rows[row_num])

        # get number of the item which should be the first in new row
        new_first_item = (width - shifts) % width
        # prepare new clear row
        new_row = []
        # fill new roq with values in correct order
        new_row.extend(self.rows[row_num][new_first_item:])
        new_row.extend(self.rows[row_num][0:new_first_item])
        # replace old row with new one
        self.rows[row_num] = new_row

    def rotate_column(self, column_num: int, shifts: int) -> None:
        """Do rotate_column command."""
        hight = len(self.rows)

        # get copy of processed column
        column = [row[column_num] for row in self.rows]
        # get number of the item which should be the first in new column
        new_first_item = (hight - shifts) % hight
        # prepare new clear column
        new_column = []
        # fill new column with values in corrrect order
        new_column.extend(column[new_first_item:])
        new_column.extend(column[:new_first_item])
        # replace old column with new one
        for i in range(hight):
            self.rows[i][column_num] = new_column[i]

    def count_lit_pixels(self) -> int:
        """Count lit_pixels command."""
        return sum(sum(1 if pixel else 0 for pixel in row) for row in self.rows)


class ScreenProcessor:
    """Class ScreenProcessor."""

    def __init__(self, screen: Screen, file: TextIOBase) -> None:
        self.__screen = screen
        self.__file = file

    def process_command(self) -> bool:
        """Do process_command."""
        line = self.__file.readline().strip()
        if len(line) == 0:
            return False

        if m := re.match(r"rect (\d*)x(\d*)", line):
            a = int(m.group(1))
            b = int(m.group(2))
            self.__screen.rect(a, b)
        elif m := re.match(r"rotate row y=(\d*) by (\d*)", line):
            a = int(m.group(1))
            b = int(m.group(2))
            self.__screen.rotate_row(a, b)
        elif m := re.match(r"rotate column x=(\d*) by (\d*)", line):
            a = int(m.group(1))
            b = int(m.group(2))
            self.__screen.rotate_column(a, b)
        else:
            raise ValueError
        return True

    def process_all_commands(self) -> None:
        """Do process all commands."""
        while self.process_command():
            pass


@stopwatch
def main():  # noqa: ANN201
    width = 50
    hight = 6

    with Path("puzzles/day08.txt").open(encoding="utf-8") as file:
        screen = Screen(width, hight)
        sp = ScreenProcessor(screen, file)
        sp.process_all_commands()

        res_1 = screen.count_lit_pixels()
        res_2 = str(screen)

        rc = Console()
        rc.print(f"{P1} =  [green]{res_1}[/green]")
        rc.print(f"{P2} ---------------------------------------")
        rc.print(f"[green]{res_2}[/green]")


if __name__ == "__main__":
    main()
