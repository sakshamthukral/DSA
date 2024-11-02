from typing import List
from collections import deque

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    # Push all values of wordList into a set
    # to make deletion from it easier and in less time complexity.
    wordList = set(wordList)
    
    # If the endWord is not in the wordList, no solution exists
    if endWord not in wordList:  # <-- Add this check to return an empty list if endWord is not in wordList
        return []

    # Creating a queue ds which stores the words in a sequence which is
    # required to reach the targetWord after successive transformations.
    q = deque()
    
    # BFS traversal with pushing the new formed sequence in queue 
    # when after a transformation, a word is found in wordList.
    q.append([beginWord]) 

    # An array defined to store the words being currently used on a level during BFS
    usedOnLevel = set()
    usedOnLevel.add(beginWord)
    level = 1

    # A vector to store the resultant transformations
    ans = []

    while q:
        currentLevelSize = len(q)
        currentLevelUsed = set()

        for _ in range(currentLevelSize):
            front_sequence = q.popleft()
            word = front_sequence[-1]
        
            # Store the answer if the endWord matches with the target word
            if word == endWord:
                if len(ans) == 0 or len(ans[0]) == len(front_sequence): # how are you ensuring that only the shortest sequence is being stored? Ans: We are using BFS, and the first sequence that will reach the endWord witll in itseld be the shortest sequence
                    ans.append(front_sequence[:])
                continue

            for i in range(len(word)):
                # Now, replace each character of ‘word’ with char
                # from a-z then check if ‘word’ exists in wordList.
                original = word
                for char in range(ord('a'), ord('z')+1):
                    char_list = list(word)
                    char_list[i] = chr(char)
                    new_word = ''.join(char_list)

                    if new_word in wordList and new_word not in usedOnLevel:
                        # Check if the word is present in the wordList and
                        # push the word along with the new sequence in the queue.
                        new_sequence = front_sequence[:]
                        new_sequence.append(new_word)
                        q.append(new_sequence)

                        # Mark as visited on the level
                        currentLevelUsed.add(new_word)
                word = original

        # Move this block inside the main while loop
        usedOnLevel.update(currentLevelUsed)
        level += 1

    return ans

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
res = findLadders(beginWord, endWord, wordList)
print(res)
