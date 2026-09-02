"""Day 11: Radioisotope Thermoelectric Generators."""

import re
from collections import deque
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum, auto
from itertools import combinations
from pathlib import Path
from typing import TYPE_CHECKING

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from io import TextIOBase


class EquipType(Enum):
    Microchip = auto()
    Generator = auto()

    def __repr__(self) -> str:
        match self:
            case EquipType.Microchip:
                return "M"
            case EquipType.Generator:
                return "G"


@dataclass(frozen=True)
class Equip:
    matter: str
    eq_type: EquipType

    @classmethod
    def from_str(cls, name: str) -> Equip:
        matter, eq_type = name.split(" ")
        match eq_type:
            case "generator":
                return cls(matter, EquipType.Generator)
            case "microchip":
                matter = matter.removesuffix("-compatible")
                return cls(matter, EquipType.Microchip)
            case _:
                mess = "Unknown type"
                raise ValueError(mess)

    def __repr__(self) -> str:
        short_name = self.matter[0:2]
        return short_name.title() + repr(self.eq_type)


class Floor:
    """The content of the floor."""

    def __init__(self) -> None:
        self.equps: set[Equip] = set()

    def __str__(self) -> str:
        return " ".join(str(eqip) for eqip in self.equps)

    def get_equips(self, comb: set[Equip]) -> set[Equip]:
        """Get equipment from the floor to the elevator."""
        if comb.issubset(self.equps):
            self.equps -= comb
            return comb
        else:
            mess = f"Getting equipment - equipment is not on the floor: comb={comb}, floor={self.equps}"
            raise ValueError(mess)

    def put_equips(self, comb: set[Equip]) -> None:
        """Put equipment from the elevator to the floor."""
        if len(comb.intersection(self.equps)) == 0:
            self.equps.update(comb)
        else:
            mess = f"Putting equipment - equipment is already on the floor: comb={comb}, floor={self.equps}"
            raise ValueError(mess)

    def is_empty(self) -> bool:
        return len(self.equps) == 0

    def is_compartible(self) -> bool:
        """Check are all equipment on the floor can be kept together."""
        chips = {equip for equip in self.equps if equip.eq_type == EquipType.Microchip}
        gens = {equip for equip in self.equps if equip.eq_type == EquipType.Generator}
        res = True
        if len(gens) > 0:
            for chip in chips:
                friendly_gen = Equip(chip.matter, EquipType.Generator)
                if friendly_gen not in gens:
                    res = False
                    break
        return res

    def get_combinations(self) -> list[set[Equip]]:
        """Get all possible combination of equipment on the floor for moving."""
        comb = [set(c) for c in combinations(self.equps, 1)]
        comb2 = [set(c) for c in combinations(self.equps, 2)]
        comb.extend(comb2)
        return comb


class Elevator:
    def __init__(self) -> None:
        self.content: set[Equip] = set()

    def is_empty(self) -> bool:
        return len(self.content) == 0

    def load(self, equip_set: set[Equip]) -> None:
        """Load equipment set to the elevator."""
        if self.is_empty() and 1 <= len(equip_set) <= 2:  # noqa: PLR2004
            self.content = equip_set
        else:
            mess = "Elevator is not empty or it is loaded too much."
            raise ValueError(mess)

    def unload(self) -> set[Equip]:
        """Unload equipment set from the elevator."""
        equip_set = self.content
        self.content = set()
        return equip_set


@dataclass(frozen=True)
class Snapshot:
    ss: tuple[int, tuple[tuple[int, int], ...]]


