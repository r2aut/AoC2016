"""Day 16: Dragon Checksum."""

from pathlib import Path

from rich.console import Console

from aoc2016.common import P1, P2, stopwatch


def mod_dragon_curve(str_a: str) -> str:
    """Implement of one step of Modified_Dragon_Curve."""
    if not isinstance(str_a, str):
        raise TypeError

    str_b = reversed(str_a)
    str_b = "".join(["1" if ch == "0" else "0" for ch in str_b])
    return str_a + "0" + str_b


def calc_random_data(start_str: str, length: int) -> str:
    """Calculate data for provided start sequence and length."""
    res_str = start_str
    while len(res_str) < length:
        res_str = mod_dragon_curve(res_str)
    return res_str[0:length]  # we need only length chars


def calc_part_check_sum(origin: str) -> str:
    """Make one step of check sum calculation."""
    if len(origin) % 2 != 0:
        raise ValueError

    return "".join(
        ["1" if origin[i * 2] == origin[i * 2 + 1] else "0" for i in range(len(origin) // 2)],
    )


def calc_check_sum(origin: str) -> str:
    """Calculate check sum."""
    check_sum = origin
    while len(check_sum) % 2 == 0:
        check_sum = calc_part_check_sum(check_sum)
    return check_sum


@stopwatch
def main() -> None:

    with Path("puzzles/day16.txt").open(encoding="UTF-8") as file:
        start_seq = file.readline().strip()
    seq_length_1 = 272
    seq_length_2 = 35651584

    rc = Console()

    seq_1 = calc_random_data(start_seq, seq_length_1)
    res_1 = calc_check_sum(seq_1)
    rc.print(f"{P1} =  [green]{res_1}[/green]")

    seq_2 = calc_random_data(start_seq, seq_length_2)
    res_2 = calc_check_sum(seq_2)
    rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
