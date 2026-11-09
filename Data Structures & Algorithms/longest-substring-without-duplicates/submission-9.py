class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        longest_l = 0
        seen = set()
        left= 0
        right = 0
        for char in s:
            # print(f'char: {char} seen: {seen}')
            if char in seen:
                while char in seen: # remove everything up to the instance of the dupe
                    # print(f'\tdiscarding: {s[left]}')
                    seen.discard(s[left]) # once removed the dupe we stop
                    left += 1
            seen.add(char)
            longest_l = max(longest_l, len(seen))
        return longest_l
        # # brute force
        # longest_l = 0
        # for i in range(len(s)):
        #     # print(f'i: {s[i]}')
        #     seen = {s[i]}
        #     j = i + 1
        #     l = 1
        #     while j < len(s) and s[j] not in seen:
        #         seen.add(s[j])
        #         # print(f'\tj: {s[j]} seen: {seen}')
        #         l += 1
        #         j += 1
        #     # print(f'l: {l}')
        #     longest_l = max(l, longest_l)
        # return longest_l
            

            

            



# xyxzzxzyz
# [y x]