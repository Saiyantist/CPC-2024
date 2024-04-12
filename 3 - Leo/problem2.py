arr = [3, 4, -1, 1, -2]

def find_smallest_missing_positive(arr):
    sortedArr = sorted(arr)
    positiveArr = []
    missing = 0
    gap = False

    for i in sortedArr:
        if i > 0:
            positiveArr.append(i)
    
    prev = 0

    for k, i in enumerate(positiveArr):
        if positiveArr[prev] + 1 == i:
            missing = positiveArr[len(positiveArr) - 1] + 1
            gap = False
        else:
            missing = i + 1
            gap = True
            break
        prev = k

    if gap != True:
            print("output:"+str(missing))
            print("Since the array contains `", end="")
            [print(str(i), end=",") for i in positiveArr]
            print("` without any gap, the smallest missing positive number is `"+str(missing)+"`.")
    else:
            print("output:"+str(missing))
            print("After sorting the positive numbers and ignoring the negative ones, the array looks like `", end="")
            [print(str(i), end=",") for i in positiveArr]
            print("`. The smallest missing positive number is `"+str(missing)+"`.")

find_smallest_missing_positive(arr)

# Functionality: 4
# Performance: 3
# Quality: 4.5