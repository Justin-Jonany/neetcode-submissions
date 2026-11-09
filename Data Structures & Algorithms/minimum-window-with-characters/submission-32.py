from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = defaultdict(int)
        for char in t:
            t_dict[char] += 1

        best_sequence = None
        curr_counter = defaultdict(int)
        left = 0
        have = 0

        for right, char in enumerate(s): # O(n)
            # print(f'before: {s[left: right + 1]}')
            curr_counter[char] += 1
            if (char in t_dict) and (curr_counter[char] == t_dict.get(char, 0)):
                have += 1
            while (
                (left < right) and
                (
                    (curr_counter[s[left]] > t_dict.get(s[left], 0))
                )
            ): # remove character until it starts with a t character and it's the rightmost appearance we've seen 
                # O(1) since once we only look at letters in curr_sequence. and curr_sequence goes from left to right of s, 
                # never repeating what it has seen
                curr_counter[s[left]] -= 1
                if (s[left] in t_dict) and (curr_counter[s[left]] == t_dict.get(s[left], 0) - 1):
                    have -= 1
                left += 1
            # print(f'after: {s[left: right + 1]}')


            if have == len(t_dict): # O(1) because 52 letters max
                # print('\tmatch!')
                if (
                    best_sequence is None or 
                    (best_sequence[1] - best_sequence[0]) > (right - left)
                ):
                    best_sequence = (left, right + 1)
                    # print(f'\tbest_sequence: {s[best_sequence[0]: best_sequence[1]]}')
                    # print()

        return s[best_sequence[0]: best_sequence[1]] if best_sequence and best_sequence[0] < best_sequence[1] else ""
    