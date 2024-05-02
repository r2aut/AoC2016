""" Day 10: Balance Bots """

import io
from multiprocessing import Value

TEST_DATA = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""

class Chip:
    value = 0
    def __init__(self, value) -> None:
        self.value = value
    def __repr__(self) -> str:
        return str(self.value)
    def __lt__(self, obj):
        return self.value < obj.value
    # def __int__(self):
    #     return self.value



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
        # self.chips.clear()
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
        # return str(self.number)+':'+str(bin)
        return str(self.number)+':'+str(self.chips)
    def __contains__(self, item):
        for i in self.chips:
            if i.value == item.value:
                return True
        return False
    # def contain_all_chips(self, *args):
    #     res = True
    #     for i in args:
    #         if i not in self:
    #             res = False
    #             break
    #     return res
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
        return str(self.bins.values())


def process(program_file):
    output_bins = OutputBins()
    bots = Bots()
    
    lines = program_file.readlines()


    i = 100
    while i:

        for line in lines:
            parts = line.strip().split()
            # print(parts)

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
            
            # print(bots)
            for b in bots.bots.values():
                if b.compare_chips(17, 61):
                # if b.compare_chips(2, 5):
                    return b.number
                    ...

        i -= 1
        # print(i)
        print(output_bins)
    return None

def main():

    with open("puzzles/aoc2016day10_data.txt", encoding="utf-8") as file:

    # with io.StringIO(TEST_DATA) as file:
        print(process(file))
    

if __name__ == "__main__":
    main()
