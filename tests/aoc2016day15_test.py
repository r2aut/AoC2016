""" Test module for Day 15: Timing is Everything """

import io

from src.aoc2016day15 import read_maze
from src.aoc2016day15 import Disk, Maze

TEST_FILE = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
"""

def test_read_maze():
    """ Tast cases for readiong maze from file """
    with io.StringIO(TEST_FILE) as file:
        maze = read_maze(file)
        assert repr(maze) == "[(1, 5, 4), (2, 2, 1)]"

# def create_test_maze():
#     maze = Maze
#     pass


def test_disk_class():
    """ Test cases for class Disk """

    d = Disk(1,5,4)
    assert repr(d) == "(1, 5, 4)"
    assert bool(d) is False

    d.rotate()
    assert repr(d) == "(1, 5, 0)"
    assert bool(d) is True

    d.rotate(2)
    assert repr(d) == "(1, 5, 2)"
    assert bool(d) is False

def test_maze_class():
    """ Test cases for class Maze """

    m = Maze()
    m.add_disk(Disk(1, 5, 4))
    m.add_disk(Disk(2, 2, 1))
    assert repr(m) == "[(1, 5, 4), (2, 2, 1)]"

    m.compensate_phase()
    assert repr(m) == "[(1, 5, 0), (2, 2, 1)]"
    assert m.is_fallable_through() is False

    m.rotate_disks()
    assert repr(m) == "[(1, 5, 1), (2, 2, 0)]"
    assert m.is_fallable_through() is False

    time = m.reach_fallable_time()
    assert time == 4
    assert repr(m) == "[(1, 5, 0), (2, 2, 0)]"
