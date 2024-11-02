# Problem Link:- https://leetcode.com/problems/word-ladder/submissions/1337258965/
from typing import List
from collections import deque

# Brute Force Approach using BFS: 
# Time complexity: O(N x word_length x 26 x log N), where 
# - N is because at max the queue will be iterated N number of times, where N is the number of words in wordlist, because we are only adding words which are part of wordlist and that too only once.
# - word_length x 26, because for each character position in word, we are testing all the possible character combination i.e. from a-z
# - log N,  because if we are converting our wordlist to a set, and set operations are logarithmic time.

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    q = deque()
    words_list = set(wordList)
    q.append((beginWord,1))
    if beginWord in words_list:
        words_list.remove(beginWord)
    while len(q) != 0:
        front = q.popleft()
        word = front[0]
        original = word
        steps = front[1]
        if word == endWord:
            return steps
        for i in range(len(word)):
            for char in range(ord('a'), ord('z')+1):
                char_list = list(word)
                char_list[i] = chr(char)
                new_word = ''.join(char_list)
                if new_word in words_list:
                    q.append((new_word, steps+1))
                    words_list.remove(new_word)
            word = original
    return 0
    


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))
