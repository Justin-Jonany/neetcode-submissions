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

        for char in s:
            # print(f'{char}: {best_sequence}')
            if (
                all(v == 0 for v in curr_counter.values()) and
                (char not in t_dict)
            ):
            
                # print('\tskipping')
                continue
            # print(f'\curr_sequence[0] == char: {curr_sequence[0] == char}')
            # print(f'\tlen(curr_counter for t_char in t_dict if curr_counter[t_char] > 0)== 1: {len([curr_counter for t_char in t_dict if curr_counter[t_char] > 0]) == 1}')

            curr_counter[char] += 1
            curr_sequence.append(char)
            # if (curr_sequence and curr_sequence[0] == char and curr_counter[char] >= t_dict[char]): # remove the first occurence of that char up to the new appearance or any t keys
            # print(f'\t INITIAL REMOVAL curr_sequence:{curr_sequence}')
            # curr_sequence_char = curr_sequence.popleft() # no need to modify count
            while (
                (curr_sequence and curr_sequence[0] not in t_dict) or
                (curr_counter[curr_sequence[0]] > t_dict[curr_sequence[0]])
            ):
                curr_sequence_char = curr_sequence.popleft()
                curr_counter[curr_sequence_char] -= 1
            # print(f'\t INITIAL REMOVAL curr_sequence:{curr_sequence}')
            # print('\tadded')
            # print(f'\tcurr_counter: {dict(curr_counter)} curr_sequence: {''.join(curr_sequence)} dict_includes_t(curr_counter): {dict_includes_t(curr_counter)}')
            if dict_includes_t(curr_counter):
                # print(f'\t\tlen(best_sequence) > len(curr_sequence): {len(best_sequence) if best_sequence else "None"} > {len(curr_sequence)}')
                if (
                    best_sequence is None or 
                    len(best_sequence) > len(curr_sequence)
                ):
                    best_sequence = ''.join(curr_sequence)
                # print(f'\t\tcurr_sequence:{curr_sequence}')
                while (
                    all(curr_counter[t_char] >= t_dict[t_char] for t_char in t_dict) or
                    (curr_sequence and curr_sequence[0] not in t_dict)
                ): # remove character until one of t char is 0
                    # print(f'\t\t\tcurr_counter: {dict(curr_counter)}: {curr_sequence}')
                    curr_sequence_char = curr_sequence.popleft()
                    curr_counter[curr_sequence_char] -= 1
                # print(f'all(curr_counter[t_char] >= t_dict[t_char] for t_char in t_dict) : {all(curr_counter[t_char] >= t_dict[t_char] for t_char in t_dict) }')

                # print(f'\t\tcurr_sequence:{curr_sequence}')
            # print('*'*100)
        return best_sequence if best_sequence else ""
                    
                        







#         s_dict = defaultdict(int)
#         for char in s:
#             s_dict[char] += 1
#         t_dict = defaultdict(int)
#         for char in t:
#             t_dict[char] += 1

#         left = 0
#         right = len(s)
#         left_counter = defaultdict(int)
#         for char in s:
#             print(s[left:right])
#             if s_dict[char] - 1 >= t_dict[char]:
#                 left += 1
#                 s_dict[char] -= 1
#             else:
#                 break
#         print()
#         for char in reversed(s):
#             print(s[left:right])
#             # print(f's_dict[char] - 1 >= t_dict[char] ')
#             if s_dict[char] - 1 >= t_dict[char]:
#                 right -= 1
#                 s_dict[char] -= 1
#             else:
#                 break

#         for key in t_dict:
#             if s_dict[key] < t_dict[key]:
#                 return ""
        

#         return s[left:right]



# s="baAaABabBba"
# t="AbbB"
# {'A': 1, 'b': 2,'B': 1}