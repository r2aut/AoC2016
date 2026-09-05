"""Day 19: An Elephant Named Joseph."""

import array
from typing import TYPE_CHECKING, Any

from rich.console import Console
from rich.progress import Progress

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from collections.abc import Iterator


class Circle:
    def __init__(self, size: int) -> None:
        self.array = array.array("L", (n + 1 for n in range(size)))

    def __setitem__(self, ind: int, value: int) -> None:
        self.array[ind] = value

    def __getitem__(self, ind: int) -> int:
        return self.array[ind]

    def __delitem__(self, ind: int) -> None:
        del self.array[ind]

    def __iter__(self) -> Iterator:
        cur_item = 0
        while True:
            value = self.array[cur_item]
            yield cur_item, value
            if len(self.array) > 1:
                if cur_item < len(self.array) and self.array[cur_item] == value:  # item wasn't removed
                    cur_item += 1
                cur_item %= len(self.array)
            else:
                return

    def __len__(self) -> int:
        return len(self.array)


def calc_part_one(size: int, **kwargs: Any) -> int:  # noqa: ANN401

    progress: Progress | None = kwargs.get("progress")
    if progress is not None:
        progress_task = progress.add_task("Calculate...", total=size - 1)

    circle = Circle(size)
    last_item = 0
    it = iter(circle)
    cnt = 0
    try:
        while True:
            _, first = next(it)
            ind, _ = next(it)
            del circle[ind]
            last_item = first
            if progress is not None:
                cnt += 1
                progress.update(progress_task, completed=cnt)  # pyright: ignore[reportPossiblyUnboundVariable]
    except StopIteration:
        return last_item


def calc_part_two(size: int, **kwargs: Any) -> int:  # noqa: ANN401

    progress: Progress | None = kwargs.get("progress")
    if progress is not None:
        progress_task = progress.add_task("Calculate...", total=size - 1)

    circle = Circle(size)
    last_item = 0
    it = iter(circle)
    cnt = 0
    try:
        while True:
            ind, first = next(it)
            cross_ind = (len(circle) // 2 + ind) % len(circle)
            del circle[cross_ind]
            last_item = first
            if progress is not None:
                cnt += 1
                progress.update(progress_task, completed=cnt)  # pyright: ignore[reportPossiblyUnboundVariable]
    except StopIteration:
        return last_item


@stopwatch
def main() -> None:

    circle_size = 3014387

    rc = Console()
    with Progress() as progress:
        res1 = calc_part_one(circle_size, progress=progress)
        res2 = calc_part_two(circle_size, progress=progress)
    rc.print(f"{P1} =  [green]{res1}[/green]")
    rc.print(f"{P2} =  [green]{res2}[/green]")


if __name__ == "__main__":
    main()
