""" Day 2: Bathroom Security """

from collections import namedtuple
from io import TextIOWrapper

keypad1 = (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"))

keypad2 = (
    ("0", "0", "1", "0", "0"),
    ("0", "2", "3", "4", "0"),
    ("5", "6", "7", "8", "9"),
    ("0", "A", "B", "C", "0"),
    ("0", "0", "D", "0", "0"),
)

Position = namedtuple("Position", "x y")  # (x, y), y increased down


def get_digits(keypad, start_pos: Position, file: TextIOWrapper):
    """Get_digits function"""

    cur_pos = start_pos
    result = []
    for command_line in file:
        for command in command_line.strip():
            match command:
                case "R":
                    next_pos = Position(cur_pos.x + 1, cur_pos.y)
                case "D":
                    next_pos = Position(cur_pos.x, cur_pos.y + 1)
                case "L":
                    next_pos = Position(cur_pos.x - 1, cur_pos.y)
                case "U":
                    next_pos = Position(cur_pos.x, cur_pos.y - 1)

            if (
                0 <= next_pos.y < len(keypad)
                and 0 <= next_pos.x < len(keypad[next_pos.y])
                and keypad[next_pos.y][next_pos.x] != "0"
            ):
                cur_pos = next_pos
        result.append(keypad[cur_pos.y][cur_pos.x])
    return "".join(result)


def main():
    """main function"""
    with open("puzzles/aoc2016day02_data.txt", encoding="utf-8") as file:
        dig1 = get_digits(keypad1, Position(1, 1), file)
        print(f"The bathroom code for part 1 is {dig1}")

    with open("puzzles/aoc2016day02_data.txt", encoding="utf-8") as file:
        dig2 = get_digits(keypad2, Position(1, 1), file)
        print(f"The bathroom code for part 2 is {dig2}")


if __name__ == "__main__":
    main()
