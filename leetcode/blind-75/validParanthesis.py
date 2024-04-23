def isValid(s)->bool:
    stack = []
    for character in s:
        if character in "([{":
            stack.append(character)
        else:
            if len(stack)==0:
                return False
            top = stack.pop()
            if character == ")" and top != "(":
                    return False
            elif character == "]" and top != "[":
                    return False
            else: # "}"
                if character == "}" and top != "{":
                    return False
    return len(stack) == 0

s=input()
print(isValid(s))