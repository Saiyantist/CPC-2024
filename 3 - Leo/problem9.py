depth = int(input("depth: "))

def pascal_triangle(depth): 
    count = 1
    space = depth

    for i in range(depth):
        for j in range(space + 1, 0, -1):
            print(" ", end=" ")
        for j in range(1, count + 1):
            print(j, end=" ")
        count += 2
        space -= 1
        print()

pascal_triangle(depth)