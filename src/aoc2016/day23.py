"""Day 23: Safe Cracking."""

from copy import deepcopy
from math import factorial
from pathlib import Path
from typing import TYPE_CHECKING, override

from rich.console import Console

from aoc2016.common import P1, P2, Command, Computer, InvalidCommandError, stopwatch

if TYPE_CHECKING:
    from io import TextIOBase


class NewComputer(Computer):
    @override
    def execute_command(self) -> None:  # noqa: C901, PLR0912
        """Execute one command under the position pos_."""
        if self.pos_ >= len(self.prog_):
            mess = "Program halted"
            raise StopIteration(mess)
        command = self.prog_[self.pos_]
        # add new command
        if command.cmd == "tgl":
            if command.op1 is not None:
                shift = self.get_op_value(command.op1)
                ptr = self.pos_ + shift
                if ptr < len(self.prog_):
                    old_cmd = self.prog_[ptr]
                    match old_cmd.cmd:
                        case "tgl":  # 1 arg
                            if old_cmd.op1 is not None and old_cmd.op1.is_reg_:
                                old_cmd.cmd = "inc"
                        case "cpy":  # 2 arg
                            if old_cmd.op2 is not None and old_cmd.op2.is_reg_:
                                old_cmd.cmd = "jnz"
                        case "inc":  # 1 arg
                            if old_cmd.op1 is not None and old_cmd.op1.is_reg_:
                                old_cmd.cmd = "dec"
                        case "dec":  # 1 arg
                            if old_cmd.op1 is not None and old_cmd.op1.is_reg_:
                                old_cmd.cmd = "inc"
                        case "jnz":  # 2 arg
                            if old_cmd.op2 is not None and old_cmd.op2.is_reg_:
                                old_cmd.cmd = "cpy"
                self.pos_ += 1
                return
            mess = f"Wrong command {command}"
            raise InvalidCommandError(mess)
        else:  # noqa: RET506
            super().execute_command()


def read_program(file: TextIOBase) -> list[Command]:
    """Read programm from file."""
    program: list[Command] = []
    for line in file:
        if line:
            parts = line.split()
            cmd = parts[0]
            op1 = parts[1] if len(parts) >= 2 else None  # noqa: PLR2004
            op2 = parts[2] if len(parts) >= 3 else None  # noqa: PLR2004
            command = Command(cmd, op1, op2)
            program.append(command)
    return program


@stopwatch
def part_one(program: list[Command]) -> int:
    comp = NewComputer(program)
    comp.set_reg("a", 7)
    comp.execute_program()
    return comp.a_


@stopwatch
def part_two(program: list[Command]) -> int | None:
    # 479009052 = 12! + (X*Y), X=81, Y=92
    comp = NewComputer(program)
    value0 = factorial(12)
    value1 = None
    value2 = None
    command1 = program[19]
    if command1.op1 is not None:
        value1 = comp.get_op_value(command1.op1)
    command2 = program[20]
    if command2.op1 is not None:
        value2 = comp.get_op_value(command2.op1)
    return value0 + value1 * value2 if value1 is not None and value2 is not None else None


@stopwatch
def main() -> None:

    with Path("puzzles/day23.txt").open(encoding="utf-8") as file:
        program = read_program(file)

    rc = Console()

    res_1 = part_one(deepcopy(program))
    rc.print(f"{P1} =  [green]{res_1}[/green]")

    res_2 = part_two(program)
    rc.print(f"{P2} =  [green]{res_2}[/green]")


if __name__ == "__main__":
    main()
