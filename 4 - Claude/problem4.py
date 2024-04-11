def reverse_string(string):
    arr = list(string)
    result = []
    for i in arr:
        result.insert(0, i)
    return ''.join(result)
print(reverse_string("ecnegilletnI"))