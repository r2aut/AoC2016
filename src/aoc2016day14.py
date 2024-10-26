""" Day 14: One-Time Pad """

from hashlib import md5


class LazyHasher:

    def __init__(self, solt_str) -> None:
        self.solt_str = solt_str
        self.hashes: dict[int, tuple] = {}

    def __getitem__(self, index):
        if index not in self.hashes:
            self._calc_(index)
        return self.hashes.get(index)

    def _calc_(self, index):
        hstring = md5((self.solt_str + str(index)).encode("ascii"), usedforsecurity=False).digest().hex()
        three_in_row = self._check_(hstring, 3)
        five_in_row = self._check_(hstring, 5)
        self.hashes[index] = (hstring, three_in_row, five_in_row)

    def _check_(self, string, num):
        for i in range(len(string) - (num - 1)):
            ch = string[i]
            the_same = True
            for j in range(1, num):
                if ch != string[i + j]:
                    the_same = False
                    break
            if the_same:
                return ch
        return None

    def __str__(self) -> str:
        return f"Hasher with solt string '{self.solt_str}'"

    def __repr__(self) -> str:
        res = ""
        res += str(self) + "\n"
        for i in self.hashes.items():
            res += f"{i[0]}, {i[1]}\n"
        return res


def calc_list(size: int, h: LazyHasher):
    counter = 0
    solt_num = 0
    aaa = list()
    while counter < size:
        found = False
        while not found:
            hash_str, check3, _ = h[solt_num]
            if check3 is not None:
                for i in range(solt_num + 1, solt_num + 1000 + 1):
                    h5, _, check5 = h[i]
                    if check3 == check5:
                        aaa.append((solt_num, hash_str, check3))
                        found = True
                        break  # for cicle
            solt_num += 1
        counter += 1
    return aaa


def main():

    h = LazyHasher("jlmsuwbz")
    l = calc_list(64, h)

    for i, item in enumerate(l):
        print(i + 1, item)


if __name__ == "__main__":
    main()
