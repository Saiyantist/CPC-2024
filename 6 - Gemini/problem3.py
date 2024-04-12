from collections import deque
def parentheses_checker(S):
    # init a deque
    dq = deque()
    for char in S:
        if char == "(":
            dq.appendleft("(")
        else:
            if len(dq) == 0:
                return False
            else:
                dq.popleft()
    if len(dq) == 0:
        return True
    
    return False

# input_string = input("Input: ")

input_string1 = ")(())"
# Should return false

input_string2 = "(()())" 
# Should return true

input_string3 = "(()())))(())" 
# Should return false

print(parentheses_checker(input_string1))
print(parentheses_checker(input_string2))
print(parentheses_checker(input_string3))