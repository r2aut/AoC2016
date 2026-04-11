"""Test module for Day 15: Timing is Everything."""

# ruff: noqa: S101, ANN201, PLR2004, PT018

import io

from aoc2016.day14 import LazyHasher, StratchingHasher, get_hash_item, hash_gen, read_solt_str

TEST_FILE = """abc
"""


def test_read_solt_str():
    """Tast cases for readiong solt string from file."""
    with io.StringIO(TEST_FILE) as file:
        solt_str = read_solt_str(file)
        assert solt_str == "abc"


def test_lazy_hasher():
    """Test cases for class Disk."""
    solt_str = "abc"

    h1 = LazyHasher(solt_str)
    assert h1[0] == ("577571be4de9dcce85a041ba0410f29f", None, None) and len(h1) == 1
    assert h1[1] == ("23734cd52ad4a4fb877d8a1e26e5df5f", None, None) and len(h1) == 2
    assert h1[18] == ("0034e0923cc38887a57bd7b1d4f953df", "8", None) and len(h1) == 3
    assert h1[39] == ("347dac6ee8eeea4652c7476d0f97bee5", "e", None) and len(h1) == 4
    assert h1[816] == ("3aeeeee1367614f3061d165a5fe3cac3", "e", "e") and len(h1) == 5
    assert h1[1] == ("23734cd52ad4a4fb877d8a1e26e5df5f", None, None) and len(h1) == 5


def test_stratching_hasher():
    """Test cases for class Disk."""
    solt_str = "abc"

    h1 = StratchingHasher(solt_str)
    assert h1[0] == ("a107ff634856bb300138cac6568c0f24", None, None) and len(h1) == 1
    assert h1[1] == ("65490b7e1ceeff8ade55d803c02bf553", None, None) and len(h1) == 2
    assert h1[5] == ("953a419067abb0b5e142680d73522236", "2", None) and len(h1) == 3
    assert h1[10] == ("4a81e578d9f43511ab693eee1a75f194", "e", None) and len(h1) == 4
    assert h1[89] == ("eaa5c17bec47565b98275b404eeeeea6", "e", "e") and len(h1) == 5
    assert h1[1] == ("65490b7e1ceeff8ade55d803c02bf553", None, None) and len(h1) == 5


def test_hash_gen():
    """Test cases for has_gen genegator."""
    solt_str = "abc"
    hash_num = 5
    expected_list = [
        (39, "347dac6ee8eeea4652c7476d0f97bee5", "e"),
        (92, "ae2e85dd75d63e916a525df95e999ea0", "9"),
        (110, "7af7fa13b999d68bbce565971ddbae27", "9"),
        (184, "02164648eee4fd760cdab7e343effd74", "e"),
        (291, "d7c86a1c1af63c851fe876e44427da83", "4"),
    ]

    h1 = LazyHasher(solt_str)
    gen = hash_gen(h1)
    lst = []
    for _ in range(hash_num):
        lst.append(next(gen))  # noqa: PERF401
    assert lst == expected_list


def test_get_hash_item():
    """Test cases for get_hash_item function."""
    solt_str = "abc"
    h1 = LazyHasher(solt_str)
    hash_num = 5
    assert get_hash_item(h1, hash_num) == (291, "d7c86a1c1af63c851fe876e44427da83", "4")
