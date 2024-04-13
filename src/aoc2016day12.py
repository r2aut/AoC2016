""" Day 12: Leonardo's Monorail """


class Op:
    """ class models 2nd and 3d operands of operator """
    name_ = ""
    is_reg_ = False
    value_ = None

    def __init__(self, name) -> None:
        if name in ('a', 'b', 'c', 'd'):
            self.name_ = name
            self.is_reg_ = True
        elif name.lstrip('-').isdigit():
            self.name_ = name
            self.is_reg_ = False
            self.value_ = int(name)

    def __repr__(self) -> str:
        return f"Op('{self.name_}')"


class InvalidCommand(Exception):
    """ Exception class for invalid arguments"""


class Computer:
    ''' cladd modeling computer '''
    a_ = 0
    b_ = 0
    c_ = 0
    d_ = 0
    pos_ = 0
    prog_ = []

    # def __init__(self, program):
    #     self.prog_ = program

    def __init__(self, program, a=0, b=0, c=0, d=0, pos=0):
        self.prog_ = program
        self.a_ = a
        self.b_ = b
        self.c_ = c
        self.d_ = d
        self.pos_ = pos

    def __str__(self) -> str:
        return "{a = %6d, b = %6d, c = %6d, d = %6d, pos = %6d}" % \
            (self.a_, self.b_, self.c_, self.d_, self.pos_)

    def __repr__(self) -> str:
        return "{a = %d, b = %d, c = %d, d = %d, pos = %d}" % \
            (self.a_, self.b_, self.c_, self.d_, self.pos_)

    def set_reg(self, name, value):
        """ set value of register by name """
        match name:
            case "a":
                self.a_ = value
            case "b":
                self.b_ = value
            case "c":
                self.c_ = value
            case "d":
                self.d_ = value

    def get_reg(self, name):
        """ get value of register by name """
        match name:
            case "a":
                return self.a_
            case "b":
                return self.b_
            case "c":
                return self.c_
            case "d":
                return self.d_

    def execute_command(self):
        """ execute one command under the position pos_"""
        if self.pos_ >= len(self.prog_):
            raise StopIteration("Program halted")
        command = self.prog_[self.pos_]
        match command[0]:
            case "cpy":
                if command[1].is_reg_:
                    value = self.get_reg(command[1].name_)
                else:
                    value = command[1].value_
                if command[2].is_reg_:
                    self.set_reg(command[2].name_, value)
                    self.pos_ += 1
                else:
                    raise InvalidCommand(
                        "second argument on command cpy isn't a register")

            case "inc":
                if command[1].is_reg_:
                    self.set_reg(command[1].name_,
                                 self.get_reg(command[1].name_)+1)
                    self.pos_ += 1
                else:
                    raise InvalidCommand(
                        "argument of command inc isn't a register")

            case "dec":
                if command[1].is_reg_:
                    self.set_reg(command[1].name_,
                                 self.get_reg(command[1].name_)-1)
                    self.pos_ += 1
                else:
                    raise InvalidCommand(
                        "argument of command dec isn't a register")

            case "jnz":
                if command[1].is_reg_:
                    value = self.get_reg(command[1].name_)
                else:
                    value = command[1].value_

                if value != 0:
                    if not command[2].is_reg_:
                        self.pos_ += command[2].value_
                    else:
                        raise InvalidCommand(
                            "second argument of command jnz is a register")
                else:
                    self.pos_ += 1

    def execute_program(self):
        """ execute the whole program """
        while 0 <= self.pos_ < len(self.prog_):
            # print("%-20s" % self.prog_[self.pos_], end="\t")
            self.execute_command()


def read_program(file):
    """ read programm from file """
    program = []
    for line in file:
        if line:
            parts = line.split()
            command = [parts[0]]
            for i in parts[1:]:
                command.append(Op(i))
            program.append(command)
    return program


def main():
    """ the main program """

    with open("puzzles/aoc2016day12_data.txt", encoding="utf-8") as file:
        program = read_program(file)

    comp = Computer(program)
    comp.execute_program()
    print(f"The value that is left in register a is {comp.a_}")

    comp2 = Computer(program, c=1)
    comp2.execute_program()
    print(
        f"The value that is left in reg a initializeng c with 1 is {comp2.a_}")


if __name__ == "__main__":
    main()