class Facility:
    def __init__(self) -> None:
        self.floors: list[Floor] = []
        self.elevator: Elevator = Elevator()
        self.elevator_floor: int = 0
        self.steps: int = 0

    def __str__(self) -> str:
        return (
            "\n".join(f"{f_num + 1} {floor}" for f_num, floor in reversed(list(enumerate(self.floors))))
            + f"\ncurrent floor = {self.elevator_floor + 1}"
        )

    def current_floor(self) -> Floor:
        """Get the floor where the elevator is."""
        return self.floors[self.elevator_floor]

    def bring_comb_upward(self, comb: set[Equip]) -> bool:
        """Move the set of equipment upward."""
        if self.elevator_floor < len(self.floors) - 1:
            self.elevator.load(self.current_floor().get_equips(comb))
            self.elevator_floor += 1
            self.current_floor().put_equips(self.elevator.unload())
            return True
        return False

    def bring_comb_downward(self, comb: set[Equip]) -> bool:
        """Move the set of equipment downward."""
        if self.elevator_floor > 0:
            self.elevator.load(self.current_floor().get_equips(comb))
            self.elevator_floor -= 1
            self.current_floor().put_equips(self.elevator.unload())
            return True
        return False

    def is_compartible(self) -> bool:
        """Check that all equipment on the facility can be kept in there locations."""
        return all(floor.is_compartible() for floor in self.floors)

    def is_completed(self) -> bool:
        """Check that all equipment is transported to the destination."""
        return all(floor.is_empty() for floor in self.floors[0:-1])

    def snapshot(self) -> Snapshot:
        """Get shapshot to mark that this combination has already been checked."""
        res = []
        dddd = {}
        for n_floor, floor in enumerate(self.floors):
            for d in floor.equps:
                mat = dddd.setdefault(d.matter, {})
                mat[d.eq_type] = n_floor
        for dt in dddd.values():
            fg = dt[EquipType.Generator]
            fm = dt[EquipType.Microchip]
            res.append((fg, fm))
        res.sort()
        return Snapshot((self.elevator_floor, tuple(res)))

    def is_visited(self, visited: set[Snapshot]) -> bool:
        """Check that this combination has already been checked."""
        ss = self.snapshot()
        return ss in visited

    def move_all(self) -> int | None:
        """Transport all equipment to the destination (last floor)."""
        visited: set[Snapshot] = set()
        queue: deque[Facility] = deque()
        queue.append(self)
        visited.add(self.snapshot())
        # use BFS with cutting off
        while len(queue) > 0:
            start_facility = queue.popleft()
            for comb in start_facility.current_floor().get_combinations():
                if start_facility.is_completed():
                    return start_facility.steps
                next_facility = deepcopy(start_facility)
                if (
                    next_facility.bring_comb_upward(comb)
                    and next_facility.is_compartible()
                    and not next_facility.is_visited(visited)
                ):
                    next_facility.steps += 1
                    visited.add(next_facility.snapshot())
                    queue.append(next_facility)
                next_facility = deepcopy(start_facility)
                if (
                    next_facility.bring_comb_downward(comb)
                    and next_facility.is_compartible()
                    and not next_facility.is_visited(visited)
                ):
                    next_facility.steps += 1
                    visited.add(next_facility.snapshot())
                    queue.append(next_facility)
        return None


def read_data(file: TextIOBase) -> Facility:
    """Read data from stream."""
    fac = Facility()

    pattren_floor = re.compile(r"The (\w*) floor")
    pattren_microchip = re.compile(r"([\w-]*) microchip")
    pattren_generator = re.compile(r"(\w*) generator")

    for line in file:
        fac.floors.append(Floor())
        m_floor_word = pattren_floor.match(line)
        if m_floor_word:
            floor_world = m_floor_word.group(1)
            match floor_world:
                case "first":
                    floor = 0
                case "second":
                    floor = 1
                case "third":
                    floor = 2
                case "fourth":
                    floor = 3
                case _:
                    mess = f"Unknown floor: {floor_world}"
                    raise ValueError(mess)
        else:
            mess = f"Cannot get floor from string {line}"
            raise ValueError(mess)

        for m_microchip in pattren_microchip.finditer(line):
            eq = Equip.from_str(m_microchip.group(0))
            fac.floors[floor].equps.add(eq)

        for m_genegator in pattren_generator.finditer(line):
            eq = Equip.from_str(m_genegator.group(0))
            fac.floors[floor].equps.add(eq)
    return fac


# @stopwatch
def part_one(fac: Facility) -> int | None:
    return fac.move_all()


# @stopwatch
def part_two(fac: Facility) -> int | None:
    # Add extra equipment
    eq = Equip.from_str("elerium generator")
    fac.floors[0].equps.add(eq)
    eq = Equip.from_str("elerium-compatible microchip")
    fac.floors[0].equps.add(eq)
    eq = Equip.from_str("dilithium generator")
    fac.floors[0].equps.add(eq)
    eq = Equip.from_str("dilithium-compatible microchip")
    fac.floors[0].equps.add(eq)

    return fac.move_all()


@stopwatch
def main() -> None:

    rc = Console()

    with Path("puzzles/day11.txt").open(encoding="utf-8") as file:
        fac = read_data(file)
        # with Progress(transient=True) as progress:
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            SpinnerColumn(spinner_name="christmas"),
            transient=True,
        ) as progress:
            progress.add_task("Working with Part One...", total=None)
            res_1 = part_one(fac)
        rc.print(f"{P1} =  [green]{res_1}[/green]")

    # facility is changed, it's easy to read it again
    with Path("puzzles/day11.txt").open(encoding="utf-8") as file:
        fac = read_data(file)
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            SpinnerColumn(spinner_name="christmas"),
            transient=True,
        ) as progress:
            progress.add_task("Working with Part Two...", total=None)
            res_2 = part_two(fac)
        rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
