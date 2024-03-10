import io


comands = ("cpy", "inc", "dec", "jnz")

class Operand:
    name_ = ""
    register_ = False
    value_ = None
    def __init__(self, name) -> None:
        if name in ('a', 'b', 'c', 'd'):
            self.name_ = name
            self.register_ = True
        elif name.lstrip('-').isdigit():
            self.name_ = name
            self.register_ = False
            self.value_ = int(name)
    # def __str__(self) -> str:
    #     return self.name_
    def __repr__(self) -> str:
        return f"op({self.name_})"



class Computer:
    a_ = 0
    b_ = 0
    c_ = 0
    d_ = 0
    pos_ = 0
    prog_ = []    

    def __init__(self, program):
        self.prog_ = program

    def __repr__(self) -> str:
        return "{a = %6d, b = %6d, c = %6d, d = %6d, pos = %6d}" % (self.a_,self.b_,self.c_,self.d_, self.pos_ )

    def set_reg(self, name, value):
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
        if self.pos_ >= len(self.prog_):
            raise StopIteration("Program halted")
        command = self.prog_[self.pos_]
        match command[0]:
            case "cpy":
                if command[1].register_:
                    value = self.get_reg(command[1].name_)
                else:
                    value = command[1].value_
                if command[2].register_:
                    self.set_reg(command[2].name_, value)
                    self.pos_ += 1
                else:
                    raise Exception("second argument on command cpy isn't a register")
                    
            case "inc":
                if command[1].register_ :
                    self.set_reg(command[1].name_, self.get_reg(command[1].name_)+1)
                    self.pos_ += 1
                else:
                    raise Exception("argument of command inc isn't a register")

            case "dec":
                if command[1].register_ :
                    self.set_reg(command[1].name_, self.get_reg(command[1].name_)-1)
                    self.pos_ += 1
                else:
                    raise Exception("argument of command dec isn't a register")

            case "jnz":
                if command[1].register_:
                    value = self.get_reg(command[1].name_)
                else:
                    value = command[1].value_
                    # raise Exception("first argument of command jnz is not a register")

                if value != 0:
                    if not command[2].register_:
                        self.pos_ += command[2].value_
                    else:
                        raise Exception("second argument of command jnz is a register")
                else:
                    self.pos_ += 1

    def execute_program(self):
        while 0 <= self.pos_ < len(self.prog_):
            # print("%-20s" % self.prog_[self.pos_], end="\t")
            self.execute_command()
            # print(self)


def read_program(file):
    program = []
    for line in file:
        if line:
            parts = line.split()
            command = [parts[0]]
            for i in parts[1:]:
                command.append(Operand(i))
            program.append(command)
            # print(command)
    return program
        


def main():

    test_str = r"""cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
"""

    # with io.StringIO(test_str) as file:
    with open("puzzles/T12_Leonardo's Monorail.txt") as file:
        program = read_program(file)
    # print(program)
    comp = Computer(program)
    comp.execute_program()
    # print(comp)
    print(f"The value that is left in register a is {comp.a_}")

    comp2 = Computer(program)
    comp2.c_ = 1
    comp2.execute_program()
    # print(comp2)
    print(f"The value that is left in register a initializeng c with 1 is {comp2.a_}")

if __name__ == "__main__":
    main()