def getNonRepeating(arr):
    arr.sort()
    repeating_number_removed = False
    result = []
    while (len(arr) != 0):
        if (len(arr) == 1):
            if (repeating_number_removed == False):
                result.append(arr.pop(0))
            else:
                return result
        elif (arr[0] == arr[1]):
            arr.pop(0)
            repeating_number_removed = True
        elif (repeating_number_removed):
            arr.pop(0)
            repeating_number_removed = False
        else:
            result.append(arr.pop(0))
    return result
print(getNonRepeating([1, 2, 3, 2, 1, 4, 5, 5]))
