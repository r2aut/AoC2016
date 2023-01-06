# --- Day 3: Squares With Three Sides ---

import io

def count_valid_triangles_variant_1(file):
    counter = 0
    for line in file:
        triangle_str = line.strip().split()
        triangle = [int(x) for x in  triangle_str]
        triangle.sort()
        if triangle[2] < triangle[1]+triangle[0]:
            counter += 1
    return counter
        
def count_valid_triangles_variant_2(file):
    counter = 0
    flag = True
    while(flag):
        tri = list()
        for i in range(3): # prepare several triangle descriptions using columns
            line = file.readline()
            if not line: # go out
                flag = False
                break
            if line:
                triangle_str = line.strip().split()
                triangle = [int(x) for x in  triangle_str]
                if not len(tri): # first string in 3 range, create lists
                    for no, item in enumerate(triangle):
                        tri.append(list())
                        tri[no].append(item)
                else:
                    for no, item in enumerate(triangle):
                        tri[no].append(item)
        if flag: # estimate triangle descriptions
            for item in tri:
                if len(item) == 3:
                    item.sort()
                    if item[2] < item[1]+item[0]:
                        counter += 1
    return counter

if __name__ == "__main__":

    with open(r"puzzles\T03_Squares_With_Three_Sides.txt") as file:
        print("It is possible {} triangles using variant 1.".format(count_valid_triangles_variant_1(file)))

    with open(r"puzzles\T03_Squares_With_Three_Sides.txt") as file:
        print("It is possible {} triangles using variant 2.".format(count_valid_triangles_variant_2(file)))
