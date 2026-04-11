"""Common files for AoC2016."""

import functools
import time
from typing import TYPE_CHECKING

from rich.console import Console

if TYPE_CHECKING:
    from collections.abc import Callable

P1 = "[blue]Part One[/blue]"
P2 = "[blue]Part Two[/blue]"


def stopwatch(func: Callable) -> Callable:
    """Measure execution time (decorator)."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # noqa: ANN002, ANN003, ANN202
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        t_res = time.perf_counter() - t0
        c = Console()
        c.print(f"[magenta]{t_res:.6f} sec for {func.__name__}[/magenta]")  # ty:ignore[unresolved-attribute]
        return result

    return wrapper


class InvalidCommandError(Exception):
    """Exception class for invalid arguments."""


class Op:
    """2nd and 3d operands of operator."""

    def __init__(self, name: str) -> None:
        if name in ("a", "b", "c", "d"):
            self.name_: str = name
            self.is_reg_: bool = True
        elif name.lstrip("-").isdigit():
            self.name_: str = name
            self.is_reg_: bool = False
            self.value_: int = int(name)

    def __repr__(self) -> str:
        return f"Op('{self.name_}')"


class Command:
    def __init__(self, cmd: str, op1: str | None, op2: str | None) -> None:
        self.cmd: str = cmd
        self.op1: Op | None = Op(op1) if op1 is not None else None
        self.op2: Op | None = Op(op2) if op2 is not None else None

    def __repr__(self) -> str:
        return f"{self.cmd} {self.op1} {self.op2}"


class Computer:
    """Cladd modeling computer."""

    def __init__(self, program: list[Command], pos: int = 0) -> None:
        self.prog_: list[Command] = program
        self.pos_: int = pos
        self.a_: int = 0
        self.b_: int = 0
        self.c_: int = 0
        self.d_: int = 0

    def __str__(self) -> str:
        return f"{{a = {self.a_}, b = {self.b_}, c = {self.c_}, d = {self.d_}, pos = {self.pos_}}}"

    def __repr__(self) -> str:
        return f"{{a = {self.a_}, b = {self.b_}, c = {self.c_}, d = {self.d_}, pos = {self.pos_}}}"

    def get_op_value(self, op: Op) -> int:
        return self.get_reg(op.name_) if op.is_reg_ else op.value_

    def set_reg(self, name: str, value: int) -> None:
        """Set value of register by name."""
        match name:
            case "a":
                self.a_ = value
            case "b":
                self.b_ = value
            case "c":
                self.c_ = value
            case "d":
                self.d_ = value
            case _:
                mess = f"Invalid name of register {name}"
                raise ValueError(mess)

    def get_reg(self, name: str) -> int:
        """Get value of register by name."""
        match name:
            case "a":
                return self.a_
            case "b":
                return self.b_
            case "c":
                return self.c_
            case "d":
                return self.d_
        mess = f"Invalid name of register {name}"
        raise ValueError(mess)

    def execute_command(self) -> None:  # noqa: C901
        """Execute one command under the position pos_."""
        if self.pos_ >= len(self.prog_):
            mess = "Program halted"
            raise StopIteration(mess)
        command = self.prog_[self.pos_]
        match command.cmd:
            case "cpy":
                if command.op1 is not None and command.op2 is not None and command.op2.is_reg_:
                    value = self.get_op_value(command.op1)
                    self.set_reg(command.op2.name_, value)
                    self.pos_ += 1
                    return

            case "inc":
                if command.op1 is not None and command.op1.is_reg_:
                    self.set_reg(command.op1.name_, self.get_reg(command.op1.name_) + 1)
                    self.pos_ += 1
                    return

            case "dec":
                if command.op1 is not None and command.op1.is_reg_:
                    self.set_reg(command.op1.name_, self.get_reg(command.op1.name_) - 1)
                    self.pos_ += 1
                    return
            case "jnz":
                if command.op1 is not None and command.op2 is not None:
                    value = self.get_op_value(command.op1)
                    step = self.get_op_value(command.op2)
                    if value != 0:
                        self.pos_ += step
                    else:
                        self.pos_ += 1
                    return
        mess = f"Wrong command {command}"
        raise InvalidCommandError(mess)

    def execute_program(self) -> None:
        """Execute the whole program."""
        while 0 <= self.pos_ < len(self.prog_):
            self.execute_command()
