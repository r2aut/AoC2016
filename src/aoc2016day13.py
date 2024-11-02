"""Day 13: A Maze of Twisty Little Cubicles"""

from enum import Enum
from typing import TypeAlias, Tuple

FAVORITE_NUMBER = 10


# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y

#     def __repr__(self) -> str:
#         # return f"(x={self.x}, y={self.y})"
#         return f"({self.x}, {self.y})"


Point: TypeAlias = Tuple[int, int]


class CellType(Enum):
    UNKNOWN = 0
    SPACE = 1
    WALL = 2

    def __str__(self) -> str:
        # return super().__str__()
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
    def __init__(self, x_size, y_size, favorite_number) -> None:
        self.x_size = x_size
        self.y_size = y_size
        self.favorite_number = favorite_number

        self.maze: list[list[CellType]] = []
        for y in range(self.y_size):
            row: list[CellType] = []
            for x in range(x_size):
                # row.append(CellType.UNKNOWN)
                row.append(self.calc_cell_type((x, y)))
            self.maze.append(row)

    def __str__(self) -> str:
        res = ""
        for row in self.maze:
            for cell in row:
                res += str(cell)
            res += "\n"
        return res

    def calc_cell_type(self, p: Point) -> CellType:
        val = p[0] * p[0] + 3 * p[0] + 2 * p[0] * p[1] + p[1] + p[1] * p[1]
        val += self.favorite_number
        bits = bin(val).count("1")
        if bits % 2 == 0:
            return CellType.SPACE
        else:
            return CellType.WALL


class Graph:
    """Class to represent a graph"""

    def __init__(self):
        self.graph = {}  # dict to store graph

    def add_edge(self, u, v, w):
        """# function to add an edge to graph"""
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
        self.graph[u][v] = w

    def get_vertices(self):
        return self.graph.keys()

    def get_graph(self):
        return self.graph

    def __repr__(self) -> str:
        # return str(self.graph)
        res = ""
        for k in self.graph.keys():
            res += str(self.graph[k])
        return res


def BellmanFord(graph, starting_vertice):

    # Step 1: Initialize distances from src to all other vertices
    # as INFINITE
    dist = dict()
    for u in graph.get_vertices():
        dist[u] = float("inf")
    dist[starting_vertice] = 0
    # print(dist)

    # Step 2: Relax all edges |V| - 1 times. A simple shortest
    # path from src to any other vertex can have at-most |V| - 1
    # edges
    for _ in range(len(graph.get_vertices()) - 1):
        # Update dist value and parent index of the adjacent vertices of
        # the picked vertex. Consider only those vertices which are still in
        # queue
        for u, r in graph.get_graph().items():
            # print(u, r)
            for v, d in r.items():
                if dist[u] != float("Inf") and dist[u] + d < dist[v]:
                    dist[v] = dist[u] + d
                    # pred[r] = k

    # Step 3: check for negative-weight cycles. The above step
    # guarantees shortest distances if graph doesn't contain
    # negative weight cycle. If we get a shorter path, then there
    # is a cycle.

    for u, r in graph.graph.items():
        for v, d in r.items():
            if dist[u] != float("Inf") and dist[u] + d < dist[v]:
                print("Graph contains negative weight cycle")
                return

    return dist


def make_graph(maze: Maze):
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


def main():

    # maze = Maze(10, 10, 10)
    maze = Maze(60, 60, 1364)
    print(maze)
    g = make_graph(maze)
    # print(g.graph[(3, 2)])
    # print(g)
    d = BellmanFord(g, (1, 1))
    print(d[(31, 39)])

    print(len({(k, v) for k, v in d.items() if v <= 50 and v > 0}))


if __name__ == "__main__":
    main()
