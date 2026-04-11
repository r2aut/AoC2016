"""Day 18: Like a Rogue."""

from collections import Counter
from pathlib import Path

from rich.console import Console
from rich.progress import Progress

from aoc2016.common import P1, P2, stopwatch


def trap(fragment: tuple[bool, bool, bool]) -> bool:
    pl, pc, pr = fragment
    return (pl and pc and not pr) or (pc and pr and not pl) or (pl and not pc and not pr) or (not pl and not pc and pr)


def get_next_row(pattern: tuple) -> tuple:
    row = []
    for num, _ in enumerate(pattern):
        if num == 0:
            fragment = (False, *pattern[:2])
        elif num == len(pattern) - 1:
            fragment = (*pattern[-2:], False)
        else:
            fragment = pattern[num - 1 : num + 2]
        tile = trap(fragment)
        row.append(tile)
    return tuple(row)


def char_to_bool(s: str) -> list:
    return [ch == "^" for ch in s]


def bool_to_char(bbb: list[bool]) -> str:
    return "".join(["^" if b else "." for b in bbb])


def pave_floor(pattern, row_number=None, **kwargs) -> list:  # noqa: ANN001, ANN003

    progress = kwargs.get("progress")
    floor = []
    if not row_number:
        row_number = len(pattern)

    if progress:
        progress_task = progress.add_task(f"Paving the floor for {row_number} rows", total=row_number)

    cur_row = pattern
    for n in range(row_number):
        floor.append(cur_row)
        cur_row = get_next_row(cur_row)
        if progress:
            progress.update(progress_task, completed=n + 1)
    return floor


def calc_safe_tiles(floor, **kwargs) -> int:  # noqa: ANN001, ANN003

    progress = kwargs.get("progress")
    row_num = len(floor)

    if progress:
        progress_task = progress.add_task(f"Calculating safe tiles for {row_num} rows", total=row_num)

    cnt: dict[bool, int] = Counter()
    for row_num, row in enumerate(floor):
        cnt.update(row)
        if progress:
            progress.update(progress_task, completed=row_num + 1)
    return cnt[False]


@stopwatch
def main() -> None:

    with Path("puzzles/day18.txt").open(encoding="UTF-8") as file:
        pattern = file.readline().strip()

    with Progress() as progress:
        row_num = 40
        floor1 = pave_floor(pattern, row_num, progress=progress)
        res_1 = calc_safe_tiles(floor1, progress=progress)

        row_num = 400_000
        floor2 = pave_floor(pattern, row_num, progress=progress)
        res_2 = calc_safe_tiles(floor2, progress=progress)

    rc = Console()
    rc.print(f"{P1} =  [green]{res_1}[/green]")
    rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
