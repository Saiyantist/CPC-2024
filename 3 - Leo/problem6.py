arr = [2, 1, 3, 2, 4, 3]


def getNonRepeating(arr):
    sortedArr = sorted(arr)
    distinctArr = []
    step = 0


    [print(str(i), end=" ") for i in sortedArr]    
    if sortedArr[0] != sortedArr[1]:
        step = 1
        distinctArr.append(sortedArr[0])
    else: 
        step = 2

    for k in range(1, len(sortedArr), step):
        print(step)
        if sortedArr[k - 1] != sortedArr[k]:
            step = 1
            distinctArr.append(sortedArr[k - 1])
        elif k == len(sortedArr) - 1 and sortedArr[k - 1] != sortedArr[k]:
            distinctArr.append(sortedArr[k])
        else: 
            step = 2

    print()
    [print(str(i), end=" ") for i in distinctArr]

getNonRepeating(arr)