def sortStack(input):
    tempStack = []
    while(len(input)>0):
        tmp = input[-1]
        input.pop()

        while(len(tempStack)>0 and tmp>tempStack[-1]):
            input.append(tempStack[-1])
            tempStack.pop()
        tempStack.append(tmp)
    return tempStack


def sortArray(arr, n):
    input = []
    for ele in arr:
        input.append(ele)
    sortedStack = sortStack(input)
    ans =[]

    while (len(sortedStack)>0):
        ans.append(sortedStack[-1])
        sortedStack.pop()
    return ans

arr = [5, 4, 3, 2, 1]
n = 5
print(sortArray(arr, n)) # [1, 2, 3, 4, 5]