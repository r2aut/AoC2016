"""Day 14: One-Time Pad."""

from hashlib import md5
from pathlib import Path
from typing import TYPE_CHECKING

from rich.console import Console

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from collections.abc import Generator
    from io import TextIOBase


class LazyHasher:
    """Class that calculates and caches hash MD5 for provided solt.

    Args:
        LazyHasher (str): creates hasher with provided solt string

    """

    def __init__(self, solt_str: str) -> None:
        self.solt_str = solt_str
        self.hashes: dict[int, tuple] = {}

    def __getitem__(self, index: int):  # noqa: ANN204
        if index not in self.hashes:
            self._calc_(index)
        return self.hashes.get(index)

    def _calc_(self, index: int) -> None:
        hstring = md5((self.solt_str + str(index)).encode("ascii"), usedforsecurity=False).hexdigest()
        three_in_row = self._check_(hstring, 3)
        five_in_row = self._check_(hstring, 5)
        self.hashes[index] = (hstring, three_in_row, five_in_row)

    def _check_(self, string: str, num: int) -> str | None:
        for i in range(len(string) - (num - 1)):
            ch = string[i]
            the_same = True
            for j in range(1, num):
                if ch != string[i + j]:
                    the_same = False
                    break
            if the_same:
                return ch
        return None

    def __str__(self) -> str:
        return f"Hasher with solt string '{self.solt_str}'"

    def __repr__(self) -> str:
        res = ""
        res += str(self) + "\n"
        for i in self.hashes.items():
            res += f"{i[0]}, {i[1]}\n"
        return res

    def __len__(self) -> int:
        return len(self.hashes)


class StratchingHasher(LazyHasher):
    """Class that calculates and caches hash MD5 for provided solt.

    Additionally, hash value calculates 2016 times subsequently.

    Args:
        LazyHasher (str): creates hasher with provided solt string

    """

    def _calc_(self, index: int) -> None:
        hstring = md5((self.solt_str + str(index)).encode("ascii"), usedforsecurity=False).hexdigest()
        for _ in range(2016):
            hstring = md5(hstring.encode("ascii"), usedforsecurity=False).hexdigest()
        three_in_row = self._check_(hstring, 3)
        five_in_row = self._check_(hstring, 5)
        self.hashes[index] = (hstring, three_in_row, five_in_row)


def hash_gen(h: LazyHasher) -> Generator:
    """Calculate and yields hash values."""
    solt_num = 0
    while True:
        hash_str, check3, _ = h[solt_num]
        if check3 is not None:
            for i in range(solt_num + 1, solt_num + 1000 + 1):
                _, _, check5 = h[i]
                if check3 == check5:
                    yield (solt_num, hash_str, check3)
                    break  # for cycle
        solt_num += 1


def read_solt_str(data_file: TextIOBase) -> str:
    """Read the puzzle input (input data) from file."""
    line = data_file.readline()
    return line.strip()


def get_hash_item(hasher, item_num: int):  # noqa: ANN001, ANN201
    """Fetch hash values untill get required."""
    h1_gen = hash_gen(hasher)
    hash_num = 1  # sequence starts from 1 according to task
    while True:
        aaa = next(h1_gen)
        if hash_num == item_num:
            return aaa
        hash_num += 1


@stopwatch
def main() -> None:

    with Path(r"puzzles/day14.txt").open(encoding="utf-8") as file:
        solt_str = read_solt_str(file)

    item_number = 64

    h1 = LazyHasher(solt_str)
    hash_item1 = get_hash_item(h1, item_number)
    res_1 = hash_item1[0]

    h2 = StratchingHasher(solt_str)
    hash_item2 = get_hash_item(h2, item_number)
    res_2 = hash_item2[0]

    rc = Console()
    rc.print(f"{P1} =  [green]{res_1}[/green]")
    rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
