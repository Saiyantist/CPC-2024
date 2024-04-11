def pascal_triangle(depth):
    x = 1
    z = depth
    a = (depth * 2) + 1
    while x != a:
        while z != x:
            print(" ", end ="")
            z = z - 1
        if x % 2 == 0:
            for y in range(1, x):
                print(y, end = " ")
        else:
            print()
        x = x + 1
        z = a
        
pascal_triangle(6)

