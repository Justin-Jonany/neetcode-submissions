class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            # print(f'stack: {stack}   days: {days}   temperature: {temperature}')
            while len(stack) > 0 and stack[-1][1] < temperature:
                popped_i, popped_temperature = stack.pop()
                days[popped_i] =  i - popped_i

            # print(f'stack: {stack}    temperature: {temperature}')
            # print()
            stack.append((i, temperature))
        return days


                

        # [30,38,30,36,35,40,28]
        # [38]
        # temperature = 40
        # 1, 38

        # [1, 0, 1, 2, 1, 0, 0]