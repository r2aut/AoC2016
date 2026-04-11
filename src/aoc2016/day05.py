"""Day 5: How About a Nice Game of Chess."""

from hashlib import md5
from pathlib import Path
from typing import TYPE_CHECKING, Any, NoReturn

from rich.console import Console
from rich.progress import BarColumn, Progress, TaskProgressColumn, TextColumn, TimeElapsedColumn

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from collections.abc import Generator


def hash_gen(door_id: str, pattern: str) -> Generator[str, Any, NoReturn]:
    """Generate valid hashes."""
    index = 0
    while True:
        door_str = door_id + str(index)
        digest = md5(door_str.encode("utf-8")).hexdigest()  # noqa: S324
        if digest.startswith(pattern):
            yield digest
        index += 1


def part_1(door_id: str, pattern: str, pass_len: int, /, progress: Progress | None = None) -> str:
    """Get the password for Part One."""
    ch_index = len(pattern)
    if progress:
        task1 = progress.add_task("Processing Part One ...", total=pass_len)
    hashes = hash_gen(door_id, pattern)
    result = []
    for _ in range(pass_len):
        ch = next(hashes)[ch_index]
        result.append(ch)
        if progress:
            progress.update(task1, advance=1)  # pyright: ignore[reportPossiblyUnboundVariable]
    return "".join(result)


def part_2(door_id: str, pattern: str, pass_len: int, /, progress: Progress | None = None) -> str:
    """Get the password for Part Two."""
    if progress:
        task2 = progress.add_task("Processing Part Two ...", total=pass_len)
    pos_index = len(pattern)
    ch_index = len(pattern) + 1
    hashes = hash_gen(door_id, pattern)
    result: list = [None] * pass_len
    pos_char_list = [str(ch) for ch in range(pass_len)]
    while not all(result):
        c = next(hashes)
        pos_char = c[pos_index]
        if pos_char in pos_char_list:
            pos = int(pos_char)
            ch = c[ch_index]
            if pos < 8 and not result[pos]:  # noqa: PLR2004
                result[pos] = ch
                if progress:
                    progress.update(task2, advance=1)  # pyright: ignore[reportPossiblyUnboundVariable]
    return "".join(result)


@stopwatch
def main():  # noqa: ANN201
    file_name = r"puzzles/day05.txt"
    with Path(file_name).open(encoding="utf-8") as file:
        door_id = file.readline().strip()

    door_id = "abc"
    pattern = "00000"

    with Progress(  # show progress bar to display process
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn(),
    ) as progress:
        res_1 = part_1(door_id, pattern, 8, progress=progress)
        res_2 = part_2(door_id, pattern, 8, progress=progress)

    rc = Console()
    rc.print(f"{P1} =  [green]{res_1}[/green]")
    rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
