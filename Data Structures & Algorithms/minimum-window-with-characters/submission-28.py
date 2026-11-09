from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = Counter()
        for char in t:
            t_dict[char] += 1

        best_sequence = None
        curr_counter = Counter()
        curr_sequence = deque()
        left = 0
        have = 0
        def dict_includes_t(d: dict) -> bool:
            for key in t_dict:
                if t_dict[key] > d[key]:
                    return False
            return True

        for right, char in enumerate(s): # O(n)
            # print(f'before: {s[left: right + 1]}')
            curr_counter[char] += 1
            if (char in t_dict) and (curr_counter[char] == t_dict[char]):
                have += 1
            while (
                (left < right) and
                (
                    (curr_counter[s[left]] > t_dict[s[left]])
                )
            ): # remove character until it starts with a t character and it's the rightmost appearance we've seen 
                # O(1) since once we only look at letters in curr_sequence. and curr_sequence goes from left to right of s, 
                # never repeating what it has seen
                # curr_sequence_char = curr_sequence.popleft()
                curr_counter[s[left]] -= 1
                if (s[left] in t_dict) and (curr_counter[s[left]] == t_dict[s[left]] - 1):
                    have -= 1
                left += 1
            # print(f'after: {s[left: right + 1]}')


            if dict_includes_t(curr_counter): # O(1) because 52 letters max
                # print('\tmatch!')
                if (
                    best_sequence is None or 
                    (best_sequence[1] - best_sequence[0]) > (right - left)
                ):
                    best_sequence = (left, right + 1)
                    # print(f'\tbest_sequence: {s[best_sequence[0]: best_sequence[1]]}')
                    # print()
                    # best_sequence = curr_sequence

        return s[best_sequence[0]: best_sequence[1]] if best_sequence and best_sequence[0] < best_sequence[1] else ""
                 # return best_sequence if best_sequence else ""
    