
def decompress(in_text) -> str:
    out_text = str()
    it = 0
    while it < len(in_text):
        it1 = in_text.find("(", it)
        it2 = in_text.find(")", it1)

        if it1 != -1 :

            assert it1 != -1 and it2 != -1 and it1 < it2

            out_text += in_text[it:it1]

            markers = in_text[it1+1:it2].split('x')
            it = it2+1 # skip ')'

            for i in range(int(markers[1])): # it1+1 skips '('
                out_text += in_text[it: it+int(markers[0])]
            
            it += int(markers[0])
        else :
            out_text += in_text[it:]
            break
    return out_text


if __name__ == "__main__":
    with open("puzzles/T09_Explosives_in_Cyberspace.txt") as file:
        text = file.readline().rstrip()
        print("Decompressed length of the file is", len(decompress(text)))
