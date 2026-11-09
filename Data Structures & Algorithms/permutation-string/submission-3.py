class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        s1_dict = defaultdict(int)
        for char in s1:
            s1_dict[char] += 1
        
        s2_dict = defaultdict(int)
        for char in s2[:window_size]:
            s2_dict[char] += 1

        def part_of_dict1(dict1: dict, dict2: dict) -> bool:
            for key in dict1:
                if (key not in dict2) or (dict2[key] != dict1[key]):
                    return False
            return True
        
        for i in range(window_size, len(s2)):
            if part_of_dict1(s1_dict, s2_dict): # O(1) because dict only contains lowercase letter, so at most doest 26 iterations
                return True
            s2_dict[s2[i - window_size]] -= 1 # remove the left
            s2_dict[s2[i]] += 1 # add the right

        return part_of_dict1(s1_dict, s2_dict)

        # lecabee
        # abc
        # a: 1 b: 1 c: 1


        # cab
        # l: 0 e: 0 c: 1 a: 1 b: 1
        