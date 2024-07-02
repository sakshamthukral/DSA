def checkParenthesis(s):
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if len(stack) == 0 and char in ")}]":
                return False
            elif char == ')' and stack[-1] != '(':
                return False 
            elif char == '}' and stack[-1] != '{':
                return False 
            elif char == ']' and stack[-1] != '[':
                return False 
            elif char not in ")}]":
                continue
            stack.pop()
    if len(stack)!=0:
        return False
    else:
        return True

s = "[sd(ab)]asb"
print(checkParenthesis(s))







# Test cases
# [sd(ab)]