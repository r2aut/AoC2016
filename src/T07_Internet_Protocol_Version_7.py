#--- Day 7: Internet Protocol Version 7 ---

def isABBA(str) -> bool:
    return (str[0] == str[3]) and (str[1] == str[2]) and (str[0] != str[1])
    
def scanLineForTLS(line) -> bool:
    
    zone = False
    res = False
    wasInZone = False

    for index in range(len(line)-3):
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

def isABA(str) -> bool:
    return (str[0] == str[2]) and (str[0] != str[1])
    
def scanLineForSSL(line) -> bool:
    zone = False
    ABAList = list()
    reverseZoneABAList = list()

    for index in range(len(line)-2):
        if line[index] == "[":
            zone = True
        elif line[index] == "]":
            zone = False
        else:
            isa = isABA(line[index: index+3])
            if isa and not zone:
                ABAList.append(line[index: index+3])
            elif isa and zone:
                sub = line[index: index+3]
                reverseZoneABAList.append(sub[1]+sub[0]+sub[1])
    res = len(set(ABAList).intersection(set(reverseZoneABAList)))>0
    return res

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
        if scanLineForTLS(line):
            counter += 1
    print(f"{counter} IPs in puzzle input support TLS")
    
    counter = 0
    for line in lines:
        if scanLineForSSL(line):
            counter += 1
    print(f"{counter} IPs in puzzle input support SSL")
