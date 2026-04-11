"""Day 4: Security Through Obscurity."""

import re
from collections import Counter
from pathlib import Path
from string import ascii_lowercase
from typing import TYPE_CHECKING, NamedTuple

from rich.console import Console

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from io import TextIOBase


class Room(NamedTuple):
    """Room description."""

    encrypted_name: str
    sector_id: int
    checksum: str

    def real_checksum(self) -> str:
        """Get real checksum."""
        counter = Counter(self.encrypted_name)
        del counter["-"]
        check = list(counter.items())
        check.sort(key=lambda item: (9 - item[1]) * 1000 + ord(item[0]))
        return "".join([ch[0] for ch in check[:5]])

    def is_valid(self) -> bool:
        """Check the validity of the room."""
        return self.real_checksum() == self.checksum

    def decrypt_name(self) -> str:
        """Get decrypted name of the room."""
        return "".join([Room._new_letter(ch, self.sector_id) for ch in self.encrypted_name])

    @staticmethod
    def _new_letter(ch: str, shift: int) -> str:
        if ch != "-":
            ind = ord(ch) - ord("a")
            new_ind = (ind + shift) % len(ascii_lowercase)
            return ascii_lowercase[new_ind]
        return "-"


def read_rooms(file: TextIOBase) -> list[Room]:
    """Read room data from file."""
    pattern = re.compile(r"(\D+)-(\d+)\[(\w+)\]")

    result: list[Room] = []
    for line in file:
        m = pattern.match(line)
        if m:
            room = Room(m[1], int(m[2]), m[3])
            result.append(room)

    return result


@stopwatch
def part_1(data: list[Room]) -> int:
    """Find the result for Part One."""
    return sum(room.sector_id for room in data if room.is_valid())


@stopwatch
def part_2(data: list[Room], /, title: str = "northpole-object-storage") -> int | None:
    """Find the result for Part Two."""
    valid_rooms = (room for room in data if room.is_valid())
    for room in valid_rooms:
        if room.decrypt_name() == title:
            return room.sector_id
    return None


@stopwatch
def main():  # noqa: ANN201
    file_name = r"puzzles/day04.txt"
    with Path(file_name).open(encoding="utf-8") as file:
        data = read_rooms(file)

        res_1 = part_1(data)
        res_2 = part_2(data)

        rc = Console()
        rc.print(f"{P1} =  [green]{res_1}[/green]")
        rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
