class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = defaultdict(int)
        for char in t:
            t_dict[char] += 1

        best_sequence = None
        curr_counter = defaultdict(int)
        curr_sequence = deque()
        left = 0
        def dict_includes_t(d: dict) -> bool:
            for key in t_dict:
                if t_dict[key] > d[key]:
                    return False
            return True

        for right, char in enumerate(s): # O(n)
            if (
                all(v == 0 for v in curr_counter.values()) and # O(1) because 52 letters so max dict with 52 keys
                (char not in t_dict)
            ):
                left += 1
                continue

            curr_counter[char] += 1
            # left += 1
            # curr_sequence.append(char)
            # print(f'before: {s[left: right + 1]}')
            while (
                (left < right) and
                (
                    ((right - left > 0) and s[left] not in t_dict) or
                    (curr_counter[s[left]] > t_dict[s[left]])
                )
            ): # remove character until it starts with a t character and it's the rightmost appearance we've seen 
                # O(1) since once we only look at letters in curr_sequence. and curr_sequence goes from left to right of s, 
                # never repeating what it has seen
                # curr_sequence_char = curr_sequence.popleft()
                curr_counter[s[left]] -= 1
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

                while (
                    (left < right) and
                    (
                        all(curr_counter[t_char] >= t_dict[t_char] for t_char in t_dict) or
                        ((right - left > 0) and s[left] not in t_dict)
                    )
                ): # remove character until curr_sequence no longer has the required characters and it doesn't start with a t character.
                # O(1) since curr_sequence is at most len(s) never readds characters it has seen. So all iterations adds up to O(n)
                    # curr_sequence_char = curr_sequence.popleft()
                    curr_counter[s[left]] -= 1
                    left += 1
        return s[best_sequence[0]: best_sequence[1]] if best_sequence and best_sequence[0] < best_sequence[1] else ""
                 # return best_sequence if best_sequence else ""
    