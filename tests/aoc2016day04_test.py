"""Day 4: Security Through Obscurity unit tests."""

# ruff: noqa: S101, ANN201, PLR2004

from io import StringIO

from src.aoc2016day04 import Room, part_1, part_2, read_rooms

TEST_ROOMS = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
"""


def test_read_rooms():  # noqa: D103
    assert read_rooms(StringIO("aaaaa-bbb-z-y-x-123[abxyz]")) == [Room("aaaaa-bbb-z-y-x", 123, "abxyz")]
    assert read_rooms(StringIO(TEST_ROOMS)) == [
        Room("aaaaa-bbb-z-y-x", 123, "abxyz"),
        Room("a-b-c-d-e-f-g-h", 987, "abcde"),
        Room("not-a-real-room", 404, "oarel"),
        Room("totally-real-room", 200, "decoy"),
    ]


def test_part_1():  # noqa: D103
    data = read_rooms(StringIO(TEST_ROOMS))
    assert part_1(data) == 1514


TEST_ROOMS_2 = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
qzmt-zixmtkozy-ivhz-343[zimth]
totally-real-room-200[decoy]
"""


def test_part_2():  # noqa: D103
    data = read_rooms(StringIO(TEST_ROOMS_2))
    assert part_2(data, title="very-encrypted-name") == 343
