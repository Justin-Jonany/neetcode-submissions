class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        table = [False for _ in range(len(s) + 1)]
        table[0] = True
        for i in range(1, len(s) + 1):
            # print(f'{i}')
            for word in wordDict:
                # print(f'word: {word}')
                # print(f'\ttable: {table}')
                # print(f'\ttable[i - len(word)]: {table[i - len(word)]}')
                # print(f'\ts[i-len(word):+1] == word: {s[i-len(word):i] == word}')
                # print(f'\ts[i-len(word):+1]: {s[i-len(word): i + 1]}')
                if i >= len(word) and table[i - len(word)] and s[i-len(word):i] == word:
                    table[i] = True
        return table[-1]


        # dp.
        # 1d array
        # a[i] = up letters i, is the letter breakable? 
        # a[i] = for each word we check if the last len(word) matches it and a[i - len(word)] is True. If it's than true. otherwise False. 
