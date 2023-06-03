#--- Day 7: Internet Protocol Version 7 ---

def isABBA(str) -> bool:
    return (str[0] == str[3]) and (str[1] == str[2]) and (str[0] != str[1])
    
def scanLine(line) -> bool:
    
    zone = False
    res = False
    wasInZone = False

    for index in range(len(line)-4):
        if line[index] == "[":
            zone = True
        elif line[index] == "]":
            zone = False
        else:
            isa = isABBA(line[index: index+4])
            if isa and not zone:
                res = True
            elif isa and zone:
                wasInZone = True
    return res and not wasInZone


def readFile(file) -> list():
    lines = list()
    while(True):
        line = file.readline()
        if line:
            lines.append(line)
        else:
            break
    return lines

if __name__ == "__main__":

    with open("puzzles/T07_Internet_Protocol_Version_7.txt") as file:
        lines = readFile(file)

    counter = 0
    for line in lines:
        if scanLine(line):
            counter += 1
    print(f"{counter} IPs in puzzle input support TLS")
    