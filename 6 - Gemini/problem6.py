def unique_nums(arr):
    
    set_arr = set(arr)
    uniques = []
    for x in set_arr:
        if arr.count(x) == 1:
            uniques.append(x)

    return sorted(uniques)
        
arr = list(input("Input: "))
solution = unique_nums(arr)
print(f"Output:\n{solution[0]} {solution[1]}")

Functionality: 4
Performance: 4
Quality: 3.5