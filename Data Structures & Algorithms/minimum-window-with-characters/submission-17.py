class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = defaultdict(int)
        for char in t:
            t_dict[char] += 1

        best_sequence = None
        curr_counter = defaultdict(int)
        curr_sequence = deque()
        def dict_includes_t(d: dict) -> bool:
            for key in t_dict:
                if t_dict[key] > d[key]:
                    return False
            return True

        for char in s: # O(n^2)
            if (
                all(v == 0 for v in curr_counter.values()) and # O(1) because 52 letters so max dict with 52 keys
                (char not in t_dict)
            ):
                continue

            curr_counter[char] += 1
            curr_sequence.append(char)

            while (
                (curr_sequence and curr_sequence[0] not in t_dict) or
                (curr_counter[curr_sequence[0]] > t_dict[curr_sequence[0]])
            ): # remove character until it starts with a t character and it's the rightmost appearance we've seen 
                # O(1) since once we only look at letters in curr_sequence. and curr_sequence goes from left to right of s, 
                # never repeating what it has seen
                curr_sequence_char = curr_sequence.popleft()
                curr_counter[curr_sequence_char] -= 1

            if dict_includes_t(curr_counter): # O(1) because 52 letters max
                if (
                    best_sequence is None or 
                    len(best_sequence) > len(curr_sequence)
                ):
                    # print(f"''.join(curr_sequence): {''.join(curr_sequence)}")
                    # print(f'curr_sequence: {curr_sequence}')
                    # print()
                    best_sequence = ''.join(curr_sequence)
                    # best_sequence = curr_sequence

                while (
                    all(curr_counter[t_char] >= t_dict[t_char] for t_char in t_dict) or
                    (curr_sequence and curr_sequence[0] not in t_dict)
                ): # remove character until curr_sequence no longer has the required characters and it doesn't start with a t character.
                # O(1) since curr_sequence is at most len(s) never readds characters it has seen. So all iterations adds up to O(n)
                    curr_sequence_char = curr_sequence.popleft()
                    curr_counter[curr_sequence_char] -= 1
        # best_sequence = ''.join(best_sequence) if best_sequence else None
        # return best_sequence if best_sequence else ""
        return ''.join(best_sequence) if best_sequence else ""
    