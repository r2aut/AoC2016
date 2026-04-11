"""Day 15: Timing is Everything."""

from pathlib import Path
from typing import TYPE_CHECKING

from rich.console import Console

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from io import TextIOBase


class Disk:
    """The disk of maze."""

    def __init__(self, number: int, size: int, init_pos: int) -> None:
        self.number = number
        self.size = size
        self.pos = init_pos

    def __repr__(self) -> str:
        return repr((self.number, self.size, self.pos))

    def __bool__(self) -> bool:
        return not bool(self.pos)

    def rotate(self, step_no: int = 1) -> None:
        """Implement rotation of the maze."""
        self.pos = (self.pos + step_no) % self.size


class Maze:
    """Maze of disks."""

    def __init__(self) -> None:
        self.disks: list[Disk] = []
        self.compensated = False

    def __repr__(self) -> str:
        return repr(self.disks)

    def add_disk(self, disk: Disk) -> None:
        """Add disk to maze."""
        if not self.compensated:
            self.disks.append(disk)
        else:
            mess = "Adding disks after compensation "
            raise SystemError(mess)

    def compensate_phase(self) -> None:
        """Compensate the difference in phaes when capsule has been dropped."""
        if not self.compensated:
            for d in self.disks:
                d.rotate(d.number)
            self.compensated = True

    def rotate_disks(self, step_no: int = 1) -> None:
        """Rotate all disks in maze."""
        for d in self.disks:
            d.rotate(step_no)

    def is_fallable_through(self) -> bool:
        """Is combination allows the capsule to fall through?."""
        return all(self.disks)

    def reach_fallable_time(self) -> int:
        """Find the time when the capsule can fall through."""
        self.compensate_phase()

        time = 0
        while not self.is_fallable_through():
            self.rotate_disks()
            time += 1
        return time


def read_maze(file: TextIOBase) -> Maze:
    """Read the maze from file."""
    maze = Maze()
    for line in file:
        words = line.strip().split()
        disk_no = int(words[1][1:])
        size = int(words[3])
        init_pos = int(words[11][:-1])
        maze.add_disk(Disk(disk_no, size, init_pos))

    return maze


@stopwatch
def main() -> None:

    file_name = r"puzzles/day15.txt"
    rc = Console()

    with Path(file_name).open(encoding="utf-8") as file:
        maze = read_maze(file)
        res_1 = maze.reach_fallable_time()
        rc.print(f"{P1} =  [green]{res_1}[/green]")

    with Path(file_name).open(encoding="utf-8") as file:
        maze = read_maze(file)
        maze.add_disk(Disk(7, 11, 0))
        res_2 = maze.reach_fallable_time()
        rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
