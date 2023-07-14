class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)
        if endWord not in s:
            return 0
        q = deque([(beginWord, 1)])
        n = len(beginWord)
        s.discard(beginWord)
        while q:
            word, steps = q.popleft()
            for i in range(n):
                for char in range(26):
                    newWord = word[:i] + chr(97+char) + word[i+1:]
                    if newWord == endWord:
                        return steps + 1
                    if newWord in s:
                        s.discard(newWord)
                        q.append((newWord, steps + 1))
        return 0
