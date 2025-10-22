"""Day 7: Internet Protocol Version 7."""

from io import TextIOBase
from pathlib import Path

from rich.console import Console


def scan_line_for_tls(line: str) -> bool:
    """Scan_line_for_tls function."""

    def is_abba(substring: str) -> bool:
        """Check if substring is satisfying abba function."""
        return (substring[0] == substring[3]) and (substring[1] == substring[2]) and (substring[0] != substring[1])

    zone = False
    res = False
    was_in_zone = False

    for index in range(len(line) - 3):
        if line[index] == "[":
            zone = True
        elif line[index] == "]":
            zone = False
        else:
            isa = is_abba(line[index : index + 4])
            if isa and not zone:
                res = True
            elif isa and zone:
                was_in_zone = True
    return res and not was_in_zone


def scan_line_for_ssl(line: str) -> bool:
    """Scan_line_for_ssl function."""

    def is_aba(substring: str) -> bool:
        """Check if substring is satisfying aba function."""
        return (substring[0] == substring[2]) and (substring[0] != substring[1])

    zone = False
    aba_list = []
    reverse_zone_aba_list = []

    for index in range(len(line) - 2):
        if line[index] == "[":
            zone = True
        elif line[index] == "]":
            zone = False
        else:
            isa = is_aba(line[index : index + 3])
            if isa and not zone:
                aba_list.append(line[index : index + 3])
            elif isa and zone:
                sub = line[index : index + 3]
                reverse_zone_aba_list.append(sub[1] + sub[0] + sub[1])
    return len(set(aba_list).intersection(set(reverse_zone_aba_list))) > 0


def read_addresses(file: TextIOBase) -> list[str]:
    """Read_addresses from file."""
    return [line.strip() for line in file]


def part_1(lines: list[str]) -> int:
    """Count TLS addresses (Part One)."""
    return sum(1 for line in lines if scan_line_for_tls(line))  # lazy counter


def part_2(lines: list[str]) -> int:
    """Count SSL addresses (Part Two)."""
    return sum(1 for line in lines if scan_line_for_ssl(line))  # lazy counter


def main():  # noqa : ANN201, D103
    with Path("puzzles/aoc2016day07_data.txt").open(encoding="utf-8") as file:
        lines = read_addresses(file)

    rc = Console()

    res_1 = part_1(lines)
    rc.print(f"[cyan](Part One)[/cyan] [green]{res_1}[/green] IPs in puzzle input support TLS")

    res_2 = part_2(lines)
    rc.print(f"[cyan](Part Two)[/cyan] [green]{res_2}[/green] IPs in puzzle input support SSL")


if __name__ == "__main__":
    main()
