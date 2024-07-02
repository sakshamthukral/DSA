def helper(curr):
    if len(curr) == 35:
        return
    helper(curr+"(")
    print(curr)
def trigger():
    curr=""
    helper(curr)

trigger()
