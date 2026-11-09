class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:
            # print(f'before: {stack}')
            arrival_time = (target - p) / s
            stack.append(arrival_time)

            if len(stack) > 1 and stack[-1] <= stack[-2]: 
            # if the arrival time of the last car we added is earlier than the one before it, then it means it would have joined the previous car's fleet. 
                stack.pop()
            # print(f'after : {stack}')
            # print()
        return len(stack)