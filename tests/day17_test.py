"""Test module for Day 17: Two Steps Forward."""

# ruff: noqa: S101, ANN201, PLR2004

from aoc2016.day17 import Position, PRooms, find_walkers


def test_find_walkers():
    """Test cases for find_walkers function."""
    grid_x_size = 4
    grid_y_size = 4
    source_pos = Position(0, 0)
    dest_pos = Position(3, 3)
    solt = "ulqzkmiv"

    rooms = PRooms(grid_x_size, grid_y_size, source_pos=source_pos, dest_pos=dest_pos, solt=solt)
    assert repr(find_walkers(rooms=rooms, first=True).path) == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"
    assert len(find_walkers(rooms=rooms, first=False).path) == 830
