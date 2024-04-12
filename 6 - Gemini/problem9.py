def create_pyramid(depth:int):
    left_lim = depth
    right_lim = 2*depth - 1
    for i in range (1,depth+1):
        print('  '*(depth-i),end="")
        for j in range (1,i*2-1+1):
            print(str(j) + " ",end="")
        print()

depth = int(input("Depth: "))
create_pyramid(depth)

# Functionality: 5
# Performance: 4.5
# Quality: 4