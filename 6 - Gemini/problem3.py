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

input_string = input("Input: ")
print(parentheses_checker(input_string))