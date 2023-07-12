class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)
        if endWord not in s:
            return 0
        vis = set()
        q = deque([(beginWord, 1)])
        res = float("inf")
        n = len(beginWord)
        vis.add(beginWord)
        while q:
            word, steps = q.popleft()
            for i in range(n):
                for char in range(26):
                    newWord = word[:i] + chr(97+char) + word[i+1:]
                    if newWord == endWord:
                        return steps + 1
                    if (newWord not in vis) and (newWord in s):
                        vis.add(newWord)
                        q.append((newWord, steps + 1))
        return 0
