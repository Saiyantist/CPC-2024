import math
def pascal_training(depth):
    string_count = [1]
    for i in range(1, depth):
        string_count.append(string_count[-1]+2)
    space = string_count[-1] * 2 - 1
    result = []
    for j in string_count:
        n = []
        for k in range(j):
            n.append(str(k+1))
        numbers = ' '.join(n)
        result.append(numbers.center(space))
    return '\n'.join(result)
print(pascal_training(5))

# Functionality: 5
# Performance: 4
# Quality: 4