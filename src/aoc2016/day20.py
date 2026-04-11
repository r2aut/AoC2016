"""Day 20: Firewall Rules."""

from collections import deque, namedtuple
from pathlib import Path
from typing import TYPE_CHECKING

from rich.console import Console

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from io import TextIOBase

Range = namedtuple("Range", "beg end")  # end is not included !  # noqa: PYI024


def read_blacklist(file: TextIOBase) -> list[Range]:
    blacklist: list[Range] = []
    for line in file:
        beg, end = [int(x) for x in line.strip().split("-")]
        end += 1  # exclude end from the interval
        blacklist.append(Range(beg, end))
    return blacklist


def unite_ranges(base: Range, other: Range) -> Range | None:
    """Unite ranges if they overlaps."""
    if other.beg <= base.end:
        return Range(base.beg, max(base.end, other.end))
    else:  # noqa: RET505
        return None


def unite_blacklist(blacklist: list[Range]) -> list[Range]:
    """Squeeze blacklist by uniting ranges."""
    result_blacklist: list[Range] = []

    if not blacklist:
        return result_blacklist

    range_queue = deque(blacklist)
    cur_range = range_queue.popleft()
    while range_queue:
        next_range = range_queue.popleft()
        while union_result := unite_ranges(cur_range, next_range):
            cur_range = union_result
            if range_queue:
                next_range = range_queue.popleft()
            else:
                break

        result_blacklist.append(cur_range)
        cur_range = next_range

    return result_blacklist


def min_allowed_num(beg: int, end: int, black_list: list[Range]) -> int | None:
    """Calulate minimal allowed number in interval if exists."""
    if sbl := sorted(black_list):
        _, first_end = sbl[0]
        if beg <= first_end <= end:
            return first_end
    return None


def calc_allowed_number(beg: int, end: int, black_list: list[Range]) -> int:
    """Calculate the number of allowed numbers in interval."""
    counter = 0
    range_gueue = deque(sorted(black_list))
    range_gueue.appendleft(Range(beg - 1, beg))
    range_gueue.append(Range(end, end + 1))
    cur_range = range_gueue.popleft()
    while range_gueue:
        next_range = range_gueue.popleft()
        if next_range.beg > cur_range.end:
            counter += next_range.beg - cur_range.end
        cur_range = next_range

    return counter


@stopwatch
def main() -> None:

    file_name = "puzzles/day20.txt"
    beg_number = 0
    end_number = 4294967295 + 1  # the end border shou;d not be included

    # get blacklist from file
    with Path(file_name).open(encoding="utf-8") as file:
        blacklist = read_blacklist(file)
    blacklist.sort()

    # unite blacklists
    blacklist = unite_blacklist(blacklist)

    rc = Console()
    res_1 = min_allowed_num(beg_number, end_number, blacklist)
    rc.print(f"{P1} =  [green]{res_1}[/green]")
    res_2 = calc_allowed_number(beg_number, end_number, blacklist)
    rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
