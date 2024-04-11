s = "(()())"
def is_balanced_parentheses(s):

    if s == "(" and ")":
        return True
    else:
        return False

print(is_balanced_parentheses(s))
