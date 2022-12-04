# --- Day 1: No Time for a Taxicab ---

import turtle


def next_position(init_position: list, commands: list, stop_at_intersection=False, use_turtle=False, turtle_colour="black") -> list:

    # x - (horizontal axis) = pos[0], y - (vertical axis) = pos[1], vertical axis forwarded up
    pos = list(init_position)
    dir = 0  # possible directions are "up"=0, "right"=1, "down"=2, "left"=3
    locations = set()

    if use_turtle:
        turtle.pencolor(turtle_colour)
        turtle.setpos((0, 0))
        turtle.pendown()
        turtle.dot()

    break_condition = False
    for com in commands:
        dir_letter = com[0]
        steps = int(com[1:])
        if dir_letter == 'R':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4

        for s in range(steps):
            if dir == 0:  # moves up
                pos[1] += 1
            elif dir == 1:  # moves right
                pos[0] += 1
            elif dir == 2:  # moves down
                pos[1] -= 1
            elif dir == 3:  # moves left
                pos[0] -= 1

            if use_turtle:
                turtle.goto(pos)

            if stop_at_intersection:
                if tuple(pos) in locations:
                    break_condition = True
                    break
                else:
                    locations.add(tuple(pos))

        if break_condition:
            break

    if use_turtle:
        turtle.dot()
        turtle.penup()

    return pos


def Manhattan_distance(pos: list):
    return abs(pos[0]) + abs(pos[1])


if __name__ == "__main__":
    
    turtle_answer = input("Use turtle? (Y/N)\n")
    use_turtle = turtle_answer.strip().upper() == 'Y'
    if use_turtle:
        turtle.setworldcoordinates(-50, -200, 200, 50)

    with open("res/T01_No_Time_for_a_Taxicab.txt") as file:
        commands = file.readline().split(", ")
    current_position = [0, 0]

    print("{} blocks away is Easter Bunny HQ".format(Manhattan_distance(
        next_position(current_position, commands, use_turtle=use_turtle))))
    print("{} blocks away is the first location visited twice".format(Manhattan_distance(
        next_position(current_position, commands, True, use_turtle=use_turtle, turtle_colour="red"))))

    if use_turtle:
        turtle.done()
