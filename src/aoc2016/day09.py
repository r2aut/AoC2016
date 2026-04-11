"""Day 9: Explosives in Cyberspace."""

from pathlib import Path

from rich.console import Console

from aoc2016.common import P1, P2, stopwatch


def get_dec_length(text: str, /, recursively: bool = False) -> int:  # noqa: FBT001, FBT002
    """Decomoress (only length, no text)."""
    it = 0
    length = 0
    while it < len(text):
        it1 = text.find("(", it)
        it2 = text.find(")", it1)

        if it1 != -1:  # found
            length += it1 - it
            markers = text[it1 + 1 : it2].split("x")
            rapport_size = int(markers[0])
            rapport_number = int(markers[1])
            it = it2 + 1  # skip ')'
            rapport_text = text[it : it + rapport_size]
            if recursively:
                length += get_dec_length(rapport_text, recursively=True) * rapport_number
            else:
                length += rapport_size * rapport_number
            it += rapport_size
        else:
            length += len(text[it:])
            break
    return length


@stopwatch
def main() -> None:
    with Path("puzzles/day09.txt").open(encoding="utf-8") as file:
        text = file.readline().rstrip()
        res_1 = get_dec_length(text)
        res_2 = get_dec_length(text, recursively=True)

        rc = Console()
        rc.print(f"{P1} =  [green]{res_1}[/green]")
        rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
