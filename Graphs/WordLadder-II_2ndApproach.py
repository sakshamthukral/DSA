from typing import List
from collections import deque
#------------------------Approach-2---------------------------------------------------------


def findShortestPathLevel(beginWord: str, wordList: List[str]):
    wordList = set(wordList)
    level_map = {}
    q = deque()
    q.append(beginWord)
    level_map[beginWord] = 0
    if beginWord in wordList:
        wordList.remove(beginWord)
    while q:
        front_word = q.popleft()
        level = level_map[front_word]
        wordLen = len(front_word)
        for i in range(wordLen):
            original = front_word
            for char in range(ord('a'), ord('z')+1):
                char_list = list(front_word)
                char_list[i] = chr(char)
                new_word = ''.join(char_list)
                if new_word in wordList:
                        q.append(new_word)
                        wordList.remove(new_word)
                        level_map[new_word] = level+1
            front_word = original

    return level_map

def dfs(word, beginWord, level_map, sequence, ans)-> List[List[str]]:
    if word == beginWord:
        ans.append(sequence[::-1])
        return
    word_len = len(word)
    level = level_map[word]
    for i in range(word_len):
        original = word
        for char in range(ord('a'), ord('z')+1):
            char_list = list(word)
            char_list[i] = chr(char)
            new_word = ''.join(char_list)
            if new_word in level_map.keys() and level == level_map[new_word]+1:
                sequence.append(new_word)
                dfs(new_word, beginWord, level_map, sequence, ans)
                sequence.pop()
        word = original
                    
def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    level_map = findShortestPathLevel(beginWord, wordList)
    ans = []
    sequence = []
    if endWord in level_map.keys():
        sequence.append(endWord)
        dfs(endWord, beginWord, level_map, sequence, ans)
    return ans

# Test case 1-----------
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# print(findLadders(beginWord, endWord, wordList))

# Test case 2---------------
beginWord = "a"
endWord = "c"
wordList = ["a","b","c"]
print(findLadders(beginWord, endWord, wordList))


# ------ Approach-1------------------------------------------------------------------------------------
# def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#     wordList = set(wordList)
#     if endWord not in wordList:
#         return []
#     q = deque()
    
#     q.append([beginWord])

#     usedOnLevel = set()
#     usedOnLevel.add(beginWord)
#     level = 1
#     ans = []

#     while q:
#         currentLevelSize = len(q)
#         currentLevelUsed = set()

#         for _ in range(currentLevelSize):
#             frontSequence = q.popleft()
#             print(type(frontSequence))
#             word = frontSequence[-1] # just need to apply the transformations on the last word of the sequence
#             if word == endWord:
#                 if len(ans) == 0 or len(ans[0]) == len(frontSequence):
#                     ans.append(frontSequence[:])
#                 continue
#             for i in range(len(word)):
#                 original = word
#                 for char in range(ord('a'), ord('z')+1):
#                     char_list = list(word)
#                     char_list[i] = chr(char)
#                     new_word = ''.join(char_list)

#                     if new_word in wordList and new_word not in usedOnLevel:
#                         newSequence = frontSequence[:]
#                         newSequence.append(new_word)
#                         q.append(newSequence)

#                         currentLevelUsed.add(new_word)
#                 word = original
#         usedOnLevel.update(currentLevelUsed)
#         level+=1
#     return ans

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# print(findLadders(beginWord, endWord, wordList))

