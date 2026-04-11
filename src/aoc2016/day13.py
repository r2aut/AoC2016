"""Day 13: A Maze of Twisty Little Cubicles."""

from enum import Enum
from pathlib import Path

from rich.console import Console

from aoc2016.common import P1, P2, stopwatch

FAVORITE_NUMBER = 10


type Point = tuple[int, int]


class CellType(Enum):
    """Cell type."""

    UNKNOWN = 0
    SPACE = 1
    WALL = 2

    def __str__(self) -> str:
        res = ""
        match self.value:
            case 0:
                res = "@"
            case 1:
                res = "."
            case 2:
                res = "#"
        return res


class Maze:
    """Maze implementation."""

    def __init__(self, x_size: int, y_size: int, favorite_number: int) -> None:
        self.x_size = x_size
        self.y_size = y_size
        self.favorite_number = favorite_number

        self.maze: list[list[CellType]] = []
        for y in range(self.y_size):
            row: list[CellType] = []
            for x in range(x_size):
                row.append(self.calc_cell_type((x, y)))  # noqa: PERF401
            self.maze.append(row)

    def __str__(self) -> str:
        res = ""
        for row in self.maze:
            for cell in row:
                res += str(cell)
            res += "\n"
        return res

    def calc_cell_type(self, p: Point) -> CellType:
        """Calculate the type of cell."""
        val = p[0] * p[0] + 3 * p[0] + 2 * p[0] * p[1] + p[1] + p[1] * p[1]
        val += self.favorite_number
        bits = val.bit_count()
        if bits % 2 == 0:
            return CellType.SPACE
        else:  # noqa: RET505
            return CellType.WALL


class Graph:
    """Class to represent a graph."""

    def __init__(self) -> None:
        self.graph = {}  # dict to store graph

    def __repr__(self) -> str:
        res = ""
        for v in self.graph.values():
            res += str(v)
        return res

    def add_edge(self, u, v, w) -> None:  # noqa: ANN001
        """Add an edge to graph."""
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
        self.graph[u][v] = w

    def get_vertices(self):  # noqa: ANN201
        """Get list of nodes."""
        return self.graph.keys()

    def get_graph(self):  # noqa: ANN201
        """Get graph reference."""
        return self.graph


def bellman_ford(graph, starting_vertice):  # noqa: ANN001, ANN201
    """Realisation of shortest path Bellman - Ford algorithm."""
    # Step 1: Initialize distances from src to all other vertices
    # as INFINITE
    dist = {}
    for u in graph.get_vertices():
        dist[u] = float("inf")
    dist[starting_vertice] = 0

    # Step 2: Relax all edges |V| - 1 times. A simple shortest
    # path from src to any other vertex can have at-most |V| - 1
    # edges
    for _ in range(len(graph.get_vertices()) - 1):
        # Update dist value and parent index of the adjacent vertices of
        # the picked vertex. Consider only those vertices which are still in
        # queue
        for u, r in graph.get_graph().items():
            for v, d in r.items():
                if dist[u] != float("Inf") and dist[u] + d < dist[v]:
                    dist[v] = dist[u] + d

    # Step 3: check for negative-weight cycles. The above step
    # guarantees shortest distances if graph doesn't contain
    # negative weight cycle. If we get a shorter path, then there
    # is a cycle.

    for u, r in graph.graph.items():
        for v, d in r.items():
            if dist[u] != float("Inf") and dist[u] + d < dist[v]:
                mess = "Graph contains negative weight cycle"
                raise ValueError(mess)

    return dist


def make_graph(maze: Maze) -> Graph:
    """Build grath according rules."""
    g = Graph()
    for r_num, row in enumerate(maze.maze[:-1:]):
        for c_num, cell in enumerate(row[:-1:]):
            if cell == CellType.SPACE:
                if row[c_num + 1] == CellType.SPACE:
                    g.add_edge((c_num, r_num), (c_num + 1, r_num), 1)
                    g.add_edge((c_num + 1, r_num), (c_num, r_num), 1)
                if maze.maze[r_num + 1][c_num] == CellType.SPACE:
                    g.add_edge((c_num, r_num), (c_num, r_num + 1), 1)
                    g.add_edge((c_num, r_num + 1), (c_num, r_num), 1)
    return g


@stopwatch
def main() -> None:

    with Path("puzzles/day13.txt").open(encoding="UTF-8") as file:
        favorit_number = int(file.readline().strip())

    rc = Console()
    maze = Maze(60, 60, favorit_number)
    rc.print(maze)
    g = make_graph(maze)
    d = bellman_ford(g, (1, 1))

    res_1 = d[(31, 39)]
    res_2 = len({(k, v) for k, v in d.items() if v <= 50})  # noqa: PLR2004
    rc.print(f"{P1} =  [green]{res_1}[/green]")
    rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
