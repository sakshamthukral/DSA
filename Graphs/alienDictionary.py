# The following is a complete the implementation, i.e. it also captures the following 2 edge cases
# Edge Case-1: If everything matching and the longer string is coming before the the shorter string, then order is not possible.
# Edge Case-2: And when there is a cyclic dependency in the order


from collections import deque

def createGraph(alien_dict, N, K, adjList):
    for i in range(N-1):
        curr_word = alien_dict[i]
        next_word = alien_dict[i+1]
        order = False
        min_len = min(len(curr_word), len(next_word))
        for j in range(min_len):   
            if curr_word[j]!=next_word[j]:
                u = ord(curr_word[j])-ord('a') # normalizing to integral values (0..) using ASCII values
                v = ord(next_word[j])-ord('a') # normalizing to integral values (0..) using ASCII values
                adjList[u].append(v)
                order = True
                break # if a we got two character which a re different in the word, then we just need to identify their order and not need to check remaining character and move to next word
        
        # Edge Case-1
        if order == False and len(curr_word) > len(next_word):
            return False
    return True

                                                              
def findOrder(alien_dict, N, K):
    adjList = [[] for _ in range(K)]
    if createGraph(alien_dict, N, K, adjList):
        # Topo Sort 
        indegree = [0]*K
        for i in range(K):
            for neighbor in adjList[i]:
                indegree[neighbor]+=1
        
        q = deque()
        dict_order = []
        for i in range(K):
            if indegree[i] == 0:
                q.append(i)
        while len(q) != 0:
            front = q.popleft()
            dict_order.append(front)
            for neighbor in adjList[front]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        
        # Edge Case-2: Either we can do this i.e if the vertex is not captured by the topo sort, then it means theres a cyclic dependency anywhere therefore can't find the correct order and return "" (empty string) in this case
        # If we need to capture the edge case 2 i.e. cycle in the graph, we can simply check
        if len(dict_order)!=K:
            return ""
        

        # Or we can do this, according to which vertex can appear in any sequence irrespective of the order if they have not been captured by topo sort
        # To tackle the case if order for any vertex is not captured, then we can append it anywhere, at start or at end. In this case i am appending them at end.
        # for i in range(K): 
        #     if i not in dict_order:
        #         dict_order.append(i)
        
        # Converting the order back to a string
        ans = ""
        for ele in dict_order:
            ans+=chr(ele+ord('a'))
        return ans

    return ""


N = 5
K = 4
alien_dict = ["baa","abcd","abca","cab","cad"]
ans = findOrder(alien_dict, N, K)
print(ans)