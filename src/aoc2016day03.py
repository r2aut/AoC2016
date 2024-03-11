""" Day 3: Squares With Three Sides """


def count_valid_triangles_variant_1(file):
    """ count_valid_triangles_variant_1 for the 1st phase """
    counter = 0
    for line in file:
        triangle_str = line.strip().split()
        triangle = [int(x) for x in triangle_str]
        triangle.sort()
        if triangle[2] < triangle[1]+triangle[0]:
            counter += 1
    return counter


def count_valid_triangles_variant_2(file):
    """ count_valid_triangles_variant_2 for the 2nd phase """
    counter = 0
    flag = True
    while flag:
        tri = list()
        for _ in range(3):  # prepare several triangle descriptions using columns
            line = file.readline()
            if not line:  # go out
                flag = False
                break
            if line:
                triangle_str = line.strip().split()
                triangle = [int(x) for x in triangle_str]
                if len(tri) == 0:  # first string in 3 range, create lists
                    for no, item in enumerate(triangle):
                        tri.append(list())
                        tri[no].append(item)
                else:
                    for no, item in enumerate(triangle):
                        tri[no].append(item)
        if flag:  # estimate triangle descriptions
            for item in tri:
                if len(item) == 3:
                    item.sort()
                    if item[2] < item[1]+item[0]:
                        counter += 1
    return counter


def main():
    """ main function """
    with open(r"puzzles\aoc2016day03_data.txt", encoding="utf-8") as file:
        print(f"It is possible {count_valid_triangles_variant_1(
            file)} triangles using variant 1.")

    with open(r"puzzles\aoc2016day03_data.txt", encoding="utf-8") as file:
        print(f"It is possible {count_valid_triangles_variant_2(
            file)} triangles using variant 2.")


if __name__ == "__main__":
    main()
