""" Day 10: Balance Bots """

import io
from multiprocessing import Value


class Chip:
    value = 0
    def __init__(self, value) -> None:
        self.value = value
    def __repr__(self) -> str:
        return str(self.value)
    def __lt__(self, obj):
        return self.value < obj.value


class OutputBin:
    number = 0
    bin = None
    def __init__(self, number) -> None:
        self.number = number
        self.bin = list()
    def __getitem__(self, index):
        return bin[index]
    def __repr__(self) -> str:
        return str(self.number)+':'+str(self.bin)
    def __iadd__(self, chip):
        self.bin.append(chip)
    def push(self, chip):
        self.bin.append(chip)


class Bot:
    number = 0
    chips = None
    condition = None
    def __init__(self, number) -> None:
        self.number = number
        self.chips = list()
    def pop_low_chip(self) -> Chip:
        return self.chips.pop(0)
    def pop_high_chip(self) -> Chip:
        return self.chips.pop(-1)
    def __iadd__(self, chip):
        self.chips.append(chip)
        self.chips.sort()
    def push(self, chip):
        self.chips.append(chip)
        self.chips.sort()
    def __repr__(self) -> str:
        return str(self.number)+':'+str(self.chips)
    def __contains__(self, item):
        for i in self.chips:
            if i.value == item.value:
                return True
        return False
    def compare_chips(self, a, b):
        if a > b:
            a, b = b, a
        if not len(self.chips):
            return False
        if self.chips[0].value == a and self.chips[-1].value == b:
            return True
        return False

class Bots:
    bots = dict()
    def __getitem__(self, index):
        if index in self.bots:
            return self.bots[index]
        else:
            bot = Bot(index)
            self.bots[index] = bot
            return bot
    def __repr__(self) -> str:
        return str(self.bots.values())

class OutputBins:
    bins = dict()
    def __getitem__(self, index):
        if index in self.bins:
            return self.bins[index]
        else:
            bin = OutputBin(index)
            self.bins[index] = bin
            return bin
    def __repr__(self) -> str:
        return "Output bins " + str(self.bins.values())


def process(program_file, compared_chips, cycle_quantity = 50):
    output_bins = OutputBins()
    bots = Bots()

    comp_results = None
    
    lines = program_file.readlines()


    cycle_number = cycle_quantity
    while cycle_number:

        for line in lines:
            parts = line.strip().split()

            assert parts[0]=="value" or parts[0]=="bot", "Bad value in bot's instruction"
            if parts[0] == "value":
                chip = Chip(int(parts[1]))
                bot_num = int(parts[5])
                if chip not in bots[bot_num]:
                    bots[bot_num].push(chip)
            elif parts[0] == "bot":
                bot_num = int(parts[1])
                if len(bots[bot_num].chips) < 2:
                    continue

                assert parts[5]=="bot" or parts[5]=="output", "Bad value in bot's instruction"
                if parts[5] == "bot":
                    dest_bot_num = int(parts[6])
                    bots[dest_bot_num].push(bots[bot_num].pop_low_chip())
                elif parts[5] == "output":
                    dest_bin_num = int(parts[6])
                    output_bins[dest_bin_num].push(bots[bot_num].pop_low_chip())

                assert parts[10]=="bot" or parts[10]=="output", "Bad value in bot's instruction"
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

    return comp_results.number, output_bins.bins[0].bin.pop().value*output_bins.bins[1].bin.pop().value*output_bins.bins[2].bin.pop().value


def main():

    with open("puzzles/aoc2016day10_data.txt", encoding="utf-8") as file:
        bot, mult = process(file, (17,61), 100)
        print(f"The number of the bot is {bot}")
        print(f"The multiplication of values is {mult}")
    

if __name__ == "__main__":
    main()
