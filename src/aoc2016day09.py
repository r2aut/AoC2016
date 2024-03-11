""" Day 9: Explosives in Cyberspace """


def get_dec_length(text, recursively=False):
    """ decomoress function """
    it = 0
    length = 0
    while it < len(text):
        it1 = text.find("(", it)
        it2 = text.find(")", it1)

        if it1 != -1:  # found
            length += (it1 - it)
            markers = text[it1+1:it2].split('x')
            rapport_size = int(markers[0])
            rapport_number = int(markers[1])
            it = it2+1  # skip ')'
            rapport_text = text[it: it+rapport_size]
            if recursively:
                length += get_dec_length(rapport_text, True) * rapport_number
            else:
                length += rapport_size * rapport_number
            it += rapport_size
        else:
            length += len(text[it:])
            break
    return length


def main():
    """ main function """
    with open("puzzles/aoc2016day09_data.txt", encoding="utf-8") as file:
        text = file.readline().rstrip()
        print(f"Decompressed length of the file is {get_dec_length(text)}")
        print(f"Fully decompressed length of the file is {
              get_dec_length(text, True)}")


if __name__ == "__main__":
    main()
