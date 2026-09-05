""" Day 19: An Elephant Named Joseph """

import array
from rich.progress import Progress


class Circle:
    def __init__(self, size):
        self.array = array.array("L", (n + 1 for n in range(size)))

    def __setitem__(self, ind, value):
        self.array[ind] = value

    def __getitem__(self, ind):
        return self.array[ind]

    def __delitem__(self, ind):
        del self.array[ind]

    def __iter__(self):
        cur_item = 0
        while True:
            value = self.array[cur_item]
            yield cur_item, value
            if len(self.array) > 1:
                if cur_item < len(self.array) and self.array[cur_item] == value:  # item wasn't removed
                    cur_item += 1
                cur_item %= len(self.array)
            else:
                return

    def __len__(self):
        return len(self.array)


def calc_part_one(size, **kwargs):

    progress: Progress | None = kwargs.get("progress", None)
    if progress is not None:
        progress_task = progress.add_task("Calculate...", total=size - 1)

    circle = Circle(size)
    last_item = 0
    it = iter(circle)
    cnt = 0
    try:
        while True:
            _, first = next(it)
            ind, _ = next(it)
            del circle[ind]
            last_item = first
            if progress is not None:
                cnt += 1
                progress.update(progress_task, completed=cnt)
    except StopIteration:
        return last_item


def calc_part_two(size, **kwargs):

    progress: Progress | None = kwargs.get("progress", None)
    if progress is not None:
        progress_task = progress.add_task("Calculate...", total=size - 1)

    circle = Circle(size)
    last_item = 0
    it = iter(circle)
    cnt = 0
    try:
        while True:
            ind, first = next(it)
            # print(first)
            cross_ind = (len(circle) // 2 + ind) % len(circle)
            del circle[cross_ind]
            last_item = first
            if progress is not None:
                cnt += 1
                progress.update(progress_task, completed=cnt)
    except StopIteration:
        return last_item


# def calc_part_two(size):

#     circle = Circle(size)
#     last_item = 0
#     it = iter(circle)
#     try:
#         while True:
#             first = next(it)

#             last_item = first
#     except StopIteration:
#         return last_item + 1  # Elf numeration is based on 1


def main():

    circle_size = 5
    circle_size = 3014387

    with Progress() as progress:
        # res1 = calc_part_one(circle_size, progress=progress)
        res2 = calc_part_two(circle_size, progress=progress)
    # print(f"Answewr for part one is {res1}")
    print(f"Answewr for part two is {res2}")

    # circle = Circle(circle_size)
    # it = iter(circle)
    # for _ in range(15):
    #     print(next(it))


if __name__ == "__main__":
    main()
