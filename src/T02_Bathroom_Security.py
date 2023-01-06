# --- Day 2: Bathroom Security ---

import io

keypad1 = ( ('1','2','3'),
            ('4','5','6'),
            ('7','8','9')
          )

keypad2 = ( ('0','0','1','0','0'),
            ('0','2','3','4','0'),
            ('5','6','7','8','9'),
            ('0','A','B','C','0'),
            ('0','0','D','0','0')
          )


def get_digits(keypad, start_pos, file):
    cur_pos = start_pos # (x, y), y increased down
    for command_line in file:
        for command in command_line:
            if command == "R" and cur_pos[0]+1 < len(keypad[0]) and keypad[cur_pos[1]][cur_pos[0]+1] !='0':
                cur_pos = (cur_pos[0]+1, cur_pos[1])
            elif command == "D" and cur_pos[1]+1 < len(keypad) and keypad[cur_pos[1]+1][cur_pos[0]] !='0':
                cur_pos = (cur_pos[0], cur_pos[1]+1)
            elif command == "L" and cur_pos[0]-1 >= 0 and keypad[cur_pos[1]][cur_pos[0]-1] !='0':
                cur_pos = (cur_pos[0]-1, cur_pos[1])
            elif command == "U" and cur_pos[1]-1 >= 0 and keypad[cur_pos[1]-1][cur_pos[0]] !='0':
                cur_pos = (cur_pos[0], cur_pos[1]-1)
        yield keypad[cur_pos[1]][cur_pos[0]]


with open("puzzles/T02_Bathroom_Security.txt") as file:
    gen = get_digits(keypad1, (1,1), file)
    print("The bathroom code for part 1 is {}".format("".join(gen)))

with open("puzzles/T02_Bathroom_Security.txt") as file:
    gen = get_digits(keypad2, (1,1), file)
    print("The bathroom code for part 2 is {}".format("".join(gen)))
