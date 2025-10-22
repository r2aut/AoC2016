"""Day 10: Balance Bots."""

# ruff: noqa: D101, D105, D107, ANN204

from io import TextIOBase
from pathlib import Path

from rich.console import Console


class Chip:
    def __init__(self, value: int) -> None:
        self.value = value  # microchip's number

    def __repr__(self) -> str:
        return str(self.value)

    def __lt__(self, obj: "Chip"):
        return self.value < obj.value


class OutputBin:
    def __init__(self, number: int) -> None:
        self.number = number  # bin number
        self.bin: list[Chip] = []

    def __getitem__(self, index: int):
        return self.bin[index]

    def __repr__(self) -> str:
        return str(self.number) + ":" + str(self.bin)

    def __iadd__(self, chip: Chip):
        self.bin.append(chip)

    def push(self, chip: Chip) -> None:
        """Push the chip into the bin."""
        self.bin.append(chip)


class Bot:
    def __init__(self, number: int) -> None:
        self.number = number  # bot's number
        self.chips: list[Chip] = []

    def __repr__(self) -> str:
        return str(self.number) + ":" + str(self.chips)

    def __contains__(self, item: Chip):
        return any(i.value == item.value for i in self.chips)

    def __iadd__(self, chip: Chip):
        self.chips.append(chip)
        self.chips.sort()

    def push(self, chip: Chip) -> None:
        """Put chip into bot's pocket."""
        self.chips.append(chip)
        self.chips.sort()

    def pop_low_chip(self) -> Chip:
        """Get the first chip from the pocket."""
        return self.chips.pop(0)

    def pop_high_chip(self) -> Chip:
        """Get the last chip from the pocket."""
        return self.chips.pop(-1)

    def compare_chips(self, a: int, b: int) -> bool:
        """Compare chips."""
        if a > b:
            a, b = b, a
        if not len(self.chips):
            return False
        return self.chips[0].value == a and self.chips[-1].value == b


class Bots:
    def __init__(self) -> None:
        self.bots: dict[int, Bot] = {}

    def __repr__(self) -> str:
        return str(self.bots.values())

    def __getitem__(self, index: int):
        if index in self.bots:
            return self.bots[index]
        bot = Bot(index)
        self.bots[index] = bot
        return bot


class OutputBins:
    def __init__(self) -> None:
        self.bins: dict[int, OutputBin] = {}

    def __repr__(self) -> str:
        return "Output bins " + str(self.bins.values())

    def __getitem__(self, index: int):
        if index in self.bins:
            return self.bins[index]
        output_bin = OutputBin(index)
        self.bins[index] = output_bin
        return output_bin


def process(  # noqa: C901
    program_file: TextIOBase,
    compared_chips: tuple[int, int],
    cycle_quantity: int = 50,
) -> tuple[int | None, int]:
    """Process."""
    output_bins = OutputBins()
    bots = Bots()

    comp_results = None

    lines = program_file.readlines()

    cycle_number = cycle_quantity
    while cycle_number:
        for line in lines:
            parts = line.strip().split()

            # assert parts[0] == "value" or parts[0] == "bot", "Bad value in bot's instruction"
            if parts[0] == "value":
                chip = Chip(int(parts[1]))
                bot_num = int(parts[5])
                if chip not in bots[bot_num]:
                    bots[bot_num].push(chip)
            elif parts[0] == "bot":
                bot_num = int(parts[1])
                if len(bots[bot_num].chips) < 2:  # noqa: PLR2004
                    continue

                # assert parts[5] == "bot" or parts[5] == "output", "Bad value in bot's instruction"
                if parts[5] == "bot":
                    dest_bot_num = int(parts[6])
                    bots[dest_bot_num].push(bots[bot_num].pop_low_chip())
                elif parts[5] == "output":
                    dest_bin_num = int(parts[6])
                    output_bins[dest_bin_num].push(bots[bot_num].pop_low_chip())

                # assert parts[10] == "bot" or parts[10] == "output", "Bad value in bot's instruction"
                if parts[10] == "bot":
                    dest_bot_num = int(parts[11])
                    bots[dest_bot_num].push(bots[bot_num].pop_high_chip())
                elif parts[10] == "output":
                    dest_bin_num = int(parts[11])
                    output_bins[dest_bin_num].push(bots[bot_num].pop_high_chip())

            for b in bots.bots.values():
                if b.compare_chips(compared_chips[0], compared_chips[1]):
                    comp_results = b

        cycle_number -= 1

    return (
        comp_results.number if comp_results else None,
        output_bins.bins[0].bin.pop().value * output_bins.bins[1].bin.pop().value * output_bins.bins[2].bin.pop().value,
    )


def main():  # noqa: ANN201, D103
    with Path("puzzles/aoc2016day10_data.txt").open(encoding="utf-8") as file:
        bot, mult = process(file, (17, 61), 100)

        rc = Console()
        rc.print(f"[cyan](Part One)[/cyan] The number of the bot is [green]{bot}[/green]")
        rc.print(f"[cyan](Part Two)[/cyan] The multiplication of values is [green]{mult}[/green]")


if __name__ == "__main__":
    main()
