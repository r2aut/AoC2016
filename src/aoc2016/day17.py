"""Day 17: Two Steps Forward."""

import logging
import pathlib
import sys
from collections import namedtuple
from copy import copy
from enum import Enum
from hashlib import md5

from rich.console import Console
from rich.progress import BarColumn, Progress, TaskProgressColumn, TextColumn, TimeElapsedColumn

from aoc2016.common import P1, P2, stopwatch

logger = logging.getLogger(__name__)


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


class Path:
    """Path of made by the walker."""

    def __init__(self, path=None) -> None:  # noqa: ANN001
        if not path:
            self.directions: list[Direction] = []
        else:
            self.directions = copy(path)

    def __add__(self, d: Direction) -> Path:
        new_instance = Path(self.directions)
        new_instance.directions.append(d)
        return new_instance

    def __repr__(self) -> str:
        return "".join([d.value for d in self.directions])

    def __len__(self) -> int:
        return len(self.directions)


Position = namedtuple("Position", "x y")  # noqa: PYI024
Door = namedtuple("Door", "pos direction")  # noqa: PYI024


def get_new_position(source_pos: Position, direction: Direction, step_num: int = 1) -> Position:
    """Calculate new Position using the Direction provided."""
    x, y = source_pos
    match direction:
        case Direction.UP:
            new_pos = Position(x, y - step_num)
        case Direction.DOWN:
            new_pos = Position(x, y + step_num)
        case Direction.LEFT:
            new_pos = Position(x - step_num, y)
        case Direction.RIGHT:
            new_pos = Position(x + step_num, y)

    return new_pos


class PRooms:
    """Protection rooms."""

    def __init__(self, x_size: int, y_size: int, /, source_pos: Position, dest_pos: Position, solt: str) -> None:
        self.x_size: int = x_size
        self.y_size: int = y_size
        self.source_pos: Position = source_pos
        self.dest_pos: Position = dest_pos
        self.solt: str = solt
        self._valid_status = set("bcdef")
        self._index_to_dir = {0: Direction.UP, 1: Direction.DOWN, 2: Direction.LEFT, 3: Direction.RIGHT}
        logger.debug("PRooms created - %s", repr(self))

    def __repr__(self) -> str:
        return f"PRooms(x_size={self.x_size}, y_size={self.y_size}, source_pos={self.source_pos}, dest_pos={self.dest_pos}, solt={self.solt})"

    def _get_cell_status(self, path: str) -> str:
        return md5((self.solt + str(path)).encode("utf-8")).hexdigest()[0 : len(self._index_to_dir)]  # noqa: S324

    def get_opened_doors(self, pos: Position, path: str) -> list[Door]:
        res = self._get_cell_status(path)
        doors: list[Door] = []
        for i in range(4):
            d = self._index_to_dir[i]
            new_pos = get_new_position(pos, d)
            x, y = new_pos
            if res[i] in self._valid_status and 0 <= x < self.x_size and 0 <= y < self.y_size:
                doors.append(Door(pos, self._index_to_dir[i]))
        return doors


class Walker:
    def __init__(self, rooms: PRooms, /, cur_pos: Position | None = None, path: Path | None = None) -> None:

        self.rooms: PRooms = rooms
        self.cur_pos: Position = cur_pos or self.rooms.source_pos
        self.path: Path = copy(path) if path else Path()

        logger.debug("Walker created - %s", repr(self))

    def __repr__(self) -> str:
        return f"Walker({self.cur_pos}, path={self.path})"

    def finished(self) -> bool:
        return self.cur_pos == self.rooms.dest_pos


def propagate_walkers(walkers: list) -> list[Walker]:
    """Propagate walkers on cell to opened doors."""
    new_walkers: list[Walker] = []
    for walker in walkers:
        opened_doors = walker.rooms.get_opened_doors(walker.cur_pos, walker.path)
        for d in opened_doors:
            new_runner = Walker(
                walker.rooms,
                cur_pos=get_new_position(walker.cur_pos, d.direction),
                path=copy(walker.path) + d.direction,
            )
            new_walkers.append(new_runner)
    return new_walkers


def find_walkers(rooms: PRooms, first: bool = True):  # noqa: ANN201, FBT001, FBT002
    """Find pathes from origin to destination in the Protecting rooms."""
    current_walkers: list[Walker] = [Walker(rooms)]
    finished_walkers: list[Walker] = []

    current_walkers = propagate_walkers(current_walkers)
    while current_walkers:
        finished = [w for w in current_walkers if w.finished()]
        if finished:
            finished_walkers.extend(finished)
            for w in finished:
                current_walkers.remove(w)
            if first:
                break
        current_walkers = propagate_walkers(current_walkers)
    if not finished_walkers:
        return None
    elif first:  # noqa: RET505
        return finished_walkers[0]
    else:
        return finished_walkers[-1]


@stopwatch
def main() -> None:

    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    logger.debug("Programm started")

    grid_x_size = 4
    grid_y_size = 4
    source_pos = Position(0, 0)
    dest_pos = Position(3, 3)
    with pathlib.Path("puzzles/day17.txt").open(encoding="UTF-8") as file:
        solt = file.readline().strip()

    with Progress(TextColumn("[progress.description]{task.description}"), BarColumn(), TaskProgressColumn(), TimeElapsedColumn()) as progress:
        rooms = PRooms(grid_x_size, grid_y_size, source_pos=source_pos, dest_pos=dest_pos, solt=solt)

        progress_task1 = progress.add_task("Finding the shortest path...", total=None)
        fastest_walker = find_walkers(rooms=rooms, first=True)
        progress.update(progress_task1, completed=1, total=1)

        progress_task2 = progress.add_task("Finding the longest path...", total=None)
        slowest_walker = find_walkers(rooms=rooms, first=False)
        progress.update(progress_task2, total=1, completed=1)

    res_1 = fastest_walker.path
    res_2 = len(slowest_walker.path)
    rc = Console()
    rc.print(f"{P1} =  [green]{res_1}[/green]")
    rc.print(f"{P2} =  [green]{res_2}[/green]")

    logger.debug("Programm finished")


if __name__ == "__main__":
    main()
