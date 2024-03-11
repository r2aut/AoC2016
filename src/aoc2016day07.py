""" Day 7: Internet Protocol Version 7 """

def is_abba(string) -> bool:
    """ is_abba function """
    return (string[0] == string[3]) and (string[1] == string[2]) and (string[0] != string[1])

def scan_line_for_tls(line) -> bool:
    """ scan_line_for_tls function """
    zone = False
    res = False
    was_in_zone = False

    for index in range(len(line)-3):
        if line[index] == "[":
            zone = True
        elif line[index] == "]":
            zone = False
        else:
            isa = is_abba(line[index: index+4])
            if isa and not zone:
                res = True
            elif isa and zone:
                was_in_zone = True
    return res and not was_in_zone

def is_aba(string) -> bool:
    """ is_aba function """
    return (string[0] == string[2]) and (string[0] != string[1])

def scan_line_for_ssl(line) -> bool:
    """ scan_line_for_ssl function """
    zone = False
    aba_list = list()
    reverse_zone_aba_list = list()

    for index in range(len(line)-2):
        if line[index] == "[":
            zone = True
        elif line[index] == "]":
            zone = False
        else:
            isa = is_aba(line[index: index+3])
            if isa and not zone:
                aba_list.append(line[index: index+3])
            elif isa and zone:
                sub = line[index: index+3]
                reverse_zone_aba_list.append(sub[1]+sub[0]+sub[1])
    res = len(set(aba_list).intersection(set(reverse_zone_aba_list)))>0
    return res

def read_file(file):
    """ read_file function """
    lines = list()
    while True:
        line = file.readline()
        if line:
            lines.append(line)
        else:
            break
    return lines

def main():
    """ main function """

    with open("puzzles/aoc2016day07_data.txt", encoding="utf-8") as file:
        lines = read_file(file)

    counter = 0
    for line in lines:
        if scan_line_for_tls(line):
            counter += 1
    print(f"{counter} IPs in puzzle input support TLS")

    counter = 0
    for line in lines:
        if scan_line_for_ssl(line):
            counter += 1
    print(f"{counter} IPs in puzzle input support SSL")

if __name__ == "__main__":
    main()
