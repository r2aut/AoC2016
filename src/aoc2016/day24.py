"""Day 24: Air Duct Spelunking."""

from collections import deque
from dataclasses import dataclass
from itertools import pairwise, permutations
from pathlib import Path
from typing import TYPE_CHECKING

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from io import TextIOBase


@dataclass(frozen=True)
class Pos:
    x: int
    y: int


@dataclass
class Mark:
    number: int
    pos: Pos


class DuctParser:
    @classmethod
    def from_aoc_reader(cls, reader: TextIOBase) -> Ducts:
        ducts = [list(line.strip()) for line in reader]
        return Ducts(ducts)


@dataclass
class Ducts:
    ducts: list[list[str]]

    def __str__(self) -> str:
        return "\n".join("".join(line) for line in self.ducts)

    def __getitem__(self, pos: Pos) -> str:
        return self.ducts[pos.y][pos.x]

    def marks(self) -> list[Mark]:
        res: list[Mark] = []
        for y, row in enumerate(self.ducts):
            for x, ch in enumerate(row):
                if ch.isdigit():
                    res.append(Mark(int(ch), Pos(x, y)))
        res.sort(key=lambda m: m.number)
        return res

    def adjacent(self, pos: Pos) -> list[Pos]:
        return [
            p
            for p in [
                Pos(pos.x - 1, pos.y),
                Pos(pos.x + 1, pos.y),
                Pos(pos.x, pos.y - 1),
                Pos(pos.x, pos.y + 1),
            ]
            if 0 <= p.y < len(self.ducts) and 0 <= p.x < len(self.ducts[0]) and self[p] != "#"
        ]

    def find_path(self, start_pos: Pos, end_pos: Pos, limit: int | None = None) -> list[Pos] | None:
        visited: set[Pos] = set()
        queue: deque[tuple[Pos, list[Pos]]] = deque()

        visited.add(start_pos)
        queue.append((start_pos, []))

        while queue:
            cur_pos, state = queue.popleft()
            if limit is None or (limit is not None and len(state) < limit - 1):
                for next_pos in self.adjacent(cur_pos):
                    if next_pos not in visited:
                        next_state = [*state, next_pos]
                        if next_pos == end_pos:
                            return next_state
                        visited.add(next_pos)
                        queue.append((next_pos, next_state))
        return None

    def find_path_between(self, positions: list[Pos], limit: int | None) -> list[Pos] | None:
        full_path: list[Pos] = []
        for start_pos, end_pos in pairwise(positions):
            part_limit = None if limit is None else limit - len(full_path)
            path = self.find_path(start_pos, end_pos, part_limit)
            if path is not None:
                full_path.extend(path)
            else:
                return None
        return full_path


def part_one(ducts: Ducts) -> int | None:
    marks = ducts.marks()
    all_lengths: list[int] = []
    limit = None
    for pp_marks in permutations(marks[1:], len(marks[1:])):
        p_marks = [marks[0], *pp_marks]
        positions = [mark.pos for mark in p_marks]
        full_path = ducts.find_path_between(positions, limit)
        if full_path is not None:
            nn_limit = len(full_path)
            all_lengths.append(nn_limit)
            limit = nn_limit if limit is None else min(limit, nn_limit)
    if all_lengths:
        return min(all_lengths)
    return None


def part_two(ducts: Ducts) -> int | None:
    marks = ducts.marks()
    all_lengths: list[int] = []
    limit = None
    for pp_marks in permutations(marks[1:], len(marks[1:])):
        p_marks = [marks[0], *pp_marks, marks[0]]
        positions = [mark.pos for mark in p_marks]
        full_path = ducts.find_path_between(positions, limit)
        if full_path is not None:
            nn_limit = len(full_path)
            all_lengths.append(nn_limit)
            limit = nn_limit if limit is None else min(limit, nn_limit)
    if all_lengths:
        return min(all_lengths)
    return None


@stopwatch
def main() -> None:
    with Path("puzzles/day24.txt").open(encoding="utf-8") as file:
        ducts = DuctParser.from_aoc_reader(file)

        rc = Console()
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            SpinnerColumn(spinner_name="christmas"),
            transient=True,
        ) as progress:
            progress.add_task("Working with Part One...", total=None)
            res_1 = part_one(ducts)
        rc.print(f"{P1} =  [green]{res_1}[/green]")

        with Progress(
            TextColumn("[progress.description]{task.description}"),
            SpinnerColumn(spinner_name="christmas"),
            transient=True,
        ) as progress:
            progress.add_task("Working with Part Two...", total=None)
            res_2 = part_two(ducts)
        rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
