""" Day 16: Dragon Checksum """


def mod_dragon_curve(str_a: str) -> str:
    """Implementation of one step of Modified_Dragon_Curve"""
    assert isinstance(str_a, str)

    str_b = reversed(str_a)
    str_b = "".join(["1" if ch == "0" else "0" for ch in str_b])
    return str_a + "0" + str_b


def calc_random_data(start_str: str, length: int) -> str:
    """Calculating data for provided start sequence and length"""
    res_str = start_str
    while len(res_str) < length:
        res_str = mod_dragon_curve(res_str)
    return res_str[0:length]  # we need only length chars


def calc_part_check_sum(origin: str) -> str:
    """One step of check sum calculation"""
    assert len(origin) % 2 == 0

    return "".join(
        [
            "1" if origin[i * 2] == origin[i * 2 + 1] else "0"
            for i in range(len(origin) // 2)
        ]
    )


def calc_check_sum(origin: str) -> str:
    """Check sum calculation"""
    check_sum = origin
    while len(check_sum) % 2 == 0:
        check_sum = calc_part_check_sum(check_sum)
    return check_sum


def main():
    """Entry point"""

    start_seq = "01111001100111011"
    seq_length_1 = 272
    seq_length_2 = 35651584

    print(f"For initial sequence {start_seq}")

    seq_1 = calc_random_data(start_seq, seq_length_1)
    check_sum_1 = calc_check_sum(seq_1)
    print(f"The correct checksum for length {seq_length_1} is {check_sum_1}")

    seq_2 = calc_random_data(start_seq, seq_length_2)
    check_sum_2 = calc_check_sum(seq_2)
    print(f"The correct checksum for length {seq_length_2} is {check_sum_2}")


if __name__ == "__main__":
    main()
