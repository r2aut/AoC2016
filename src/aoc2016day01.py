""" Day 1: No Time for a Taxicab """

import turtle
from turtle import Turtle


def next_position(init_position: list, commands: list, stop_at_intersection=False,
                  tur=None, turtle_colour="black") -> list:
    """ calculate next position ??? """

    # x - (horizontal axis) = pos[0], y - (vertical axis) = pos[1], vertical axis forwarded up
    pos = list(init_position)
    direction = 0  # possible directions are "up"=0, "right"=1, "down"=2, "left"=3
    locations = set()

    use_turtle = False
    if tur is not None:
        use_turtle = True

    if use_turtle:
        # tur = Turtle()
        tur.pencolor(turtle_colour)
        tur.setpos((0, 0))
        tur.pendown()
        tur.dot()

    break_condition = False
    for com in commands:
        dir_letter = com[0]
        steps = int(com[1:])
        if dir_letter == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

        for _ in range(steps):
            if direction == 0:  # moves up
                pos[1] += 1
            elif direction == 1:  # moves right
                pos[0] += 1
            elif direction == 2:  # moves down
                pos[1] -= 1
            elif direction == 3:  # moves left
                pos[0] -= 1

            if use_turtle:
                tur.goto(pos)

            if stop_at_intersection:
                if tuple(pos) in locations:
                    break_condition = True
                    break
                else:
                    locations.add(tuple(pos))

        if break_condition:
            break

    if use_turtle:
        tur.dot()
        tur.penup()

    return pos


def manhattan_distance(pos: list):
    """ calculate Manhattan """
    return abs(pos[0]) + abs(pos[1])


def main():
    """ main function """

    turt = None
    turtle_answer = input("Use turtle? (Y/N)\n")
    use_turtle = turtle_answer.strip().upper() == 'Y'
    if use_turtle:
        turt = Turtle()
        turt.screen.setworldcoordinates(-50, -200, 200, 50)

    with open("puzzles/aoc2016day01_data.txt", encoding="utf-8") as file:
        commands = file.readline().split(", ")
    current_position = [0, 0]

    md1 = manhattan_distance(next_position(current_position, commands, tur = turt))
    print(f"{md1} blocks away is Easter Bunny HQ")
    md2 = manhattan_distance(next_position(current_position, commands, True, tur=turt,
                                           turtle_colour="red"))
    print(f"{md2} blocks away is the first location visited twice")

    if use_turtle:
        turtle.done()

if __name__ == "__main__":
    main()
