class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = sorted(coins)
        table = [-1 for _ in range(amount + 1)]
        table[0] = 0
        for i in range(1, amount + 1):
            # print(f'{i}: {table}')
            for coin in coins:
                # print(f'\t{coin}: {table}')
                if i == coin:
                    table[i] = 1
                elif i - coin >= 0 and table[i - coin] != -1:
                    if table[i] == -1:
                        table[i] = table[i-coin] + 1
                    else:
                        table[i] = min(table[i - coin] + 1, table[i])
                # print(f'\t{table}')
            # print(f'{i}: {table}')
            # print()
        return table[-1]



        # sort it first
        # [2, 3, 5, 7] target  13
        # let a[i] = least number of coins to get i 
        # a[i] = min([a[coin] + 1  for each coin in coins if a[i-coin] != -1]) but if the array is mepty then -1.
        # [0 -1 1 1 -1 1 2 1 2 2 ...]
        # so run time will be O(nm) wher en is number of differnet coins and m is amount.

        # if we were to brute force it, we would consdier every possible comibnation plus combinatiosn where each of the numbers can appear more than once. Which will try more combinations then the dp appraoch as it recounts the least amount of coins up to target i again and again, so it's slower.

# [2, 5, 12]