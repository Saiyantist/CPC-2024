arr = list(input('input: '))
set_arr = set(arr)

for x in set_arr:
    if arr.count(x) == 1:
        print(x)

# Functionality: 5
# Performance: 3
# Quality: 3