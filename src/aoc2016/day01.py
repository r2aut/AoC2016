"""Day 1: No Time for a Taxicab."""

from enum import Enum
from pathlib import Path
from turtle import Turtle, done
from typing import TYPE_CHECKING, NamedTuple

from rich.console import Console

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable
    from io import TextIOBase


class Position(NamedTuple):
    """Position on the map."""

    x: int  # horizontal axis forwarded right
    y: int  # vertical axis forwarded up

    def md(self) -> int:
        """Calculate the Manhattan distance between itself and zero point."""
        return abs(self.x) + abs(self.y)


class Direction(Enum):
    """Direction in wich the runner looks (forward direction)."""

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Runner:
    """Santa delivering gifts."""

    def __init__(self, position: Position | None = None, /, log_func: Callable[[Position], None] | None = None) -> None:
        """Create runner with start position and logger function."""
        if position:
            self.position: Position = Position(*position)
        else:
            self.position = Position(0, 0)
        self.direction: Direction = Direction.NORTH
        self.log_func: Callable[[Position], None] | None = log_func
        if self.log_func:
            self.log_func(self.position)

    def move(self, blocks: int) -> None:
        """Move the runner on number of blocks."""
        for _ in range(blocks):
            match self.direction:
                case Direction.NORTH:
                    self.position = Position(self.position.x, self.position.y + 1)
                case Direction.EAST:
                    self.position = Position(self.position.x + 1, self.position.y)
                case Direction.SOUTH:
                    self.position = Position(self.position.x, self.position.y - 1)
                case Direction.WEST:
                    self.position = Position(self.position.x - 1, self.position.y)
            if self.log_func:
                self.log_func(self.position)

    def turn(self, ch: str) -> None:
        """Turn the runner (change current forward direction)."""
        match ch:
            case "L":
                self.direction = Direction((self.direction.value - 1) % 4)
            case "R":
                self.direction = Direction((self.direction.value + 1) % 4)
            case _:
                raise ValueError

    def execute(self, command: str) -> None:
        """Execute the command."""
        turn = command[0]
        distance = int(command[1:])
        self.turn(turn)
        self.move(distance)


class RunLogger:
    """Logger for runner movings."""

    def __init__(self) -> None:
        self.trace: list[Position] = []  # for drawing
        self.places: set[Position] = set()  # for quick search
        self.intersections: list[Position] = []  # to get intersections

    def log(self, position: Position) -> None:
        """Log the movings."""
        self.trace.append(position)
        if position in self.places:
            self.intersections.append(position)
        self.places.add(position)


def read_data(file: TextIOBase) -> list[str]:
    """Get data from file."""
    return file.readline().strip().split(", ")


def show_trace(trace: Iterable[Position]) -> None:
    """Show the trace as graphic turtle drawing."""
    turt = Turtle()
    turt.screen.setworldcoordinates(-50, -200, 200, 50)
    turt.pencolor("black")
    turt.setpos((0, 0))
    turt.pendown()
    turt.dot()
    for point in trace:
        turt.goto(*point)
    turt.dot()
    turt.penup()
    done()


@stopwatch
def parts(data: list[str]) -> tuple[int, int, Iterable[Position]]:
    logger = RunLogger()
    runner = Runner(log_func=logger.log)
    for cmd in data:
        runner.execute(cmd)
    return runner.position.md(), logger.intersections[0].md(), logger.trace


def main():  # noqa : ANN201
    with Path(r"puzzles/day01.txt").open(encoding="utf-8") as file:
        data = read_data(file)
        res_1, res_2, trace = parts(data)

        rc = Console()
        rc.print(f"{P1} =  [green]{res_1}[/green]")
        if res_2:
            rc.print(f"{P2} = [green]{res_2}[/green]")
        else:
            rc.print(f"{P2} It was no intersections in the way.")
        if input("Show demonstration (y/n)?").lower() == "y":
            show_trace(trace)


if __name__ == "__main__":
    main()
