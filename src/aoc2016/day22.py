"""Day 22: Grid Computing."""

from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

from rich.console import Console

from aoc2016.common import P1, P2, stopwatch

if TYPE_CHECKING:
    from io import TextIOBase


@dataclass(frozen=True)
class Pos:
    """Position."""

    x: int
    y: int


class Node:
    def __init__(self, name: str, size: int, data: int) -> None:
        self.name: str = name
        self.size: int = size
        self.data: int = data

    def is_empty(self) -> bool:
        return self.data == 0


class ClasterParser:
    """Factory for claster."""

    @classmethod
    def from_aoc_reader(cls, reader: TextIOBase) -> Cluster:
        """Parse from AoC data."""
        nodes: dict[Pos, Node] = {}
        for line in reader:
            if len(line) > 0 and line[0] == r"/":
                name, size, used, *_ = line.strip().split()
                _, x, y = name.split("-")
                node = Node(name, int(size[:-1]), int(used[:-1]))
                pos = Pos(int(x[1:]), int(y[1:]))
                nodes[pos] = node
        return Cluster(nodes)


class Cluster:
    def __init__(self, nodes: dict[Pos, Node]) -> None:
        self.nodes: dict[Pos, Node] = nodes
        self.min_x: int = min(pos.x for pos in self.nodes)
        self.max_x: int = max(pos.x for pos in self.nodes)
        self.min_y: int = min(pos.y for pos in self.nodes)
        self.max_y: int = max(pos.y for pos in self.nodes)

    def recalculate_borders(self) -> None:
        """Recalculate if it's changed after creation."""
        self.min_x: int = min(pos.x for pos in self.nodes)
        self.max_x: int = max(pos.x for pos in self.nodes)
        self.min_y: int = min(pos.y for pos in self.nodes)
        self.max_y: int = max(pos.y for pos in self.nodes)

    def __str__(self) -> str:
        res = ""
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                pos = Pos(x, y)
                node = self.nodes.get(pos, None)
                if node is None:
                    res += " "
                elif node.data == 0:
                    res += "_"
                elif 100 * node.data / node.size > 90:  # noqa: PLR2004
                    res += "#"
                else:
                    res += "."
            res += "\n"
        return res

    def __getitem__(self, pos: Pos) -> Node:
        return self.nodes[pos]

    def __contains__(self, pos: Pos) -> bool:
        return pos in self.nodes

    def is_viable(self, pos1: Pos, pos2: Pos) -> bool:
        """Chech pair of nodes if them viable according to rules."""
        return (pos1 != pos2) and not self[pos1].is_empty() and (self[pos1].data <= self[pos2].size - self[pos2].data)

    def viable_pairs_number(self) -> int:
        """Count all viable pairs (part one)."""
        return sum(1 for pos1 in self.nodes for pos2 in self.nodes if self.is_viable(pos1, pos2))

    def check_nodes(self) -> str:
        """Check and visualize if all nodes can be used in move operations."""
        min_capacity = min(node.size for node in self.nodes.values())
        nodes = {pos: node for pos, node in self.nodes.items() if node.data <= min_capacity}
        cluster = Cluster(nodes)
        return str(cluster)

    def get_adjacent_pos(self, pos: Pos) -> list[Pos]:
        """Get all adjactent positions for the node."""
        return [
            p
            for p in [
                Pos(pos.x - 1, pos.y),
                Pos(pos.x + 1, pos.y),
                Pos(pos.x, pos.y - 1),
                Pos(pos.x, pos.y + 1),
            ]
            if self.min_x <= p.x <= self.max_x and self.min_y <= p.y <= self.max_y
        ]

    def find_min_path(self, start_pos: Pos, target_pos: Pos) -> list[Pos] | None:
        """Find min path by BFS algorithm."""
        visited: set[Pos] = set()
        queue: deque[tuple[Pos, list[Pos]]] = deque()

        visited.add(start_pos)
        queue.append((start_pos, []))

        while len(queue) > 0:
            cur_pos, state = queue.popleft()
            for next_pos in self.get_adjacent_pos(cur_pos):
                if next_pos not in visited and self[next_pos].data <= self[cur_pos].size:
                    next_state = [*state, next_pos]
                    if next_pos == target_pos:
                        return next_state
                    else:
                        visited.add(next_pos)
                        queue.append((next_pos, next_state.copy()))

        return None

    def visualise(self, path: list[Pos], visited: set[Pos]) -> str:
        """Visualise solution for debugging."""
        res = ""
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                pos = Pos(x, y)
                node = self.nodes.get(pos, None)
                if node is None:
                    res += " "
                elif pos in path:
                    res += "@"
                elif pos in visited:
                    res += "*"
                elif node.data == 0:
                    res += "_"
                elif 100 * node.data / node.size > 90:  # noqa: PLR2004
                    res += "#"
                else:
                    res += "."
            res += "\n"
        return res


@stopwatch
def part_one(cluster: Cluster) -> int:
    """Solve part one."""
    return cluster.viable_pairs_number()


@stopwatch
def part_two(cluster: Cluster) -> int | None:
    """Solve part two."""
    start_pos_dict = {pos: node for pos, node in cluster.nodes.items() if node.data == 0}
    start_pos = next(iter(start_pos_dict))
    target_pos = Pos(cluster.max_x - 1, cluster.min_y)
    destination_pos = Pos(cluster.min_x, cluster.min_y)
    min_path = cluster.find_min_path(start_pos, target_pos)
    if min_path is not None:
        path_length = len(min_path)
        path_length += (target_pos.x - destination_pos.x) * 5 + 1
        return path_length
    return None


def main() -> None:
    rc = Console()

    with Path("puzzles/day22.txt").open(encoding="utf-8") as file:
        cluster = ClasterParser.from_aoc_reader(file)
        res_1 = part_one(cluster)
        rc.print(f"{P1} =  [green]{res_1}[/green]")
        res_2 = part_two(cluster)
        rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
