""" Day 8: Two-Factor Authentication """

import io


class Screen:
    """ class Screen """
    __rows = list()

    def __init__(self, width, hight):
        for _ in range(hight):
            row = [False]*width
            self.__rows.append(row)

    def __str__(self) -> str:
        strio = io.StringIO()
        for row in self.__rows:
            for col in row:
                print("#" if col else ".", end='', sep='', file=strio)
            print(file=strio)
        return strio.getvalue()

    def rect(self, width, hight):
        """ rect method """
        for row in range(hight):
            for col in range(width):
                self.__rows[row][col] = True

    def rotate_row(self, row_num, shifts):
        """ rotate_row method """
        width = len(self.__rows[0])
        new_row = [False] * width
        for num, col in enumerate(self.__rows[row_num]):
            if col:
                new_pos = (num + shifts) % width
                new_row[new_pos] = True
        self.__rows[row_num] = new_row

    def rotate_column(self, column_num, shifts):
        """ rotate_column method """
        hight = len(self.__rows)
        new_column = [False] * hight
        for row in range(len(self.__rows)):
            if self.__rows[row][column_num]:
                new_row = (row + shifts) % hight
                new_column[new_row] = True
        for row in range(len(self.__rows)):
            self.__rows[row][column_num] = new_column[row]

    def lit_pixels(self):
        """ lit_pixels method """
        counter = 0
        for row in self.__rows:
            for col in row:
                if col:
                    counter += 1
        return counter


class ScreenProcessor:
    """ class ScreenProcessor """
    __screen = None
    __file = None

    def __init__(self, screen, file) -> None:
        self.__screen = screen
        self.__file = file

    def process_command(self):
        """ process_command method """
        line = self.__file.readline()
        if len(line) == 0:
            return False
        line_parts = line.split()
        if line_parts[0] == 'rect':
            args = line_parts[1].split('x')
            self.__screen.rect(int(args[0]), int(args[1]))
        elif line_parts[0] == "rotate" and line_parts[1] == "row":
            args = line_parts[2].split('=')
            self.__screen.rotate_row(int(args[1]), int(line_parts[4]))
        elif line_parts[0] == "rotate" and line_parts[1] == "column":
            args = line_parts[2].split('=')
            self.__screen.rotate_column(int(args[1]), int(line_parts[4]))
        return True


def main():
    """ main function """

    width = 50
    hight = 6

    with open("puzzles/aoc2016day08_data.txt", encoding="utf-8") as file:
        screen = Screen(width, hight)
        print(screen)
        sp = ScreenProcessor(screen, file)
        while sp.process_command():
            print(screen)
        print(screen.lit_pixels(), "pixels should be lit")


if __name__ == "__main__":
    main()
