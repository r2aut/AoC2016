"""Day 21: Scrambled Letters and Hash."""

import math
from itertools import permutations
from pathlib import Path
from typing import TYPE_CHECKING

from rich.console import Console
from rich.progress import Progress

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from io import TextIOBase


class Scrambler:
    """Scrumbles string according to commands."""

    def __init__(self, password: str) -> None:
        self.password = password
        self.result: list[str] = list(self.password)

    def __repr__(self) -> str:
        return "".join(self.result)

    def swap_position(self, pos_a: int, pos_b: int) -> None:
        if not (0 <= pos_a < len(self.result) and 0 <= pos_b < len(self.result)):
            raise ValueError
        self.result[pos_a], self.result[pos_b] = self.result[pos_b], self.result[pos_a]

    def swap_letter(self, letter_a: str, letter_b: str) -> None:
        ind_a = self.result.index(letter_a)
        ind_b = self.result.index(letter_b)
        self.result[ind_a], self.result[ind_b] = self.result[ind_b], self.result[ind_a]

    def rotate_left(self, pos: int) -> None:
        pos = pos % len(self.result)
        self.result = self.result[pos:] + self.result[:pos]

    def rotate_right(self, pos: int) -> None:
        pos = pos % len(self.result)
        self.result = self.result[-pos:] + self.result[:-pos]

    def rotate_based(self, letter: str) -> None:
        ind = self.result.index(letter)
        additional_step = 1 if ind >= 4 else 0  # noqa: PLR2004
        self.rotate_right(ind + 1 + additional_step)

    def reverse_positions(self, pos_a: int, pos_b: int) -> None:  # pos_b is included
        if not (0 <= pos_a < len(self.result) and 0 <= pos_b < len(self.result)):
            raise ValueError
        pos_b1 = pos_b + 1
        sl = slice(pos_a, pos_b1)
        self.result[sl] = reversed(self.result[sl])

    def move_position(self, pos_a: int, pos_b: int) -> None:
        letter = self.result.pop(pos_a)
        self.result.insert(pos_b, letter)


def process_commands(file: TextIOBase, scr: Scrambler) -> str:
    """Process commands from file to scrumble the string."""
    for line in file:
        words = line.strip().split()
        pattern = " ".join(words[0:2])  # first two words
        match pattern:
            case "swap position":
                scr.swap_position(int(words[2]), int(words[5]))
            case "swap letter":
                scr.swap_letter(words[2], words[5])
            case "rotate left":
                scr.rotate_left(int(words[2]))
            case "rotate right":
                scr.rotate_right(int(words[2]))
            case "rotate based":
                scr.rotate_based(words[6])
            case "reverse positions":
                scr.reverse_positions(int(words[2]), int(words[4]))
            case "move position":
                scr.move_position(int(words[2]), int(words[5]))
            case _:
                mess = "Wrong input command"
                raise ValueError(mess)
    return "".join(scr.result)


@stopwatch
def main() -> None:

    # Part One - calculation of scrambled password
    file_name = "puzzles/day21.txt"
    password = "abcdefgh"  # noqa: S105

    scr = Scrambler(password)
    with Path(file_name).open(encoding="utf-8") as file:
        res_1 = process_commands(file, scr)

    # re-scrumbling password by trying all permutations (brute force)
    scrambled_password = "fbgdceah"  # noqa: S105
    letters = list(scrambled_password)
    perm = permutations(letters)
    passwd = ""

    with Progress() as progress:  # display progress bar
        total = math.perm(len(letters))  # total number of permutations
        progress_task = progress.add_task("Calculating all permutations...", total=total)
        for i in perm:
            password = "".join(i)
            scr = Scrambler(password)
            with Path(file_name).open(encoding="utf-8") as file:  # preliminary reading the file to string
                # increases speed not significantly (measured)
                # so we can continue read from file
                res_1 = process_commands(file, scr)
                if res_1 == scrambled_password:
                    passwd = password
                    progress.update(progress_task, completed=total)
                    break  # it found, stop calculationg
            progress.update(progress_task, advance=1)

    # printing results

    rc = Console()
    rc.print(f"{P1} =  [green]{res_1}[/green]")
    res_2 = passwd
    rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
