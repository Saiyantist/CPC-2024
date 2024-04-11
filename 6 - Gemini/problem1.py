arr = list(input('input: '))
set_arr = set(arr)

for x in set_arr:
    if arr.count(x) == 1:
        print(x)