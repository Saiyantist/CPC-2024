def find_unique_number(arr):
    arr.sort()
    unique_num : int
    repeating_number = False
    while (len(arr) != 1):
        if (len(arr) == 2):
            if (repeating_number):
                unique_num = arr[1]
                break
        elif (arr[0] == arr[1]):
            arr.pop(0)
            repeating_number = True
            continue
        elif (repeating_number):
            arr.pop(0)
            repeating_number = False
    return unique_num
print(find_unique_number([2, 3, 5, 3, 2]))
# print(find_unique_number([1, 1, 2, 2, 3, 3, 4]))
