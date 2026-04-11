"""Day 13: A Maze of Twisty Little Cubicles."""

# ruff: noqa: S101, ANN201, PLR2004

from aoc2016.day13 import Maze, bellman_ford, make_graph

FAVORITE_NUMBER = 10


def test_maze():
    """Test maze."""
    maze = Maze(10, 10, 10)
    g = make_graph(maze)
    d = bellman_ford(g, (1, 1))
    assert d[(7, 4)] == 11
    assert len({(k, v) for k, v in d.items() if v <= 50 and v > 0}) == 24
